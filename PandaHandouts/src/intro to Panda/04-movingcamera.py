# intro to Panda/04-movingcamera
from Panda import *
panda (position = P3 (0,0,0))

# Create a panda at (0,0,0) and move the camera using
# sliders to adjust the location and heading of the camera

# Note the use of "label" in making sliders
# We use "text" to add imformation to the scene on an overlay
# The %7.3f means to make a number with 7 digits, 3 after the "."
# Watch out - it's hard to grab the controls
# What do all the arguments to slider do?

start()