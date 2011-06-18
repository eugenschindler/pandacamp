from Panda import *

# a "when" is used to react to a condition - something this is true or false
# Conditions are usually created by > or <

# A reaction function for "when" only has one parameter: the model

def bounce(m, v):
    p.v = -p.v.now()*1.1
    p.wall = p.wall.now()*1.1
    m.position = p.position.now() + P3(p.v*(localTime), 0, 0)

# Make a panda moving right

p = panda(position = P3(time, 0, 0))
p.v = 1
p.wall = 1
p.when((getX(p.position) > p.wall) | (getX(p.position) < -p.wall), bounce)

# Make the panda go faster with each bounce.
# Make the "wall" a variable in the panda - increase the wall distance with each bounce.
start()