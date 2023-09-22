# flasher.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# class for flashing the led
# for testing the led flashing with esp32 devkit
# it is recommended to put the flasher.py and main.py file into the esp device
# then run the main.py 

import machine
import time

# class for flashing the led
# input parameters are :
# pin number of led -> pin
# on time of the led -> on_time
# off time of the led -> off_time 
class Flasher:
    def __init__(self,pin,on_time,off_time):
        self.pin = pin
        self.on_time = on_time
        self.off_time = off_time
        self.led_state = 0
        self.last_change = 0
        self.led = machine.Pin(self.pin,machine.Pin.OUT)
    # method to update the led state using non-blocking delay 
    def update(self):
        # turn on the led 
        if (time.ticks_ms()-self.last_change)>=self.off_time and self.led_state == 0:
            self.last_change = time.ticks_ms()
            self.led_state = 1
            self.led.value(self.led_state)
            print(f"LED at pin {self.pin} is On")
        # turn off the led 
        elif (time.ticks_ms()-self.last_change)>=self.on_time and self.led_state == 1:
            self.last_change = time.ticks_ms()
            self.led_state = 0
            self.led.value(self.led_state)
            print(f"LED at pin {self.pin} is Off")

