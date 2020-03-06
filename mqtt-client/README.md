# MQTT Client examples

All provided examples follow a simple but complete MQTT client workflow:

* connect to mqtt broker
* subscribe to "test" topic
* publish a message to the "test" topic
* receive published message in a separate callback
* disconnect from the mqtt broker

The expected stdout output will be like this:

```
mqtt client created, connecting...
connected, subscribing to "test" topic...
subscribed to "test" topic, publishing message...
received message in topic "test": "hello from flespi mqtt client example script!"
disconnecting...
disconnected
```

## Requirements: flespi token

To connect to [flespi mqtt broker](https://flespi.com/mqtt-broker) you have to obtain a **flespi token**.

Please [refer here](https://flespi.com/kb/tokens-access-keys-to-flespi-platform) to read how to do it (don't worry, it's fast and simple).

To run these examples you need a **flespi token** allowing to publish and subscribe to "test" topic.
That may be a **Standard** token, a **Master** token (although using it in the example may be excessive) or an [**ACL** token](https://flespi.com/blog/take-control-of-token-access-permissions-with-flexible-acls) (see the "Token for MQTT broker" section).

## nodejs

Example source code is located at [./nodejs/](./nodejs/)

To run the example you need to install the dependencies ([mqtt](https://github.com/mqttjs/MQTT.js) package):

```sh
npm install
```

And then run the example script with the **flespi token** passed through the process environment:

```sh
FlespiToken=XXXXXXXXXXXXXXX node ./example.js
```

## python

Example source code is located at [./python/](./python/)

To run the example you need to install the dependencies ([gmqtt](https://github.com/wialon/gmqtt) package):

```sh
# optionally create and activate the virtualenv
virtualenv venv
. venv/bin/activate

# install requirements
pip install -r requirements.txt
```

And then run the example script with the **flespi token** passed through the process environment:

```sh
# optionally use created virtualenv
. venv/bin/activate

# run example
FlespiToken=XXXXXXXXXXXXXXX python ./example.py
```

## python-windows

Example source code is located at [./python-windows/](./python-windows/).
The only difference in the windows version is missing the uvloop module and not handling signals (windows does not have them).

To run the example you need to install the dependencies ([gmqtt](https://github.com/wialon/gmqtt) package):

```cmd
rem   optionally create and activate the virtualenv
python -m venv venv
venv\Scripts\activate.bat

rem   install requirements
pip install -r requirements.txt
```

And then run the example script with the **flespi token** passed through the process environment:

```cmd
rem   optionally use created virtualenv
venv\Scripts\activate.bat

rem   run example
set FlespiToken=XXXXXXXXXXXXXXX
python example.py
```

## micropython (esp8266)

Example source code is located at [./micropython/](./micropython/)

![esp8266 micropython mqtt](./micropython/esp.jpg?raw=true "esp8266 with micropython")

We used a NodeMCU(esp8266) board with preinstalled light sensor that sends sensor value to topic "myesp/light".

To run the example you need to flash [micropython firmware](https://micropython.org/download#esp8266)

Manual: https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

To flash you should install esptool:

```sh
pip install esptool
```

Now you can flash firmware
```sh
# clear flash
esptool.py --port /dev/ttyUSB0 erase_flash
# deploy downloaded firmware
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20191220-v1.12.bin
```

If everything is ok, please edit boot.py file and provide valid data:
```python
# Your flespi token
token = "YourFlespiTokenHere"
topic = "myesp/light"

# Wi-Fi settings
wifissid = "test"
wifipassword = "12345678"
```

Now you can load the example to your board:

```sh
ampy --port /dev/ttyUSB0 put boot.py
ampy --port /dev/ttyUSB0 put mqtt.py
ampy --port /dev/ttyUSB0 put wifi.py
```

Then just unplug then plug power cable from your board. And check result for example in your favorite UI MQTT client (we love to use [MQTT-Board](https://mqttboard.flespi.io))

## lua

Example source code is located at [./lua/](./lua/)

To run the example you need to install the dependencies ([luamqtt](https://github.com/xHasKx/luamqtt) package):

```sh
# optionally create local environment using hererocks (https://github.com/mpeterv/hererocks):
hererocks venv -l5.3 -rlatest
. venv/bin/activate

# install requirements
luarocks install luasocket
luarocks install luasec
luarocks install luamqtt
```

And then run the example script with the **flespi token** passed through the process environment:

```sh
# optionally use created local environment
. venv/bin/activate

# run example
FlespiToken=XXXXXXXXXXXXXXX lua ./example.lua
```

## browser

Example source code is located at [./browser/](./browser/)

You may run the example [in your browser from GitHub Pages](https://flespi-software.github.io/examples/mqtt-client/browser/example.html) or open the example.html file from your local file system.

This example uses the [browser-version of the mqtt.js](https://github.com/mqttjs/MQTT.js#browser) library.
