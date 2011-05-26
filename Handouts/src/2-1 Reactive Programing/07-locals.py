from Panda import *

# A model can have other values associated besides things like position or hpr
# Let's add a value called "count" to our panda
p = panda()
p.count = 1.0
p.position = P3(p.count/3, 0, 0)
p.size = p.count/4
p.hpr = HPR(p.count/10.0, 0, 0)

# Use this to keep the panda from going up until the third time it's clicked
def goUp(p, v):
    c = p.count.now()+1 # You need to use now() to be able to use the if
    if (c == 4):
        c = 1.0
    p.count = c

def goDown(p, v):
    c = p.count.now()-1 # You need to use now() to be able to use the if
    p.count = c
text(p.count)

p.react(lbp, goUp)
p.react(rbp, goDown)

# Add a reaction to rbp that makes the count go down
# Put an "if" in the program so that when the count is equal to 4 it sets the count back to 1

start()