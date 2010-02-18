from Panda import *

# Use the mouse to control your panda
# Mouse values are in (-1,-1) to (1,1)
# How can you get the mouse value to cover a specific range?

# Show where the mouse currently is:
text(format("Mouse: %5.3f, %5.3f", getX(mouse), getY(mouse)))

# Change parameters so that the mouse is controlling the panda's
# position or hpr.
# Use getX and getY to take just the X or Y coordinate out of the
# mouse position.

panda(position = P3(getX (mouse), getY (mouse*5), 0), hpr = HPR(getX (mouse*pi),getY (-mouse),0))

start()