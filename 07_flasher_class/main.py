# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# flash the multiple leds independently

import flasher

# object for led 1
led1 = flasher.Flasher(8,500,900)
# object for led 2
led2 = flasher.Flasher(47,300,1200)

while True:
    try:
        # update the states of leds
        led1.update()
        led2.update()
    except KeyboardInterrupt:
        print("Exit")
        break
    