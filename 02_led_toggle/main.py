# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# toggle the led state 

import machine
import time

# method to toggle the led
# input parameters: led pin, on time, off time
def led_toggle(pin, on_time, off_time):
    # object for led pin
    led = machine.Pin(pin,machine.Pin.OUT)
    while True:
        try:
            # turn on the led
            led.value(1)
            print("LED is on")
            time.sleep(on_time)
            # turn off the led 
            led.value(0)
            print("LED is off")
            time.sleep(off_time)
        except KeyboardInterrupt:
            print("Exit")
            break


led_toggle(42,2,4)

        
    
    