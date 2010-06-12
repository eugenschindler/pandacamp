# intro to Panda/08-mouse.py
from Panda import *

# Use the mouse to control your panda
# Mouse values are in (-1,-1) to (1,1)


# Show where the mouse currently is:
text(mouse)

# Change parameters so that the mouse is controlling the panda's
# position or hpr.
# Use getX and getY to take just the X or Y coordinate out of the
# mouse position.

panda(position = P3(getX (mouse), getY (mouse*5), 0), hpr = HPR(getX (mouse*pi),getY (-mouse),0))

start()