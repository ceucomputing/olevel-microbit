from microbit import *

pin1.set_analog_period(20)
pin2.set_analog_period(20)

def forward():
    pin1.write_analog(180)
    pin2.write_analog(1)

def stop():
    pin1.write_analog(0)
    pin2.write_analog(0)

def left():
    pin1.write_analog(1)
    pin2.write_analog(1)
    
def right():
    pin1.write_analog(180)
    pin2.write_analog(180)
