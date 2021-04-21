from machine import *
from time import *

# PRAKTEK 

led1 = PWM (Pin(4), Pin.OUT)
led2 = PWM (Pin(5), Pin.OUT)
led1.freq(500)
led2.freq(500)

def nyala1(n):
    a = 0
    while True:
        a += 1
        led1.duty(100)
        sleep(0.5)
        led1.duty(0)
        led2.duty(500)
        sleep(0.5)
        led2.duty(0)
        if a == n:
            break

def nyala2(n):
    a = 0
    while True:
        a += 1
        led_max = 1000
        led_min = 0
        step = 50
        for x in range(led_min, led_max, step):
            led1.duty(x)
            led2.duty(x)
            sleep(0.05)
        led1.duty(0)
        led2.duty(0)
        if a == n:
            break

def nyala3(n):
    a = 0
    led_max = 1000
    led_min = 0
    step = 50
    while True:
        a += 1
        for x in range(led_min, led_max, step):
            led1.duty(led_max - x)
            led2.duty(led_max - x)
            sleep(0.05)
        led1.duty(0)
        led2.duty(0)
        if a == n:
            break


nyala1(5)
nyala2(10)
nyala3(10)



