import os
import asyncio
import signal
import uvloop

from gmqtt import Client as MQTTClient


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
STOP = asyncio.Event()


def on_connect(client, flags, rc, properties):
    print('connected, subscribing to "test" topic...')
    client.subscribe('test', qos=1)

def ask_exit(*args):
    STOP.set()

def on_message(client, topic, payload, qos, properties):
    print('received message in topic "{}": "{}"'.format(topic, payload.decode('utf8')))
    print('disconnecting...')
    ask_exit()

def on_disconnect(client, packet, exc=None):
    print('disconnected')

def on_subscribe(client, mid, qos, properties):
    print('subscribed to "test" topic, publishing message...')
    client.publish('test', 'hello from flespi mqtt client example script!')

async def main():
    client = MQTTClient('flespi-examples-mqtt-client-python', clean_session=True)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    client.set_auth_credentials('FlespiToken {}'.format(os.environ.get("FlespiToken")), None)
    print('mqtt client created, connecting...')
    await client.connect('mqtt.flespi.io', port=8883, ssl=True)
    await STOP.wait()
    await client.disconnect()
    print('disconnected')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main())
