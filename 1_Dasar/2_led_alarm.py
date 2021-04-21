from machine import *
from time import *

led = Pin(4, Pin.OUT)

def Led_Lambat():
    a = 0
    while True:
        a += 1
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        if a == 5:
            break

def Led_Cepat():
    b = 0
    while True:
        b += 1
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)
        if b == 5:
            break

Led_Lambat()
Led_Cepat()