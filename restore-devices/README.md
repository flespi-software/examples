# Flespi Restore Devices Script

This Node.js script fetches information about deleted devices from the Flespi platform, processes this data, and recreates the devices by sending the data back to the Flespi platform in batches of 100.

## Prerequisites

- Node.js (version 14 or later)
- npm (Node package manager)

## Getting Started

1. **Clone the repository**

   ```sh
   git clone https://github.com/flespi-software/examples.git
   cd restore-devices
   ```

2. **Install the dependencies**

   ```sh
   npm install
   ```

3. **Update the script with your FlespiToken**

   Open the `index.js` file and replace the placeholder `FlespiToken` with your actual FlespiToken.

4. **Run the script**

   ```sh
   node index.js
   ```

## Script Explanation

The script performs the following steps:

1. **Fetch Data**: Sends a GET request to the Flespi platform to fetch logs of deleted devices.
2. **Transform Data**: Processes the received data to extract relevant device information.
3. **Send Data**: Recreates the deleted devices by sending the transformed data in batches of 100 to another endpoint on the Flespi platform.

## Dependencies

- [axios](https://www.npmjs.com/package/axios)\

These dependencies are automatically installed when you run `npm install`.

## Troubleshooting

- Ensure that your Node.js version is 14 or later.
- Make sure to replace the placeholder `FlespiToken` with your actual token.
- Check the console output for any error messages and ensure your internet connection is stable.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
