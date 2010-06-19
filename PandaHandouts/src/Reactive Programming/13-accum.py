# The accum function starts with a given value and then
# uses events that change the value in some way.
# These functions change a number:
#   add(x): add x to the number
#   sub(x): subtract x from the number
#   times(x): multiply the number by x
#   const(x): change the number to x

from Panda import *

text("Press a to raise the bear by .1")
text("Press s to lower the bear by .1")
text("Press d to double the bear's height")
text("Press f to reset the bear to 0")
text("Use q and w to change the roll")
# This uses the "a" key to add .1 to the position
# Can you:
#   Add the other three events (remember to use + to combine events)
#   Start the panda out at z = -2 instead of z = 0?
#   Use a second set of keys to control the roll?
pos = accum(0, key("a", add(.1))+ key("s", sub(.1)))


panda(position = P3(0, 0, pos))
text(pos)

start()