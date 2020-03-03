def sub_cb(topic, msg):
    print((topic, msg))

def send(topic="test", data="hello world!", client_id='testmicropython', server='mqtt.flespi.io', port=1883, user='', password=''):
    from umqtt.simple import MQTTClient
    import time

    print(data)

    client=MQTTClient(client_id, server, port, user, password) # Create MQTT client
    client.set_callback(sub_cb) # on message callback
    client.connect() # connect to MQTT broker
    client.subscribe(topic) # subscribe topic
    client.publish(topic, str(data)) # publish data to topic
    client.wait_msg() # waiting for a message
    time.sleep(2)
    client.disconnect() # disconnect
