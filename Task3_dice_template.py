from microbit import *
import random

while True:
    if button_a.was_pressed():
        display.on()
    if accelerometer.is_gesture('shake'):
        print(random.randint(0,5))
    if button_b.was_pressed():
        display.off()
    