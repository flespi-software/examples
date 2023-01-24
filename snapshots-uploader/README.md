# flespi.io Snapshots Uploader Tool

**Example:** [snapshots_uploader.py](snapshots_uploader.py)

**To start this example you need to install the following dependencies:**

    pip install requests

**You must also configure the script by editing the lines:**

    filename = '1674415503.gz' # snapshot filename

    token = 'YOUR_FLESPI_TOKEN_HERE'

    id = 0 # set your device id

    # if from_timestamp and to_timestamp are zero - republish all messages from the snapshot
    from_timestamp = 0
    to_timestamp = 0

    count = 100 # messages in chunk

**Then start the example:**

    python snapshots_uploader.py
