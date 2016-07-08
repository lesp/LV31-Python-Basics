from gpiozero import LED, Button
from time import sleep
from random import choice

red = LED(17)
amber = LED(27)
green = LED(22)
button = Button(2)
flashes = 3
LEDS = [red,amber,green]

while True:
    if button.is_pressed:
        colour = choice(LEDS)
        print(colour)    
        for i in range(flashes):
            colour.on()
            sleep(0.5)
            colour.off()
            sleep(0.5)
