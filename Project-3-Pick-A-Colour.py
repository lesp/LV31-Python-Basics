from gpiozero import LED, Button
from time import sleep
from random import choice
from signal import pause

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

if red_button.is_pressed:
    print("RED")
    lightup("red")
elif amber_button.is_pressed:
    lightup("amber")
elif green_button.is_pressed:
    lightup("green")
        
pause()
