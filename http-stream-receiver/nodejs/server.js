var http = require('http');
var fs = require('fs');

function processMessages(request, response, callback) {
	var data = '';
	if (typeof callback !== 'function') return null;

	if (request.method == 'POST') {
		request.on('data', function(data) {
			data += data;
			if (data.length > 1024*1024*3) { // 3mb limit
				data = '';
				response.writeHead(413, {'Content-Type': 'text/plain'}).end();
				request.connection.destroy();
			}
		});

		request.on('end', function() {
			request.post = data;
			callback();
		});

	} else {
		response.writeHead(405, {'Content-Type': 'text/plain'});
		response.end();
	}
}
http.createServer(function(request, response) {
	const { headers, method, url } = request;
  console.log(headers, method, url)
  // Process only POST method and /post url
	if (request.method == 'POST' && url == '/post') {
		processMessages(request, response, function() {
			// Write received messages to file
			fs.writeFile('lastmessage.json', request.post, function(err, data) {
				if (err) console.log(err);
				console.log('Successfully saved');
			});
			console.log(request.post);
			response.writeHead(200, 'OK', {'Content-Type': 'text/plain'});
			response.end();
		});
	} else {
		response.writeHead(200, 'OK', {'Content-Type': 'text/plain'});
		response.end();
	}
}).listen(7777); // Listen stream on 7777 port
