# intro to Panda/03-rotatingpanda.py
from Panda import *

# Create a panda at (0,0,0) and play with hpr using a slider
# Try "h = slider(min = 0, max = 2*pi, label = "h")" to make a slider.

# Note that pi is a defined constant
# Note that degrees(360) would have worked too
# Change this to alter pitch and roll

h = slider(min = 0, max = 2*pi, label = "heading")

panda (position = P3 (0,0,0), hpr = HPR(h, 0, 0))

start()