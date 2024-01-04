import requests
import json
import sys
import time
from datetime import datetime

def main():
    # Read command line arguments
    _, token, device_id, from_timestamp, to_timestamp, format_type = sys.argv

    # Validate input arguments
    if not all([device_id, from_timestamp, to_timestamp, token, format_type]):
        print('Usage: python convert.py <token> <device_id> <from> <to> {JSON,KML,GPX,GEOJSON,CSV}')
        sys.exit(1)

    # Construct the URL with dynamic values
    api_url = f"https://flespi.io/gw/devices/{device_id}/messages?data={json.dumps({'fields': 'timestamp,position.altitude,position.latitude,position.longitude', 'filter': 'timestamp,position.latitude,position.longitude', 'from': int(from_timestamp), 'to': int(to_timestamp)})}"

    # Set the Authorization header with the token
    headers = {
        'Authorization': f'FlespiToken {token}'
    }

    # Make a GET request with the Authorization header
    response = requests.get(api_url, headers=headers)

    if not response.ok:
        print(f'HTTP error! Status: {response.status_code}')
        sys.exit(1)

    data = response.json()
    process_response(data['result'], format_type.lower(), device_id, from_timestamp, to_timestamp)

def process_response(data, format_type, device_id, from_timestamp, to_timestamp):
    if format_type == 'kml':
        result = convert_kml(data, device_id, from_timestamp, to_timestamp)
    elif format_type == 'csv':
        result = convert_csv(data, device_id, from_timestamp, to_timestamp)
    elif format_type == 'geojson':
        result = convert_geojson(data, device_id, from_timestamp, to_timestamp)
    elif format_type == 'gpx':
        result = convert_gpx(data, device_id, from_timestamp, to_timestamp)
    else:
        result = json.dumps(data)

    print(result)

def format_unix_utc(timestamp):
    return datetime.utcfromtimestamp(timestamp).isoformat() + 'Z'

def convert_kml(data, device_id, from_timestamp, to_timestamp):
    coordinates = ' '.join([f"{obj['position.longitude']},{obj['position.latitude']},0.0" for obj in data])
    kml = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.0">
<Document>
<Placemark>
  <name>#{device_id}</name>
  <TimeSpan>
    <begin>{format_unix_utc(int(from_timestamp))}</begin>
    <end>{format_unix_utc(int(to_timestamp))}</end>
  </TimeSpan>
  <LineString>
    <coordinates>{coordinates}</coordinates>
  </LineString>
</Placemark>
</Document>
</kml>'''
    return kml

def convert_csv(data, device_id, from_timestamp, to_timestamp):
    csv = 'longitude,latitude,time\n' + '\n'.join([f"{obj['position.longitude']},{obj['position.latitude']},{format_unix_utc(obj['timestamp'])}" for obj in data])
    return csv

def convert_geojson(data, device_id, from_timestamp, to_timestamp):
    coordinates = [[obj['position.longitude'], obj['position.latitude']] for obj in data]
    geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'properties': {
                    'stroke': '#ff0000',
                    'stroke-width': 2,
                    'stroke-opacity': 1
                },
                'geometry': {
                    'type': 'LineString',
                    'coordinates': coordinates
                }
            }
        ]
    }
    return json.dumps(geojson)

def convert_gpx(data, device_id, from_timestamp, to_timestamp):
    msgs = '\n'.join([f"<trkpt lat=\"{obj['position.latitude']}\" lon=\"{obj['position.longitude']}\"><time>{format_unix_utc(obj['timestamp'])}</time><ele>{obj['position.altitude']}</ele></trkpt>" for obj in data])
    gpx = f'''<?xml version="1.0" encoding="UTF-8"?>
<gpx
xmlns="http://www.topografix.com/GPX/1/1"
version="1.1"
creator="flespi"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
<time>{format_unix_utc(int(time.time()))}</time>
<metadata>
  <name>#{device_id}</name>
  <author>
    <name>flespi</name>
  </author>
</metadata>
<trk>
  <name>track</name>
  <trkseg>
    {msgs}
  </trkseg>
</trk>
</gpx>'''
    return gpx

if __name__ == "__main__":
    main()
