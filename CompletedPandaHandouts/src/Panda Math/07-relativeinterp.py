#shaking but works 1/25/11 TFF
from Panda import *
# Relative interpolation means that instead of knowing exactly where you want to go
# you know the way to go to get there.

# For example, this moves up (incrementing z) and then right (incrementing x)
i = move(.1, HPR(0,0,.1)) + move(.1,HPR(.1,0,0))

# First, use this as the path of a panda.
# You'll have to do something to get the panda started - it needs to know where
# the path begins (how?)
# How long is this path?
# How can you make the slider have the right range?
# Now, if you put this "stair step" in a variable. you can make a path with three
# steps in it.
# Can you add three steps going down after the three that go up?
panda(hpr=(interpolate(time, at(HPR(0,0,0)) + forever(i))))

start()