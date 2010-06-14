# Vectors and Interpolation/02-vectors.py
# Adding and scaling vectors
# This is the same example except you can make
# this easier to understand by using just two
# values: the initial point (a P3) and the direction
# (another P3).  You can add two P3's together and multiply
# a P3 by a number.

from Panda import *

# Replace these by two P3's
p0 =
vel =
# Replace the definition of p0 by a slider, using sliderP3.
# Observe what happens when the velocity changes as the program runs

def f(t):
     return p0 + t*vel


b = panda(position = f(time))

camera.location = P3(0, -10, 0)

# Add a second function, g, that does the same thing with HPR - you can add these and
# multiply them just like P3s.  Use g to set the hpr of your panda.

start()