import 'package:mqtt5_client/mqtt5_client.dart';
import 'package:mqtt5_client/mqtt5_server_client.dart';
import 'dart:async';
import 'dart:io';
import 'package:typed_data/typed_data.dart';

void main() async {
  // Retrieve Flespi token from environment variable
  final flespiToken = Platform.environment['FlespiToken'];
  if (flespiToken == null || flespiToken.isEmpty) {
    print('Flespi token is not set in the environment variables.');
    return;
  }

  // Create an MQTT client instance
  print('mqtt client created, connecting...');
  final client = MqttServerClient.withPort('wss://mqtt.flespi.io', '', 443);

  // Configure the client for WebSocket
  client.useWebSocket = true;
  client.websocketProtocolString = ['mqtt'];

  // Set the client identifier
  client.clientIdentifier = 'dart_mqtt_client';

  // Set the username with the Flespi token (no password in this example)
  final connMessage = MqttConnectMessage()
      .withClientIdentifier('dart_mqtt_client')
      .authenticateAs(flespiToken, '');

  client.connectionMessage = connMessage;

  // Connect to the MQTT broker
  try {
    await client.connect();
  } on Exception catch (e) {
    print('Connection failed: $e');
    client.disconnect();
    return;
  }

  // Check if we are connected
  if (client.connectionStatus?.state == MqttConnectionState.connected) {
    print('connected, subscribing to "test" topic...');
  } else {
    print('Connection failed: ${client.connectionStatus}');
    return;
  }

  // Subscribe to the "test" topic
  const topic = 'test';
  client.subscribe(topic, MqttQos.atMostOnce);
  print('subscribed to "test" topic, publishing message...');

  // Handle incoming messages
  client.updates?.listen((List<MqttReceivedMessage<MqttMessage>> c) {
    final MqttPublishMessage message = c[0].payload as MqttPublishMessage;
    final Uint8Buffer? payloadBuffer = message.payload.message;

    if (payloadBuffer != null) {
      final payload = String.fromCharCodes(payloadBuffer);
      print('received message in topic "test": "$payload"');
    } else {
      print('Received null payload from topic: "${c[0].topic}"');
    }
  });

  // Publish a message to the "test" topic
  final builder = MqttPayloadBuilder();
  builder.addString('hello from flespi mqtt client example script!');
  client.publishMessage(topic, MqttQos.atMostOnce, builder.payload!);

  // Keep the connection alive
  await Future.delayed(Duration(seconds: 5));  // Give some time to receive the message

  print('disconnecting...');
  client.disconnect();
  print('disconnected');
}
