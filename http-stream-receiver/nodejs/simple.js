const fs = require('fs');
const http = require('http');

// HTTP requests handler function
const requestHandler = (request, response) => {
  try {
    // checking right method and url
    if (request.method === 'POST' && request.url === '/post') {
      // collecting body
      let body = [];
      request
        .on('data', (chunk) => { body.push(chunk); })
        .on('end', () => {
          body = Buffer.concat(body).toString();
          // now body will be something like this:
          // [{"channel.id":94,"ident":"1234","peer":"127.0.0.1:36260","protocol.id":19,"server.timestamp":1554445625.950464,"timestamp":1554445625.950464}]

          // you may use JSON.parse(body) to parse json

          // but in this example we are just storing it in a file
          // please note that it will be overwritten on each new request
          fs.writeFileSync('messages.json', body);

          // NOTE: it's important to send HTTP 200 OK status
          // to acknowledge successful messages delivering
          response.end();
        });
    } else {
      // all other method's/url's are not allowed
      // the HTTP response code should not be 200 to preserve undelivered messages in the flespi stream buffer
      response.writeHead(400, 'Bad Request', {'Content-Type': 'text/plain'});
      response.end('Please configure flespi.io http stream to /post url of this server');
    }
  } catch (err) {
    console.log('unhandled exception:', err);
    // the HTTP response code should not be 200 to preserve undelivered messages in the flespi stream buffer
    response.writeHead(500, 'Internal Server Error');
    response.end();
  }
}

// create a HTTP server
const server = http.createServer(requestHandler);

// and start listening on port 7777
server.listen(7777, (err) => {
  if (err) {
    return console.log('failed to listen on port 7777:', err);
  }
});
