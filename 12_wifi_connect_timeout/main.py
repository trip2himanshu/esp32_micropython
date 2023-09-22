# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# configure the esp device in station mode
# connect with Wi-Fi using timeout and check the device IP
# when calling the function connect_wifi()
# you need to oprovide your ssid and password as input parameters 

import network
import time
import sys

def connect_wifi(ssid, psk, timeout):
    # object for wlan
    wlan = network.WLAN(network.STA_IF)
    # restart the wi-fi driver
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    # connect with target Wi-Fi
    wlan.connect(ssid,psk)
    print("connecting....")
    t = 0
    while wlan.isconnected() == False and t < timeout:
        print(timeout-t)
        t += 1
        time.sleep(1)
    if wlan.isconnected() == True:
        print("Connection established")
        return wlan
    else:
        print("Timeout expired, unable to connect")
        


if __name__ == "__main__":
    try:
        wlan = connect_wifi("your_ssid", "your_password", 10)
        if wlan.isconnected() == True:
            print(wlan.ifconfig())
        else:
            pass 
    except Exception as e:
        print("Error> ",e)
    except KeyboardInterrupt:
        print("Exit")
    sys.exit()
        