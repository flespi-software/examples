import requests
import time

token = "INSERT_YOUR_TOKEN_HERE"
device_id = 0 # INSERT YOUR DEVICE ID HERE
ts_from = 0 # begin timestamp. First available message will be used if 0
ts_to = int(time.time()) # end timestamp. The time of script start will be used if timestamp is not specified
delay = 0.01 # second delay between requests to re-POST messages

# uri will be the same to get messages and to post messages
uri = 'https://flespi.io/gw/devices/' + str(device_id) + '/messages'

# get messages within specified time range
response = requests.get(uri, headers = {'Authorization' : 'FlespiToken ' + token}, json={"from": ts_from, "to": ts_to})
messages = response.json()['result']

messages_size = len(messages)
print("fetched ", messages_size, " messages")

# iterate over messages and re-post it with delay
for i in range(messages_size):
    requests.post(uri, headers = auth_header, json=[messages[i]])
    time.sleep(delay)
    print("\rExecuted " + str(round(100 * (i + 1) / messages_size, 2)) + "%", end="")
print("\n")