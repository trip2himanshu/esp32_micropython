# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# writing a class for toggling the led

import machine
import time
import sys

# class for toggling the led 

class Toggle:
    # init method 
    def __init__(self,pin,on_time,off_time):
        self.pin = pin
        self.on_time = on_time
        self.off_time = off_time
        self.last_change = 0
        self.led_state = 0
        # object for led
        self.led = machine.Pin(self.pin,machine.Pin.OUT)
    # update method to update the led state 
    def update(self):
        if (time.ticks_ms()-self.last_change >= self.off_time) and self.led_state is 0:
            self.last_change = time.ticks_ms()
            self.led_sate = 1
            self.led.value(self.led_state)
            print(f"led at pin {self.pin} is on")
        elif (time.ticks_ms()-self.last_change >= self.on_time) and self.led_state is 1:
            self.last_change = time.ticks_ms()
            self.led_sate = 0
            self.led.value(self.led_state)
            print(f"led at pin {self.pin} is off")

# object for led 1 connected with pin 8
led1 = Toggle(8,400,800)
# object for led 2 connected with pin 9
led2 = Toggle(9,700,300)

try:
    while True:
        # update the state of leds 
        led1.update()
        led2.update()
except KeyboardInterrupt:
    print("Exit")
    sys.exit()

                    
        