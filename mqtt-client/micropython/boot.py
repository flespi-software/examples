# This file is executed on every boot (including wake-boot from deepsleep)
#
# To upload files use next commands:
# ampy --port /dev/ttyUSB0 put boot.py
# ampy --port /dev/ttyUSB0 put mqtt.py
# ampy --port /dev/ttyUSB0 put wifi.py
#
# To connect to your esp use(linux):
# picocom /dev/ttyUSB0 -b115200

import esp
esp.osdebug(None)
esp.check_fw()

import time
time.sleep(3)

import uos
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

import os
os.listdir()

# Your flespi token
token = "YourFlespiTokenHere"
topic = "myesp/light"
# Wi-Fi settings
wifissid = "test"
wifipassword = "12345678"

import wifi
import mqtt
import machine
adc = machine.ADC(0) # get ADC pin
net = None
while True:
    if (not net or net.isconnected() == False):
        print("Waiting for connect")
        # Connect to preconfigured WiFi default: test:12345678
        net = wifi.connect(ssid=wifissid, password=wifipassword)
    else:
        print("Try to send data")
        try:
            # Send 'hello world!' to topic 'test'
            mqtt.send(user=token)
            # send light sensor state
            mqtt.send(
                topic,
                data=adc.read(),
                client_id='testmicropython',
                server='mqtt.flespi.io',
                port=1883,
                user=token,
                password=''
            )
        except Exception as inst:
            print("Can't send!")
            print(inst)
            pass
    time.sleep(10) # retry every 10 seconds
