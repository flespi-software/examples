fetch('http://ch0000000.flespi.gw:00000', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify([
    {
      ident: 'nodejs-fetch-example',
      timestamp: Date.now() / 1000,
      'message.type': 'example',
      'driver.message': 'Hello, flespi!'
    }
  ])
})
  .then(response => {
    // Handle response
    console.log(response);
  })
  .catch(error => {
    // Handle error
    console.log(error);
  });
