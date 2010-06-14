# Adding and scaling vectors
# This is the same example except you can make
# this easier to understand by using just two
# values: the initial point (a P3) and the direction
# (another P3).  You can add two P3's together and multiply
# a P3 by a number.

from Panda import *

# Replace these by two P3's
p0 = P3(0,0,0)
vel = sliderP3(min = -5, max = 5, label = "Velocity")
hpr0 = HPR(0,0,0)
hprv = HPR(1, .3, .1)

# This needs to be rewritten to use
# P3's
def f(t):
     return p0 + t*vel

def g(t):
    return hpr0 + t*hprv

b = panda(position = f(time), hpr = g(time))

camera.location = P3(0, -10, 0)
# Try changing the HPR instead of the position
# Try using a slider to allow the value to be changed while the
#  program is running

start()