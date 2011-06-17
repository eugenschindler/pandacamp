from Panda import *

text(mouse)


# Use the mouse to control some models
# You have to do a getX or getY to pull apart the 2-D coordinate
# The number will always be between -1 and 1
# Control the z of two different models with the mouse
# How could you adjust a number between 0 and 10 instead of -1 to 1?
# Control the angle two models (how do you scale -1 to 1 into an angle?)
pos = P3(3*getX(mouse),0,3*(getY(mouse))-.5)
vel =integral(P3(getX(mouse),0,getY(mouse)))
pos1 = integral(vel)
p = panda(position = pos1, hpr = HPR(getX(vel), -getZ(vel), 0))
text(p.position)
text(p.hpr)



start()