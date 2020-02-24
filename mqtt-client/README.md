# MQTT Client examples

All provided examples are performing the simple but complete MQTT client workflow:

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
That may be a **Standard** token, **Master** token (although using it in the example may be unwise) or the [**ACL** token](https://flespi.com/blog/take-control-of-token-access-permissions-with-flexible-acls).

## nodejs

Example source code located in the [./nodejs/](./nodejs/)

To run the example you need to install the dependencies ([mqtt](https://github.com/mqttjs/MQTT.js) package):

```sh
npm install
```

And then run the example script with the **flespi token** passed through the process environment:

```sh
FlespiToken=XXXXXXXXXXXXXXX npm run example # just runs 'node ./example.js'
```

## python

Example source code located in the [./python/](./python/)

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

## lua

Example source code located in the [./lua/](./lua/)

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
