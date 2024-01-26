# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# setup esp device in access point mode
# in AP mode esp device acts as hotspot and other devices may connect with it 

import network
import sys
import time 

try:
    # object for wlan
    wlan = network.WLAN(network.AP_IF)
    # restart the wlan driver
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    # wi-fi configuration
    wlan.config(ssid='myESP', password='123456789', authmode=network.AUTH_WPA_WPA2_PSK)
    # print the ip address of esp device
    print(wlan.ifconfig())
except Exception as e:
    print(f"Error > {e}")
    
sys.exit()
    

