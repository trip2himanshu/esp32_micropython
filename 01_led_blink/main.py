# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# blink the led connected with D42 pin 

import machine
import time

# object for led
led = machine.Pin(42, machine.Pin.OUT)

def led_blink():
    # toggle the led state 
    led.value(not led.value())
    # print the message 
    print("LED is on" if led.value() else "LED is off")
    # sleep for 2 sec 
    time.sleep(2)

if __name__ == "__main__":
    while True:
        try:
            led_blink()
        except KeyboardInterrupt:
            print("Exit")
            break

        
    
    