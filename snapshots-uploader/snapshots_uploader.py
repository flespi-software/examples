import json
import requests
import gzip

filename = '1674415503.gz' # snapshot filename

token = 'YOUR_FLESPI_TOKEN_HERE'
id = 0 # set your device id

# if from_timestamp and to_timestamp are zero - republish all messages from the snapshot
from_timestamp = 0
to_timestamp = 0

count = 100 # messages in chunk


def post_messages():
    print("\n=======\n")
    print(cntr)
    print("\n")
    messages = requests.post(
        'https://flespi.io/gw/devices/' + str(id) + '/messages',
        data=json.dumps(arr),
        headers={'Authorization': 'FlespiToken ' + token},
        stream=True
        )
    if messages.status_code == 200:
        print('Done')
    else:
        print(json.dumps(arr))
        print('Uploading error!')
with gzip.open(filename, 'rb') as f:
    data = json.load(f)
    cntr = 0
    arr = []
    for i in data:
        if cntr == count:
            post_messages() # post messages chunk
            cntr = 0
        if cntr == 0:
            arr = []
        if (i['params']['timestamp'] <= to_timestamp and i['params']['timestamp'] >= from_timestamp) or (from_timestamp == 0 and to_timestamp == 0):
            arr.append(i['params'])
            cntr+=1
    if cntr > 0:
        post_messages() # post messages chunk
