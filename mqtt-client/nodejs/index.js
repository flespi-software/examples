const mqtt = require('mqtt');

const client = mqtt.connect('mqtts://mqtt.flespi.io:8883', {
  // see https://flespi.com/kb/tokens-access-keys-to-flespi-platform to read about flespi tokens
  username: `FlespiToken ${process.env.FlespiToken}`,
  protocolVersion: 5,
  clean: true,
});
console.log('mqtt client created, connecting...');

client.on('connect', () => {
  console.log('connected, subscribing to "test" topic...');

  client.subscribe('test', (err) => {
    if (err) {
      console.log('failed to subscribe to topic "test":', err);
      return;
    }
    console.log('subscribed to "test" topic, publishing message...');
    client.publish('test', 'hello from flespi nodejs mqtt client example script!', {qos: 1});
  });
});

client.on('message', (topic, msg) => {
  console.log(`received message in topic "${topic}": "${msg.toString('utf8')}"`);
  console.log('disconnecting...');
  client.end();
});

client.on('close', () => {
  console.log('disconnected');
})

client.on('error', (err) => {
  console.log('mqtt client error:', err);
});
