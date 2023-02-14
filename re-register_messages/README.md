# Python code example to re-post existing messages to device

Note, when the message is re-registered, server.timestamp is not present in the message, and the paramter rest.timestamp added. This may lead to some UI features not working. E.g. not possible to switch from message to traffic in logs & messages tab.

To run the script you need:

* insert valid TOKEN
* enter the device ID
* enter timestamps of left and right borders to ts_from and ts_to variables. If not modified all messages will be re-registered
