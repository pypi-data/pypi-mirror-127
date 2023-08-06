from endpointlib.devices.serial_device import SerialDevice
from endpointlib.devices.socket_device import SocketDevice
from endpointlib.endpoints.endpoint import Endpoint
from endpointlib.endpoints.endpoint_device import EndpointDevice
from endpointlib.endpoints.endpoint_monitor_device import EndpointMonitorDevice

class EndpointFactory:

    @staticmethod
    def basic_endpoint(mqtt_connection, main_callback=None, handlers=None, on_idle_callback=None, idle_delay=1):
        return Endpoint(host=mqtt_connection[0], port=mqtt_connection[1], main_callback=main_callback,
                    handlers=handlers, on_idle_callback=on_idle_callback, idle_delay=idle_delay)

    @staticmethod
    def socket_endpoint(mqtt_connection, socket_connection, main_callback=None, handlers=None,
            on_idle_callback=None, idle_delay=1):
        return EndpointDevice(host=mqtt_connection[0], port=mqtt_connection[1],
                    device=SocketDevice(socket_connection[0], socket_connection[1]),
                    main_callback=main_callback, handlers=handlers,
                    on_idle_callback=on_idle_callback, idle_delay=idle_delay)

    @staticmethod
    def socket_monitor_endpoint(mqtt_connection, socket_monitor, main_callback=None, handlers=None,
            on_idle_callback=None, idle_delay=1):
        return EndpointMonitorDevice(host=mqtt_connection[0], port=mqtt_connection[1],
                    device=SocketDevice(socket_monitor[0], socket_monitor[1]),
                    delay=socket_monitor[2], command=socket_monitor[3],
                    on_monitor_callback=socket_monitor[4], main_callback=main_callback, handlers=handlers,
                    on_idle_callback=on_idle_callback, idle_delay=idle_delay)

    @staticmethod
    def serial_endpoint(mqtt_connection, serial_connection, main_callback=None, handlers=None,
            on_idle_callback=None, idle_delay=1):
        return EndpointDevice(host=mqtt_connection[0], port=mqtt_connection[1],
                    device=SerialDevice(serial_connection[0], serial_connection[1]),
                    main_callback=main_callback, handlers=handlers,
                    on_idle_callback=on_idle_callback, idle_delay=idle_delay)

    @staticmethod
    def serial_monitor_endpoint(mqtt_connection, serial_monitor, main_callback=None, handlers=None,
            on_idle_callback=None, idle_delay=1):
        return EndpointMonitorDevice(host=mqtt_connection[0], port=mqtt_connection[1],
                    device=SerialDevice(serial_monitor[0], serial_monitor[1]),
                    delay=serial_monitor[2], command=serial_monitor[3],
                    on_monitor_callback=serial_monitor[4], main_callback=main_callback,
                    handlers=handlers, on_idle_callback=on_idle_callback, idle_delay=idle_delay)
