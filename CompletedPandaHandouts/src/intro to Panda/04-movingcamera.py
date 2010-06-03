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

x = slider(min = -10, max = 10, init = 0, label = "left/right")
y = slider(min = -10, max = 10, init = -5, label = "back/forward")
z = slider(min = -10, max = 10, init = 0, label = "up/down")
h = slider(max = 2*pi, label = "h")
p = slider(max = 2*pi, label = "p")
r = slider(max = 2*pi, label = "roll")
text(format("Position: (%7.3f, %7.3f, %7.3f)", x, y, z))
text(format("HPR: (%7.3f, %7.3f, %7.3f)", h, p, r))

panda(position = P3(0,0,0))

camera.position = P3(x, y, z)
camera.hpr = HPR(h, p, r)
start()


