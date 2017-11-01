from microbit import *

power_on = False

while True:
    
    if button_a.was_pressed():
        power_on = True
        
    if button_b.was_pressed():
        display.clear()
        power_on = False
        
    if power_on:
        x_accel = accelerometer.get_x()
        if x_accel < 0:
            display.show('-')
        elif x_accel > 0:
            display.show('+')
        else:
            display.show('0')
