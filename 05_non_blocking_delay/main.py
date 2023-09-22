# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# using a non-blocking delay with esp32s3
# the led state is being toggled 
import machine
import time

# method to toggle the led 1
def toggle_led(pin,on_time,off_time):
    # object for led
    led = machine.Pin(pin,machine.Pin.OUT)
    # variables
    last_change = 0
    led_state = 0
    while True:
        try:
            if led_state == 0 and (time.ticks_ms()-last_change >= off_time):
                last_change = time.ticks_ms()
                led_state = 1
                led.value(led_state)
                print("LED is on")
            elif led_state == 1 and (time.ticks_ms()-last_change >= on_time):
                last_change = time.ticks_ms()
                led_state = 0
                led.value(led_state)
                print("LED is off")
        except KeyboardInterrupt:
            print("Exit")
            break
        except Exception as e:
            print("Error: ",e)
            break

toggle_led(8,200,400)
