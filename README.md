# flespi.io usage examples

## http stream receiver

* [NodeJS](http-stream-receiver/nodejs)
* [PHP](http-stream-receiver/php)
* [Python](http-stream-receiver/python)

More info about http streams: https://flespi.com/kb/stream-forward-data-from-gateway

In short:

1. create a **stream** in flespi platform, using `http` as **configuration** and something like `http://your-server:port/path-on-server` as **uri** parameter
2. subscribe created **stream** to items you need
3. deploy one of examples listed above on your server or VPS
4. configure your example to listen on `your-server:port` network endpoint and to handle a `/path-on-server` uri
5. flespi platform will constantly deliver a batch of messages to your deployment

# Contributing

If you have cool examples of flespi API usage or have time and zeal to write examples on your preferred language, you are welcome to contribute by making a pull request.
