from gpiozero import LED
from time import sleep

red = LED(17)
amber = LED(27)
green = LED(22)
flashes = 3

while True:
    for i in range(flashes):
        red.on()
        sleep(0.5)
        red.off()
        sleep(0.5)
    for i in range(flashes):
        amber.on()
        sleep(0.5)
        amber.off()
        sleep(0.5)
    for i in range(flashes):
        green.on()
        sleep(0.5)
        green.off()
        sleep(0.5)
