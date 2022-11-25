## HTTP stream receiver

* [NodeJS](nodejs)
* [PHP](php) or [PHP+MySQL](hphp_mysql)
* [Python](python)

More info about http streams:
  https://flespi.com/blog/get-data-in-your-platform-via-flespi-http-stream
  https://flespi.com/blog/streams-now-pushing-as-well-as-pulling

In short:

1. create a **stream** in flespi platform, using `http` as **configuration** and something like `http://your-server:port/path-on-server` as **uri** parameter
2. subscribe created **stream** to items you need
3. deploy one of examples listed above on your server or VPS
4. configure your example to listen on `your-server:port` network endpoint and to handle a `/path-on-server` uri
5. flespi platform will be constantly delivering batches of messages to your deployment
