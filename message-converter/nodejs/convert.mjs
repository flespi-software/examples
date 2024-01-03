import fetch from 'node-fetch';

// Read command line arguments
const [, , token, device_id, from, to, format] = process.argv;

// Validate input arguments
if (!device_id || !from || !to || !token) {
  console.error('Usage: node convert.js <token> <device_id> <from> <to> {JSON,KML,GPX,GEOJSON,CSV}');
  process.exit(1);
}

const params = {
  fields: 'timestamp,position.timestamp,position.altitude,position.latitude,position.longitude',
  filter: 'timestamp,position.latitude,position.longitude',
  from: parseInt(from),
  to: parseInt(to)
}
// Construct the URL with dynamic values
const apiUrl = `https://flespi.io/gw/devices/${device_id}/messages?data=${encodeURIComponent(JSON.stringify(params))}`;

// Set the Authorization header with the token
const headers = {
  'Authorization': `FlespiToken ${token}`
};

// Make a GET request with the Authorization header
fetch(apiUrl, { method: 'GET', headers })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    processResponse(data.result)
  })
  .catch(error => {
    console.error('Error:', error.message);
  });

function processResponse(data) {
  let result = ''
  switch (String(format).toLowerCase()) {
    case 'kml': result = convertKML(data); break;
    case 'csv': result = convertCSV(data); break;
    case 'geojson': result = convertGeoJSON(data); break;
    case 'gpx': result = convertGPX(data); break;
    default: result = JSON.stringify(data);
  }
  console.log(result)
}

function formatUnixUTCTZ(timestamp) {
  return new Date(timestamp * 1000).toISOString()
}
function convertKML(data) {
  let coordstring = data.map(obj => obj['position.longitude'] + ',' + obj['position.latitude'] + ',0.0').join(' ')

  let kml = `<?xml version="1.0" encoding="UTF-8"?> <kml xmlns="http://earth.google.com/kml/2.0"> <Document><Placemark>  <name>${'#' + device_id}</name>
<TimeSpan>
<begin>${formatUnixUTCTZ(from)}</begin>
<end>${formatUnixUTCTZ(to)}</end>
</TimeSpan><LineString><coordinates>${coordstring}</coordinates></LineString></Placemark></Document></kml>`
  return kml
}
function convertCSV(data) {
  let csv = 'longitude,latitude,time\n' + data.map(obj => obj['position.longitude'] + ',' + obj['position.latitude'] + ',' + formatUnixUTCTZ(obj['position.timestamp'] || obj['timestamp'])).join('\n')
  return csv;
}
function convertGeoJSON(data) {
  let coordinates = data.map(obj => [obj['position.longitude'], obj['position.latitude']])

  let geojson = {
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
  return JSON.stringify(geojson)
}
function convertGPX(data) {
  let coordstring = data.map(obj => `<trkpt lat="${obj['position.latitude']}" lon="${obj['position.longitude']}">
    <time>${formatUnixUTCTZ(obj['position.timestamp'] || obj['timestamp'])}</time>
    <ele>${obj['position.altitude']}</ele>
  </trkpt>`).join('\n')
  let gpx = `<?xml version="1.0" encoding="UTF-8"?>
<gpx
xmlns="http://www.topografix.com/GPX/1/1"
version="1.1"
creator="flespi"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
<time>${formatUnixUTCTZ(new Date() / 1000)}</time>
<metadata>
<name>${'#' + device_id}</name>
<author>
 <name>flespi</name>
</author>
</metadata>
<trk>
<name>track</name>
<trkseg>
  ${coordstring}
</trkseg>
</trk>
</gpx>`
  return gpx
}
