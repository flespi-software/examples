<?php
  $json_string = file_get_contents('php://input'); // Receive POST payload
  $file_handle = fopen('lastmessage.json', 'w');
  fwrite($file_handle, $json_string); // Write received messages to file
  fclose($file_handle);
  echo $json_string;
?>
