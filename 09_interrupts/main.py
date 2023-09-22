# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# hardware interrupts with ESP32S3 DevkitC-1
# toggle the led with each button press using interrupts 

import machine
import time

# object for led
led = machine.Pin(8,machine.Pin.OUT)
# object for button
button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)


# interrupt service routine button
def button_isr(p):
    led.value(not led.value())
    print("LED is on" if led.value() else "LED is off")
    
# interrupt initialization
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_isr)

while True:
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("Exit")
        break
    