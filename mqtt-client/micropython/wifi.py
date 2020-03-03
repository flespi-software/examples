def connect(ssid="test", password="12345678"):
    import network

    net = network.WLAN(network.STA_IF)

    if net.isconnected() == True:
        print("Already connected")
        return

    net.active(True)
    net.connect(ssid, password)

    while net.isconnected() == False:
        pass

    print("Connection successful")
    print(net.ifconfig())
    return net
