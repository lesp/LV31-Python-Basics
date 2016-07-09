from gpiozero import LED, Button
from time import sleep
red = LED(17)
amber = LED(27)
green = LED(22)
red_button = Button(2)
amber_button = Button(3)
green_button = Button(4)
LEDS = [red,amber,green]
def lightup(colour):
    for led in LEDS:
        led.off()
    if colour == "red":
        red.on()
    elif colour == "amber":
        amber.on()
    elif colour == "green":
        green.on()
while True:
    if red_button.is_pressed:
        print("RED")
        lightup("red")
    elif amber_button.is_pressed:
        print("AMBER")
        lightup("amber")
    elif green_button.is_pressed:
        print("GREEN")
        lightup("green")
    sleep(0.1)

