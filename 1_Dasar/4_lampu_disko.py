from machine import*
from time import*

led_merah = Pin(5, Pin.OUT)
led_kuning = Pin(4, Pin.OUT)
led_hijau = Pin(14, Pin.OUT)
led_putih = Pin(12, Pin.OUT)


def Nyala_1(n):
    a = 0
    while True:
        a += 1
        led_merah.on()
        led_hijau.on()
        led_kuning.on()
        led_putih.on()
        sleep(0.3)
        led_merah.off()
        led_hijau.off()
        led_kuning.off()
        led_putih.off()
        sleep(0.3)
        if a == n:
            break

def Nyala_2(n):
    a = 0
    while True:
        a += 1
        led_merah.on()
        sleep(0.1)
        led_merah.off()
        sleep(0.1)
        led_kuning.on()
        sleep(0.1)
        led_kuning.off()
        sleep(0.1)
        led_hijau.on()
        sleep(0.1)
        led_hijau.off()
        sleep(0.1)
        led_putih.on()
        sleep(0.1)
        led_putih.off()
        sleep(0.1)
        if a == n:
            break

Nyala_1(10)
Nyala_2(15)