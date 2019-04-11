<?php
  // Receive HTTP POST request body
  $json_string = file_get_contents('php://input');

  /* now $json_string should contain JSON array like this:
  [
    {
      'channel.id': 94,
      'ident': '1234',
      'peer': '127.0.0.1:53862',
      'protocol.id': 19,
      'server.timestamp': 1554447820.251666,
      'timestamp': 1554447820.251666
    }
  ]
  */

  // more details about available message content:
  // https://flespi.com/kb/messages-basic-information-units

  // just store it in a file
  // please note that it will be overwritten on each new request
  $file_handle = fopen('messages.json', 'w');
  fwrite($file_handle, $json_string); // Write received messages to file
  fclose($file_handle);

  // NOTE: it's important to send HTTP 200 OK status
  // to acknowledge successful messages delivering
  http_response_code(200);
?>
