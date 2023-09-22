# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# toggle the led state with each button press event
# Boot button is used as input button
# boot button on esp32s3 is connected with pin 0 

import machine
import time

# object for led
led = machine.Pin(42,machine.Pin.OUT)
# object for button with iternal pull_up 
button = machine.Pin(0,machine.Pin.IN, machine.Pin.PULL_UP)

# method to toggle the led with button press
def led_toggle():
    while True:
        try:
            # button.value() will be 1 when button is pressed 
            if not button.value():
                # toggle the led state 
                led.value(not led.value())
                # print the led state
                print("LED is on" if led.value() else "LED is off")
                # wait till the button is released 
                while not button.value():
                    time.sleep_ms(5)
        except KeyboardInterrupt:
            print("Exit")
            break

led_toggle()

    