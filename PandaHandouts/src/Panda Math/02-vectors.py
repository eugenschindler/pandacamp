# Adding and scaling vectors
# This is the same example except you can make
# this easier to understand by using just two
# values: the initial point (a P3) and the direction
# (another P3).  You can add two P3's together and multiply
# a P3 by a number.

from Panda import *

# Replace these by two P3's
p0 = P3(0,0,0)
vel = P3(1,1,1)

# This needs to be rewritten to use
# P3's
def f(t):


b = panda(position = f(time))
camera.location = P3(0, -10, 0)
# Try changing the HPR instead of the position
# Try using a slider to allow the value to be changed while the
#  program is running

start()