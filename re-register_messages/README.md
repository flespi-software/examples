# Python code example to re-register existing messages to device

Why do you need to do that? Couple use-cases:
* apply plugin value to historical messages
* send some batch of messages via stream

Note, when the [message](https://flespi.com/kb/messages-basic-information-units) is re-registered, server.timestamp is not present in the message, and the paramter rest.timestamp added.

To run the script you need:

* insert valid TOKEN
* enter the device ID
* enter timestamps of left and right borders to ts_from and ts_to variables. If not modified all messages will be re-registered
* (optional) modify messages batch size
* (optional) modify delay