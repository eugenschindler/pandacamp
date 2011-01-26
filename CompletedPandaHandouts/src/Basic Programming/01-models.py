# works fine as of 1/25/11 (TIFF)
from Panda import *
# Understanding models

# Every model has the following:
#  position
#  hpr
#  size
#  color

# There are two ways to define these:
#  When you initially create the model:
#   panda(position = P3(1,0,1))
#  or by giving the model a name and then using "." notation:
#   p = panda()
#   p.position = P3(1,0,0)
# These do exactly the same thing - the first is more concise but
# the other method allows you to separate creation of the model from
# setting its location.

# Create two pandas, naming them p1 and p2.  Set the locations to be
# P3(-.5, 0, 0) and P3(.5, 0 0) using the "." notation.
p1 = panda ()
p2 = panda ()
p1.pos = P3(-.5, 0, 0)
p2.pos = P3(.5, 0, 0)
p2.size = 5
# Warning!  If you misspell "position" in the "." notation, you won't
# get any error message.


start()