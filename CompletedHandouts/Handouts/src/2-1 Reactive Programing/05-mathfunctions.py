# Mirroring rotation, on X

from Panda import *

# We can use functions to express interesting math relationships
# For example, here's a "mirrored" heading in a hpr:

def headingMirror(hpr):
    return HPR(-getH(hpr), -getP(hpr), -getR(hpr))

# Note that this uses something new: return
# You use this when a function is defining a value rather than
# changing things in a model

p = panda(position = P3(1,0,0), hpr = HPR(0, -getY(mouse), getX(mouse)))
p1 = panda(position = P3 (-1,0,0), hpr = headingMirror(p.hpr))
# add a second panda at (-1, 0, 0) that mirrors the hpr of p

# You can write a similar function to mirror the X coordinate of
# a P3 - try this!

#  Change p so that the location is P3(getY(mouse), 0, 0)
# and have the second panda mirror the location as well as the hpr
# Finally, create a function which mirrors the roll in the hpr and
# make the second panda mirror both the heading and the roll by calling
# both functions.  Set the roll of the first panda to be "time" instead
# of 0

start()
