
# Random Numbers

from Panda import *

# You can use rand() to get a random number between 0 and 1.

# This puts a panda at a random location:

panda(position = P3(rand()*4-2, 0, rand()), hpr = HPR(time*rand(), time , 0))
panda(position = P3(rand()*4-2, 0, rand()), hpr = HPR(time*rand(), time , 0))
# Run this twice - see if the pandas are always in the same place

# Recall that we can use a simple function to do things repeatedly:

def lots(i):
    if i > 0:
        panda(position = P3(rand()*4-2, 0, rand()*4-2), hpr = HPR(time*rand(), time, time))
        lots(i-1)
# Use lots to make 20 pandas
# Modify "lots" to make the pandas spread out with x and y between -2 and 2
# instead of between 0 and 1.

# Finally, give each panda a spin - choose a random spin rate and multiply
# this by "time".

lots(15)
start()