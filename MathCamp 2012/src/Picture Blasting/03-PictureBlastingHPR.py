from Panda import *

# Demonstrate the use of "time" to alter the HPR of each tile

pieces = blastPicture("mathcamp.jpg", 5, 5)

for p in pieces:
    p.position = p.location
    p.hpr = HPR(time, 0, 0)

# Things to do:
#   Change pitch and roll too
#   Change at different rates by multiplying the time components by an integer
#   Use random integers to set the rates
#   Add motion in the position too


start()