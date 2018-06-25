from microbit import *

while True:
    a = button_a.is_pressed()
    b = button_b.is_pressed()

    if a and b:
        display.show('F')
    elif a:
        display.show('L')
    elif b:
        display.show('R')
    else:
        display.show('S')
    
    sleep(100)
    