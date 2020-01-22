import requests
import shutil

token = 'YOUR_FLESPI_TOKEN_HERE'

itemtype = 'gw/devices'
# itemtype = 'storage/containers' # To download containers snapshots uncomment this line

ids = 'all' # You can list ids with a comma like '1,2,3,4' or 'all' for all items

print('Get available snapshots.')
snapshots = requests.get('https://flespi.io/' + itemtype + '/' + str(ids) + '/snapshots', headers={'Authorization': 'FlespiToken ' + token})
if snapshots.status_code == 200:
    snapshots_list = snapshots.json()
    print('Downloading')
    for device_snapshots in snapshots_list['result']:
        length = len(device_snapshots['snapshots'])
        if length > 0:
            print(str(device_snapshots['id']) + '-' + str(device_snapshots['snapshots'][length - 1]) + '.gz')
            snapshot = requests.get(
                'https://flespi.io/' + itemtype + '/' + str(device_snapshots['id']) + '/snapshots/' + str(device_snapshots['snapshots'][length - 1]) + '.gz',
                headers={'Authorization': 'FlespiToken ' + token},
                stream=True
                )
            if snapshot.status_code == 200:
                with open(str(device_snapshots['id']) + '-' + str(device_snapshots['snapshots'][length - 1]) + '.gz', 'wb') as f:
                    snapshot.raw.decode_content = True
                    shutil.copyfileobj(snapshot.raw, f)
                print('Done')
            else: print('Downloading error!')
        else: print('No snapshots available for ' + str(device_snapshots['id']))
else: print('Error: Wrong request!')
