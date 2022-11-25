## Message Webhook plugin listeners

* [NodeJS](nodejs)

More info about msg-webhook plugin:
  https://forum.flespi.com/d/875-changelog-msg-webhook-plugin

In short:

1. create a **plugin** in flespi platform, using `msg-webhook` as **configuration** and something like `http://your-server:port/post` as **uri** parameter
2. assign created **plugin** to device you need
3. deploy one of examples listed above on your server or VPS
4. configure your example to listen on `your-server:port` network endpoint and to handle a `/post` uri
5. flespi platform will be constantly delivering batches of messages to your deployment
