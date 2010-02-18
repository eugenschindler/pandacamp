from Panda import *

text(mouse)


# Use the mouse to control some models
# You have to do a getX or getY to pull apart the 2-D coordinate
# The number will always be between -1 and 1
# Control the z of two different models with the mouse
# How could you adjust a number between 0 and 10 instead of -1 to 1?
# Control the angle two models (how do you scale -1 to 1 into an angle?)

panda(position = P3(-1,0,0), hpr = )
panda(position = P3(1,0,0), hpr = )
start()