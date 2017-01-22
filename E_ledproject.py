#!/usr/bin/env python
import RPi.GPIO as GPIO

led_color_gpio = {
    'yellow': 0,
    'orange': 2,
    'red': 3,
    'green': 4,
    'blue': 5,
    'white': 6
}

buttons_gpio = {
    'red': 28,
    'blue': 29,
    }

gpio_to_bcm = {
    0: 17,
    1: 18,
    2: 27,
    3: 22,
    4: 23,
    5: 24,
    6: 25,
    21: 5,
    22: 6,
    23: 13,
    24: 19,
    25: 26,
    26: 12,
    27: 16,
    28: 20,
    29: 21,
    }

def led_color(color, on):
    if color not in led_color_gpio:
        print('No LEDs of color {0}'.format(color))
        return
    bcm_pin = gpio_to_bcm[led_color_gpio[color]]
    if on:
        GPIO.output(bcm_pin, False)
    else:
        GPIO.output(bcm_pin, True)

GPIO.setmode(GPIO.BCM)
for gpio in led_color_gpio.values():
    print("setting gpio {0} BCM pin {1}".format(gpio, gpio_to_bcm[gpio]))
    bcm_pin = gpio_to_bcm[gpio]
    GPIO.setup(bcm_pin, GPIO.OUT)
    GPIO.output(bcm_pin, True)


print("Type 'quit' to quit")
while True:
    user_input = raw_input("Enter Color and on/off: ")
    tokens = user_input.split()
    if len(tokens) < 1:
        continue
    color = tokens[0]
    if color == "quit":
        break
    onoff = 1
    if len(tokens) > 1:
        onoff = tokens[1]
        if onoff == "on":
            onoff = 1
        elif onoff == "off":
            onoff = 0
        else:
            onoff = int(onoff)
    led_color(color, onoff)


for gpio in led_color_gpio.values():
    bcm_pin = gpio_to_bcm[gpio]
    GPIO.output(bcm_pin, True)
