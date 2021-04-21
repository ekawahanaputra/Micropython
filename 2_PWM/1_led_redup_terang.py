from machine import *
from time import *

# Belajar membuat LED hidup redup dan terang dengan pin PWM

led = PWM(Pin(4), Pin.OUT)    # Mendeklarasikan pin 4 sebagai PWM
led.freq(500)                 # agar menjadi PWM, freq led harus bernilai 500

led.duty(10)
sleep(3)
led.duty(100)
sleep(3)
led.duty(500)
sleep(3)
led.duty(1000)
sleep(3)
led.duty(0)

# Cycle Duty dari led adalah 0 - 1000 untuk komponen elektronik yang lain,
# bisa lihat petunjuk dan referensi