const fs = require('fs');
const express = require('express');

// create a HTTP server application
const app = express();

// configure json parsing middleware
app.use(express.json({
  limit: '10mb',
  strict: true,
}));

// HTTP requests handler function
app.post('/post', (req, res) => {
  // now req.body will be a parsed object containing messages array like this:
  /* [ { 'channel.id': 94,
    ident: '1234',
    peer: '127.0.0.1:53862',
    'protocol.id': 19,
    'server.timestamp': 1554447820.251666,
    timestamp: 1554447820.251666 } ] */

  // more details about available message content:
  // https://flespi.com/kb/messages-basic-information-units

  // in this example we are just storing it in a file
  // please note that it will be overwritten on each new request
  fs.writeFileSync('messages.json', JSON.stringify(req.body));

  // NOTE: it's important to send HTTP 200 OK status
  // to acknowledge successful messages delivering
  res.end();
});

// start listening on port 7777
app.listen(7777);
