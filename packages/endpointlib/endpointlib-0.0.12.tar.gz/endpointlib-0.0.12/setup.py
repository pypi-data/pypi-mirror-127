from setuptools import setup

setup(
    name='endpointlib',
    packages=['endpointlib', 'endpointlib.clients', 'endpointlib.connections', 'endpointlib.devices', 'endpointlib.endpoints',
                'endpointlib.helpers', 'endpointlib.helpers.loggers'],
    package_dir={'': '.'},
    version='0.0.12',
    description='MQTT Endpoint Library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='afranco',
    author_email='afranco@astro.unam.mx',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.7',
    install_requires=['paho-mqtt==1.5.1', 'pyserial-asyncio==0.5', 'asyncio-mqtt==0.10.0', 'aiologger==0.6.1'],
    setup_requires=['pytest-runner==5.3.1'],
    tests_require=['pytest==6.2.4', 'pytest-asyncio==0.15.1'],
    test_suite='tests',
    project_urls={
        'Source': 'https://github.com/afranco-astro/endpoint-lib/'
    }
)
