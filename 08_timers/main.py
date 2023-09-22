# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# timers in esp32
# it has Four hardware timers, named as Timer 0 to Timer 3
# Timers can be used for various timining related tasks,
# such as generating PWM signals, measuring time intervals and schedule tasks
# Timer 2 has dedicated hardware PWM controller
# Timer 0, Timer 1 and Timer 3 can be used for various timing tasks

import machine


# object for led
led = machine.Pin(8,machine.Pin.OUT)
# object for timer
timer0 = machine.Timer(0)

# method for handling ISR of timer
def timer0_isr(t):
    led.value(not led.value())
    print("LED is on" if led.value() else "LED is off")

# set the timer mode (initialize timer)
# timer can be start using timer0.start() and
# it can be stopped using timer0.stop() methods
# Timer automatically starts with the initialization
timer0.init(mode=machine.Timer.PERIODIC, period=1000, callback=timer0_isr)

while True:
    try:
        pass
    except KeyboardInterrupt:
        print("EXIT")
        break



