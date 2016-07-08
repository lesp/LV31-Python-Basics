from gpiozero import LED, Button
from time import sleep
from random import choice
red = LED(17)
amber = LED(27)
green = LED(22)
red_button = Button(2)
amber_button = Button(3)
green_button = Button(4)
flashes = 3
LEDS = [red,amber,green]
def lightup(colour):
    for led in LEDS:
        led.off()
    if colour == "red":
        red.on()
    elif colour == "amber":
        amber.on()
    else:
        green.on()
while True:
    if red_button.is_pressed:
        print("RED")
        lightup("red")
    elif amber_button.is_pressed:
        print("AMBER")
        lightup("amber")
    elif green_button.is_pressed:
        print("green")
        lightup("green")
    sleep(0.1)

