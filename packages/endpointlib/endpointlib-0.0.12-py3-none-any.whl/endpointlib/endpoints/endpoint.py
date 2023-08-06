import asyncio
import inspect
import signal
import threading
import uuid

from endpointlib.clients.mqtt_async_client import MQTTAsyncClient
from endpointlib.helpers.loggers.logger_manager import LoggerManager

class Endpoint:
    def __init__(self, host, port, main_callback=None, handlers=None, on_idle_callback=None, idle_delay=1):
        if (handlers is None):
            handlers = dict()
        self.id = str(uuid.uuid4())
        self.host = host
        self.port = port
        self._main_callback = main_callback
        self._handlers = handlers
        self._on_idle = on_idle_callback
        self._idle_delay = idle_delay
        self._command_handlers = dict()
        self._mqtt_publisher = None
        self._on_tasks_initializing = 0
        self._on_tasks_initializing_lock = asyncio.Lock()
        self._on_tasks_ready = asyncio.Event()
        self._logger = LoggerManager.get_async_logger(name='endpointlib')
        self._inner_tasks = []

    def get_id(self):
        return self._id
    
    def get_logger(self):
        return self._logger

    def create_id(self):
        return str(uuid.uuid4())

    async def run_forever(self):
        loop = asyncio.get_event_loop()
        signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
        for s in signals:
            loop.add_signal_handler(
                s, lambda s=s: asyncio.create_task(self._shutdown(signal=s)))

        tasks = self.get_core_tasks()
        async with self._on_tasks_initializing_lock:
            self._on_tasks_initializing = len(tasks)
        tasks.extend(self.get_tasks_started_by(self._on_tasks_ready))

        self._store_inner_tasks_ids(tasks)

        try:
            await asyncio.gather(*tasks, return_exceptions=False)
        except asyncio.CancelledError:
            pass
        except Exception:
            await self._shutdown(signal=signal.SIGTERM)

    def shutdown(self):
        id = threading.get_ident()
        signal.pthread_kill(id, signal.SIGTERM)

    async def _shutdown(self, signal):     
        tasks = [t for t in asyncio.all_tasks()
                    if t is not asyncio.current_task()
                    and self._is_inner_task(t)]

        await self._logger.info('Shutting down endpointlib tasks...')
        [task.cancel() for task in tasks]
        await asyncio.gather(*tasks, return_exceptions=True)
        await self._logger.info('Shut down completed')
        await asyncio.sleep(1)

    def get_core_tasks(self):
        tasks = []
        tasks.append(self.create_task(self.run_mqtt_client()))
        tasks.append(self.create_task(self.prepare_mqtt_publisher()))
        return tasks

    def _store_inner_tasks_ids(self, tasks):
        for task in tasks:
            _id = id(task)
            self._inner_tasks.append(_id)

    def _is_inner_task(self, task):
        _id = id(task)
        return _id in self._inner_tasks

    def create_task(self, coro):
        return asyncio.create_task(coro=coro)

    def get_tasks_started_by(self, on_tasks_ready):
        tasks = []
        tasks.append(self.create_task(self._main_wrapper(on_tasks_ready)))
        tasks.append(self.create_task(self._idle_loop(on_tasks_ready)))

        additional = self.get_additional_tasks(on_tasks_ready)
        for add in additional:
            tasks.append(self.create_task(add))

        return tasks

    def get_additional_tasks(self, on_tasks_ready):
        return []

    async def on_task_initialized(self):
        raiseEvent = False
        async with self._on_tasks_initializing_lock:
            self._on_tasks_initializing -= 1
            raiseEvent = self._on_tasks_initializing == 0
        if (raiseEvent):
            self._on_tasks_ready.set()

    async def run_mqtt_client(self):
        async with MQTTAsyncClient(id=self.id, host=self.host, port=self.port) as client:
            await client.connect()
            self.setup_process_message(client=client)
            await self._setup_command_handlers(client)
            await self.on_task_initialized()
            await client.loop_forever()

    async def prepare_mqtt_publisher(self):
        self._mqtt_publisher = MQTTAsyncClient(id=self.create_id(), host=self.host, port=self.port)
        await self._mqtt_publisher.connect()
        await self.on_task_initialized()

    def get_handlers(self):
        return dict()

    def get_command_handlers(self):
        return self._command_handlers

    def setup_process_message(self, client):
        client.process_message = self._process_message

    def get_mqtt_publisher(self):
        return self._mqtt_publisher

    # Publish to the default broker host
    async def publish(self, topic, payload, qos=0, retain=False):
        await self._mqtt_publisher.publish(topic=topic, payload=payload, qos=qos, retain=retain)

    # Use this method when you want to publish to another mqtt broker
    async def publish_to(self, connection, topic, payload, qos=0, retain=False):
        try:
            async with MQTTAsyncClient(id=self.create_id(), host=connection[0], port=connection[1]) as client:
                await client.connect()
                await client.publish(topic=topic, payload=payload, qos=qos, retain=retain)
        except Exception as ex:
            await self._logger.error(str(ex))

    async def _main_wrapper(self, on_tasks_ready):
        await on_tasks_ready.wait()
        if (self._main_callback):
            await self._main_callback()
        else:
            await self.on_main()

    async def on_main(self):
        pass

    async def _idle_loop(self, on_tasks_ready):
        await on_tasks_ready.wait()
        while True:
            try:
                if(self._on_idle):
                    await self._on_idle()
                else:
                    await self.on_idle()
            except Exception as ex:
                await self._logger.error(str(ex))
            finally:
                await asyncio.sleep(self.get_idle_delay())

    async def on_idle(self):
        pass

    def get_idle_delay(self):
        return self._idle_delay

    async def _setup_command_handlers(self, client):
        topics = set()
        if (not self._handlers):
            for k, v in self.get_handlers().items():
                self._command_handlers[k] = v
                topics.add(k)
        else:
            for k, v in self._handlers.items():
                self._command_handlers[k] = v
                topics.add(k)
        await client.subscribe(topics)

    async def _process_message(self, topic, payload):
        handler = self._command_handlers.get(topic, None)
        if (handler is not None):
            if inspect.iscoroutinefunction(handler):
                params = len(inspect.signature(handler).parameters)
                if (params == 2):
                    await handler(topic, payload)
            else:
                await asyncio.get_event_loop().run_in_executor(None, handler, topic, payload)
