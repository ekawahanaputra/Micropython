from machine import *
from time import *

# Push button adalah tombol atau saklar yang apabila ditekan akan menjadi on ataupun off, on atau off
# inilah yang akan digunakan sebagai sinyal untuk kepentingan terentu.
# pada contoh kali ini, push button akan digunakan sebagai sinyal input untuk menghidupkan led

button = Pin(0, Pin.IN, Pin.PULL_UP)     # ===>> Pin.IN berarti pin untuk sinyal input dan sebalikanya
led = Pin(5, Pin.OUT)

while True:
    button.value()
    sleep(1)
    if button.value() == 0:
        print("ON")
        led.on()
        sleep(1)
    else:
        print("OFF")
        led.off
        sleep(1)