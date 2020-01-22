# flespi.io Snapshots Downloader Tool

**Example:** [snapshots_downloader.py](snapshots_downloader.py)

**To start this example you need to install the following dependencies:**

    pip install requests

**You must also configure the script by editing the lines:**

    token = 'YOUR_FLESPI_TOKEN_HERE'

    itemtype = 'gw/devices'
    # itemtype = 'storage/containers' # To download containers snapshots uncomment this line

    ids = 'all' # You can list ids with a comma like '1,2,3,4' or 'all' for all items

**Then start the example:**

    python snapshots_downloader.py
