const axios = require('axios');

// URL for GET request
const getUrl = 'https://flespi.io/platform/deleted/all/logs?data=%7B%22count%22%3A3000%2C%22reverse%22%3Atrue%2C%22filter%22%3A%22origin_type%3D11%22%2C%22fields%22%3A%22old%22%7D';

// Headers for requests
const headers = {
  'Authorization': 'FlespiToken YOUR_TOKEN_HERE',
  'Content-Type': 'application/json'
};

// URL for POST request
const postUrl = 'https://flespi.io/gw/devices';

// Function to perform GET request and fetch data
async function fetchData() {
  try {
    const response = await axios.get(getUrl, { headers });
    const data = response.data;

    // Transforming data
    const transformedData = data.result.map(item => {
      let a = item.old
      delete a.protocol_id
      delete a.cid
      delete a.id
      return a
    });

    console.log('response: ', data);

    console.log('Transformed data:', transformedData);

    // Returning transformed data
    return transformedData;
  } catch (error) {
    console.error('Error performing GET request:', error);
  }
}

// Function to split array into chunks
function chunkArray(array, chunkSize) {
  const chunks = [];
  for (let i = 0; i < array.length; i += chunkSize) {
    chunks.push(array.slice(i, i + chunkSize));
  }
  return chunks;
}

// Function to perform POST request
async function sendData(dataChunks) {
  try {
    for (const chunk of dataChunks) {
      const response = await axios.post(postUrl, JSON.stringify(chunk), { headers });
      console.log('Response to POST request:', response.data);
    }
  } catch (error) {
    console.error('Error performing POST request:', JSON.stringify(error.response.data, null, '  '));
  }
}

// Calling functions to fetch and send data
fetchData().then(transformedData => {
  if (transformedData) {
    const dataChunks = chunkArray(transformedData, 100);
    sendData(dataChunks);
  }
});
