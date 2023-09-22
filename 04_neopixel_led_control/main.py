# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# control the onboard neopixel led on devkit
# step 1: turn on each color (RGB) one by one
# change color continuously 

import machine
import neopixel 
import time
import sys

# object for neopixel led
# on devkit the neopixel led is connected with GPIO 48
# and only 1 pixel is available 
np = neopixel.NeoPixel(machine.Pin(48),1)

# method to on each color led one by one
def color_on():
    try:
        # on RED color led 
        np[0] = (255,0,0)
        np.write()
        time.sleep(2)
        # on Green color led
        np[0] = (0,255,0)
        np.write()
        time.sleep(2)
        # on BLUE color led
        np[0] = (0,0,255)
        np.write()
        time.sleep(2)
    except KeyboardInterrupt:
        print("Exit from color_on() method")
        exit()
    except Exception as e:
        print(f"Error in color_on() > {e}")
        exit()


# method for smooth color change with neopixel led
def color_change():
    red = 0
    green = 255
    blue = 128
    while True:
        try:
            np[0] = (red,green,blue)
            np.write()
            time.sleep_ms(10)
            if red >= 255:
                red = 0
            if green <= 0:
                green = 255
            if blue >= 255:
                blue = 128
            red = red+1
            green = green-1
            blue = blue+1
        except Exception as e:
            print(f"Error in color_change() > {e}")
            break
        except KeyboardInterrupt:
            print("Exit from color_change()")
            break
    exit()


#  method for exiting the code
def exit():
    np[0] = (0,0,0)
    np.write()
    sys.exit()
    
    
color_on()
color_change()
    