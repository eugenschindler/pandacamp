from Panda import *

# a "when" is used to react to a condition - something this is true or false
# Conditions are usually created by > or <


def bounce(m, v):
    p.v = -p.v.now()  # v is the velocity
    m.position = p.position.now() + P3(p.v*(localTime), 0, 0)

# Make a panda moving right

p = panda(position = P3(time, 0, 0))
p.v = 1
p.when((getX(p.position) > 1) | (getX(p.position) < -1), bounce)


# Make the panda go faster with each bounce.
# Make the "wall" a variable in the panda - increase the wall distance with each bounce.
#
start()