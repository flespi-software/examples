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
received message in topic "test": "hello from flespi nodejs mqtt client example script!"
disconnecting...
disconnected
```

## Requirements

To connect to [flespi mqtt broker](https://flespi.com/mqtt-broker) you have to obtain a **flespi token**.

Please [refer here](https://flespi.com/kb/tokens-access-keys-to-flespi-platform) to read how to do it (don't worry, it's fast and simple).

## nodejs

Example source code located in the [./nodejs/](./nodejs/)

To run the node.js example you need to install the dependencies (mqtt package):

```sh
npm install
```

And then run the entry point script with the **flespi token** passed through the process environment:

```sh
FlespiToken=XXXXXXXXXXXXXXX npm run main # runs node ./index.js
```
