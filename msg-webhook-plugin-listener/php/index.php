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

  // convert json string to php array
  $json = json_decode($json_string, true);
  foreach ($json as $key => $el) {
    // add squirrel parameter to each message ;)
    $obj = [
      "squirrel" => "🐿️"
    ];
    if ($el['timestamp']) {
      // convert timestamp parameter to date/time string
      $obj['datetime'] = gmdate("M d Y H:i:s", $el['timestamp']);
    }
    // replace obj in array
    $json[$key] = $obj;
  }
  // response to request
  echo json_encode($json);

  // NOTE: it's important to send HTTP 200 OK status
  // to acknowledge successful messages delivering
  http_response_code(200);
?>
