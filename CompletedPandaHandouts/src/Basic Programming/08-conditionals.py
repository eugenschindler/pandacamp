#works but kinda thin on material 1/25/11 (TIFF)
from Panda import *

# A "conditional" allows you to choose one or the other alternative.
# We've seen "if" - there's another way to do this that allows you
# to constantly reconsider the choice: choose(test, ifTrue, ifFalse)
# For example, choose(x < 2, red, blue) will be either red or blue
# depending on the value of x.

p = panda()
# Give a panda the name "p"
mouseControl(p)
# Let the mouse move the panda around

# Set the color of the panda to be red if the x coordinate of the
# position is < 0 or blue otherwise.

p.color = choose(sin(time/10)<0, green, blue)

camera.position = P3(0, -5, 0)

# Can you change the size based on the position?
# Can you change the orientation based on the position?
# Can you make it turn clockwise / counterclockwise based on the position
start()