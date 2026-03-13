# FLV stream player example

[run it in your browser](https://flespi-software.github.io/examples/video/flv-player.html#your-stream-uuid-here)

A standalone HTML page for low-latency playback of FLV streams from [flespi media server](https://flespi.com/kb/media-from-gps-trackers) using [mpegts.js](https://github.com/nicce/mpegts.js).

**Example:** [flv-player.html](flv-player.html)

## Usage

Open `flv-player.html` in your browser and pass the stream UUID as a URL hash:

    flv-player.html#your-stream-uuid-here

The player will automatically connect to `https://media.flespi.io/{uuid}` and start playback.

## Features

- **Low-latency playback** — stash buffer disabled, latency target ~0.5s
- **Latency chaser** — automatically adjusts playback rate (1.05x–2.0x) to keep up with the live edge
- **Stall recovery** — skips buffer gaps and seeks to live edge on prolonged stalls
- **Live stats overlay** — shows current latency and playback rate in the top-right corner
- **No dependencies to install** — mpegts.js is loaded from CDN
