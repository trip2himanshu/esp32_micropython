# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# setup esp device in station mode
# in station mode esp may connect with any existing wi-fi network


import network
import sys

try:
    # object for wlan
    wlan = network.WLAN(network.STA_IF)
    # active the wlan driver
    wlan.active(True)
    # scan nearby networks
    networks = wlan.scan()
    # print the available networks
    print(networks)
except Exception as e:
    print(f"Error > {e}")
    
sys.exit()
    

