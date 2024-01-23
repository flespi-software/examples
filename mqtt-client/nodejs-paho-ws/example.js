import Paho from "paho-mqtt";

// for nodejs
import WebSocket from 'ws';
global.WebSocket = WebSocket

const uri = "mqtt.flespi.io";
const username = `FlespiToken ${process.env.FlespiToken}`;
const clientId = `mqtt-async-test-${parseInt(Math.random() * 100)}`;
const client = new Paho.Client(uri, 443, clientId);
function onConnect() {
  console.log("Success");
  client.subscribe("test/test");
}

function onFailure(error) {
  console.log("Failed", error);
}

function onMessageArrived(message) {
  console.log("Message: " + message.payloadString);
}

client.onMessageArrived = onMessageArrived;

client.connect({
  userName: username,
  useSSL: true,
  onSuccess: onConnect,
  onFailure: onFailure,
});
