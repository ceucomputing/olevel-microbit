from microbit import *
import random

# Length and height of display
N = 5

# Delay between gem drops
DROP_DELAY = 500

# The gem is a pair of x and y coordinates
gem = [random.randint(0, N - 1), 0]

while True:
    # Draw the gem
    display.clear()
    display.set_pixel(gem[0], gem[1], 5)

    # Drop gem by 1 pixel
    gem[1] += 1

    # Check if gem is no longer visible
    if gem[1] > N - 1:
        # If so, move gem to random position at top of display
        gem = [random.randint(0, N - 1), 0]

    sleep(DROP_DELAY)
