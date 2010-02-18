from Panda import *

# a "when" is used to react to a condition - something this is true or false
# Conditions are usually created by > or <

# A reaction function for "when" only has one parameter: the model

def startOver(m):
    p.dir = -p.dir.now()
    m.position = P3(p.dir*(localTime-2), 0, 0)
    p.when(localTime >3, startOver)
# Make a panda moving right
p = panda(position = P3(localTime-2, 0, 0))
# When 3 seconds have elapsed, start over.
# Why is this when1 instead of when?
# Now add another when that turns the panda green when the x coordinate is
# bigger than 2.5

start()