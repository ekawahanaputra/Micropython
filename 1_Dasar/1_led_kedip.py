from machine import Pin
import time

led = Pin(5, Pin.OUT)

x = 0
while True:
    x += 1
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(1)

    if x == 5:
        break