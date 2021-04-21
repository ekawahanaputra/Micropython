from machine import*
from time import*

lampu_merah = Pin(5, Pin.OUT)
lampu_kuning = Pin(4, Pin.OUT)
lampu_hijau = Pin(14, Pin.OUT)

def Red(t):
    lampu_merah.on()
    sleep(t)
    lampu_merah.off()

def Yellow(n):
    x = 0
    while True:
        x += 1
        lampu_kuning.on()
        sleep(1)
        lampu_kuning.off()
        sleep(1)
        if x == n:
            break

def Green(t):
    lampu_hijau.on()
    sleep(t)
    lampu_hijau.off()

a = 0
while True:
    a += 1
    Red(10)
    Yellow(2)
    Green(10)
    Yellow(3)
    if a == 3:
        break
