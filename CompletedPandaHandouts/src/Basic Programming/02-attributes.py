#pretty sweet, works just fine 1/25/11 (TIFF)
from Panda import *

# The "." notation allows you to observe the position, hpr, size, or color
# of a named model.

# The following panda moves in a circle (don't worry about the sin / cos
# stuff just yet!)
p = panda(position = P3(sin(time*3), 0, cos(time)))
p1 = panda(position = P3(sin(time*5), 4, cos(time*2)))
fred = panda(color =  color(.4*sin(time)+.4, .4, .4))
fred2 = panda(color =  color(sin(time)+.4, .7, .7))
fred.position = p. position + P3(1,0,0)
fred2.position = p1. position + P3(1,-1/2,1)

# Create a second panda whose position is the position of p + P3(1,0,0)
# That is, the second panda will be 1 unit to the right.  Color this second
# panda blue.

start()
