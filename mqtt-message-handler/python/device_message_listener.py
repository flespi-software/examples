device_id = '12345' # you can use + to subscrube to all devices or list device IDs separated by commas (123,124,135)
flespi_mqtt_host = 'mqtt.flespi.io'
flespi_token = 'YOUR FLESPI TOKEN'
mysql_host = 'localhost'
mysql_user = 'root'
mysql_passwd = 'password'
mysql_db = 'message_receiver'

# First of all you should create a new table in your database to handle messages.
# You can change columns as you wish. But then you should change the respective insert query in "on_message" function.
#
# CREATE TABLE message_receiver.python_message_listener (
# 	ident varchar(100) NOT NULL,
# 	`server.timestamp` DOUBLE NOT NULL,
# 	`position.longitude` DOUBLE NULL,
# 	`position.latitude` DOUBLE NULL,
# 	`timestamp` DOUBLE NULL,
# 	`position.altitude` DOUBLE NULL,
# 	`position.direction` DOUBLE NULL,
# 	`position.speed` DOUBLE NULL,
# 	`position.satellites` INT NULL,
# 	CONSTRAINT python_message_listener_PK PRIMARY KEY (ident,`server.timestamp`,`timestamp`)
# )
# ENGINE=MyISAM
# DEFAULT CHARSET=utf8
# COLLATE=utf8_general_ci;


import asyncio
import os
import signal
import time
import json
import pymysql
import uvloop
from gmqtt import Client as MQTTClient



asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
STOP = asyncio.Event()
con = None
counter = 0

def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('flespi/message/gw/devcies/' + device_id, qos=0)


def on_message(client, topic, payload, qos, properties):
    global counter, con
    data = json.loads(payload)
    if con is not None:
        cursor = con.cursor()
        cursor.execute(
            """
                INSERT INTO python_message_listener (
                    `ident`,
                    `server.timestamp`,
                    `position.longitude`,
                    `position.latitude`,
                    `timestamp`,
                    `position.altitude`,
                    `position.direction`,
                    `position.speed`,
                    `position.satellites`
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                data["ident"],
                data["server.timestamp"],
                data["position.longitude"],
                data["position.latitude"],
                data["timestamp"],
                data["position.altitude"],
                data["position.direction"],
                data["position.speed"],
                data["position.satellites"]
            )
            )
        counter+=1
        con.commit()
    else:
        print('Not inserted', json.dumps(data, indent=4))


def on_disconnect(client, packet, exc=None):
    print('Disconnected')
    if con is not None:
        con.close()

def on_subscribe(client, mid, qos, properties):
    print('SUBSCRIBED')

def ask_exit(*args):
    print('Inserted:', counter)
    STOP.set()

async def main(broker_host, token):
    global con
    con = pymysql.connect(host = mysql_host, user = mysql_user, passwd = mysql_passwd, db = mysql_db, autocommit=True)
    client = MQTTClient('message_listener')

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    client.set_auth_credentials(token, None)
    await client.connect(broker_host)

    await STOP.wait()
    await client.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main(flespi_mqtt_host, flespi_token))
