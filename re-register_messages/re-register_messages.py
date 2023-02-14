import requests
import time

token = "INSERT_YOUR_TOKEN_HERE"
device_id = 0 # INSERT YOUR DEVICE ID HERE
ts_from = 0 # begin timestamp. First available message will be used if 0
ts_to = int(time.time()) # end timestamp. The time of script start will be used if timestamp is not specified
delay = 0.1 # seconds delay between requests to re-POST messages
batch_size = 100

# uri will be the same to get messages and to post messages
uri = 'https://flespi.io/gw/devices/' + str(device_id) + '/messages'
auth_header = {'Authorization' : 'FlespiToken ' + token}

# get messages within specified time range
response = requests.get(uri, headers = auth_header, json={"from": ts_from, "to": ts_to})
messages = response.json()['result']

messages_size = len(messages)
print("fetched ", messages_size, " messages")

i = 0
for i in range(0, messages_size - batch_size, batch_size):
    requests.post(uri, headers = auth_header, json=messages[i: i + batch_size])
    if delay > 0:
        time.sleep(delay)
    print("\rExecuted " + str(round(100 * (i + batch_size) / messages_size, 2)) + "%", end="")
requests.post(uri, headers = auth_header, json=messages[i + batch_size:])
print("done!")