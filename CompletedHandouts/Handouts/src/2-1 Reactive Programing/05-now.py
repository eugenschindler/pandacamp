from Panda import *
# We've been limited by not being able to observe the old value of something like a position or hpr
# when computing the new value.  Within a reaction function, you can use .now() to get the current
# (constant) value of a signal like position or hpr.

# Let's move a panda up and down from it's current location

p = panda()
# This takes the panda, looks at the current position,
# and starts going up from this position
def goUp(p, v):
    here = p.position.now()
    p.position = here + P3(0,0,localTime)
    hpr1 = p.hpr.now()
    p.hpr = hpr1 + HPR(localTime, 0, 0)
def goDown(p, v):
    here = p.position.now()
    p.position = here + P3(0,0,-localTime)
    hpr1 = p.hpr.now()
    p.hpr = hpr1 + HPR(-localTime, 0, 0)
# On the left button press, go up
p.react(lbp, goUp)
p.react(rbp, goDown)
# Try adding a print statement to the goUp function so
# you can see where you are when you start to go up
# print "Position is " + p.here
# Make the panda turn right as it goes up and left as it goes down.




start()