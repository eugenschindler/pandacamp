__author__="stu885974"
__date__ ="$Mar 2, 2011 10:28:01 AM$"

from Panda import *
# Adjust the slider to set the speed of the panda.
# The "integral" operation turns speed into position.


x = slider(min = -1, max = 1, init = 0)
text(format("X Velocity: %5.3f", x))
y = slider(min = -1, max = 1, init = 0)
text(format("Y Velocity: %5.3f", y))
z = slider(min = -1, max = 1, init = 0)
text(format("Z Velocity: %5.3f", z))

p = panda(position = P3(integral(x), integral(y), integral(z)))
text(format("Position: %5.3f", getX(p.position)))
start()