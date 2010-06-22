from Panda import *
# Abstraction is finding patterns and turning them into functions

# Suppose you want to create a line of different objects.  These all have
# a y and z coordinate of 0 but different x coordinates.  There are lots of different kinds of things.

def f(m, x):
    m(position = P3(x, 0, 0), hpr = HPR(time, 0, 0))

f(panda, 2)
f(jeep, 1)
f(boyBalloon, 0)
f(chair, -1)
# Add another parameter to f so that you can give each model a different size
start()
