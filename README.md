# flespi.io usage examples

## HTTP stream receiver

* [NodeJS](http-stream-receiver/nodejs)
* [PHP](http-stream-receiver/php) or [PHP+MySQL](http-stream-receiver/php_mysql)
* [Python](http-stream-receiver/python)

More info about http streams: https://flespi.com/blog/get-data-in-your-platform-via-flespi-http-stream

In short:

1. create a **stream** in flespi platform, using `http` as **configuration** and something like `http://your-server:port/path-on-server` as **uri** parameter
2. subscribe created **stream** to items you need
3. deploy one of examples listed above on your server or VPS
4. configure your example to listen on `your-server:port` network endpoint and to handle a `/path-on-server` uri
5. flespi platform will constantly deliver a batch of messages to your deployment

## MQTT client examples

[MQTT client source code examples](mqtt-client/) using the [flespi broker](https://flespi.com/mqtt-broker) on [**nodejs**](./mqtt-client/nodejs), [**python**](./mqtt-client/python), [**python on windows**](./mqtt-client/python-windows), [**lua**](./mqtt-client/lua), [**browser**](./mqtt-client/browser), [**micropython (esp8266)**](./mqtt-client/micropython), etc...

## MQTT channel message handler

* [Python + MySQL](mqtt-message-handler/python)

## Snapshots downloader tool

* [Python](snapshots-downloader)

## Devices creation tool

This tool may help you to create many [devices](https://flespi.com/kb/device-virtual-instance-of-real-tracker) in your [flespi.io](https://flespi.io/) account.

* [run it in your browser](https://flespi-software.github.io/examples/devices-creation-tool/)
* [sources](https://github.com/flespi-software/examples/tree/master/devices-creation-tool)

# Contributing

If you have cool examples of flespi API usage or have time and zeal to write examples on your preferred language, you are welcome to contribute by making a pull request.
