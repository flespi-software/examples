<?php
  $mysql_host = 'localhost';
  $mysql_user = 'root';
  $mysql_password = 'password';
  $mysql_db = 'message_receiver';
  $mysql_table = 'php_message_listener';

  // First of all you should create a new table in your database to handle messages.
  // You can change columns as you wish. But then you should change the respective insert query in "on_message" function.
  //
  // CREATE TABLE message_receiver.php_message_listener (
  // 	ident varchar(100) NOT NULL,
  // 	`server.timestamp` DOUBLE NOT NULL,
  // 	`position.longitude` DOUBLE NULL,
  // 	`position.latitude` DOUBLE NULL,
  // 	`timestamp` DOUBLE NULL,
  // 	`position.altitude` DOUBLE NULL,
  // 	`position.direction` DOUBLE NULL,
  // 	`position.speed` DOUBLE NULL,
  // 	`position.satellites` INT NULL,
  // 	CONSTRAINT php_message_listener_PK PRIMARY KEY (ident,`server.timestamp`,`timestamp`)
  // )
  // ENGINE=MyISAM
  // DEFAULT CHARSET=utf8
  // COLLATE=utf8_general_ci;


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
  if ($json_string) {
    // decode received json string
    $json = json_decode($json_string, true);
  } else {
    // skip empty message
    http_response_code(200);
    exit(1);
  }

  // more details about available message content:
  // https://flespi.com/kb/messages-basic-information-units

  // Connect to mysql database
  $con = mysqli_connect($mysql_host, $mysql_user, $mysql_password, $mysql_db);

  if ($con === false) {
    // Could not connect
    http_response_code(500);
  } else {
    $itms = [];
    // Prepare messages
    for ($i=0; $i < count($json); $i++) {
      $itms[] = '(
        "' . mysqli_real_escape_string($con, $json[$i]['ident'] ?? '') . '",
        ' . floatval($json[$i]['server.timestamp'] ?? 0) . ',
        ' . floatval($json[$i]['position.longitude'] ?? 0) . ',
        ' . floatval($json[$i]['position.latitude'] ?? 0) . ',
        ' . floatval($json[$i]['timestamp'] ?? 0) . ',
        ' . floatval($json[$i]['position.altitude'] ?? 0) . ',
        ' . floatval($json[$i]['position.direction'] ?? 0) . ',
        ' . floatval($json[$i]['position.speed'] ?? 0) . ',
        ' . intval($json[$i]['position.satellites'] ?? 0) . '
      )';
    }

    $query = '
    INSERT INTO ' . $mysql_table . ' (
      `ident`,
      `server.timestamp`,
      `position.longitude`,
      `position.latitude`,
      `timestamp`,
      `position.altitude`,
      `position.direction`,
      `position.speed`,
      `position.satellites`
    ) VALUES ' . join(',', $itms);

    // insert message to database
    if (mysqli_query($con, $query)) {
      // NOTE: it's important to send HTTP 200 OK status
      // to acknowledge successful messages delivering
      http_response_code(200);
    } else {
      http_response_code(500);
    }
  }
  mysqli_close($con);
?>
