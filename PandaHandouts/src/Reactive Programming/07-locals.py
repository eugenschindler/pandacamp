from Panda import *

# A model can have other values associated besides things like position or hpr
# Let's add a value called "count" to our panda
p = panda()
p.count = 1.0
p.position = P3(p.count/3, 0, 0)

# Use this to keep the panda from going up until the third time it's clicked
def goUp(p, v):
    c = p.count.now()+1 # You need to use now() to be able to use the if
    if (c == 4):
        c = 1.0
    p.count = c

text(p.count)

p.react(lbp, goUp)

# Add a reaction to rbp that makes the count go down


start()