# Vectors and interpolation/03-interpolation.py
from Panda import *

# How do you interpolate between two points?
# If the panda is at p0 at t = 0 and p1 at t = 1,
# what equation would make it move from p0 to p1 smoothly?
# what happens when t is not between 0 and 1?
# What if you want to make it arrive at p1 when t = 2 instead of 1?

p0 = P3(1,1, 1)
p1 = P3(2, 0, -1)
soccerball(position = p0, size = .05, color = red)
soccerball(position = p1, size = .05, color = blue)

t = slider(min = -1, max = 2, init = 0)
text(t)
text(p)
p = 
panda(position = p)

start()
