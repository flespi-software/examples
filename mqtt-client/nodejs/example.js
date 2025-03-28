const mqtt = require('mqtt');
const test_topic = 'test'
const randomstring = (Math.random() + 1).toString(36).substring(6)
const client = mqtt.connect('mqtts://mqtt.flespi.io:8883', {
  // The random string is needed when you try to run 2 clients in parallel,
  // because each client must have a UNIQUE client_id
  clientId: 'flespi-examples-mqtt-client-nodejs_' + randomstring,
  // see https://flespi.com/kb/tokens-access-keys-to-flespi-platform to read about flespi tokens
  username: `FlespiToken ${process.env.FlespiToken}`,
  protocolVersion: 5,
  clean: false,
  properties: {
    sessionExpiryInterval: 60 // this setting is required when clean:false
  }
});
console.log('mqtt client created, connecting...');

client.on('connect', () => {
  console.log('connected, subscribing to "test" topic...');

  client.subscribe(test_topic, {qos: 1}, (err) => {
    if (err) {
      console.log('failed to subscribe to topic "test":', err);
      return;
    }
    console.log('subscribed to "test" topic, publishing message...');
    client.publish(test_topic, 'hello from flespi mqtt client example script!', {qos: 1});
  });
});

client.on('message', (topic, msg, packet) => {
  console.log(`received ${packet.retain ? 'retained' : 'realtime'} message in topic "${topic}": "${msg.toString('utf8')}"`);
  console.log('disconnecting...');
  if (!packet.retain) {
    client.end();
  }
});

client.on('close', () => {
  console.log('disconnected');
})

client.on('error', (err) => {
  console.log('mqtt client error:', err);
  client.end(true) // force disconnect and stop the script
});
