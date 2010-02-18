from Panda import *

# A model can have other values associated besides things like position or hpr
# Let's add a value called "count" to our panda
p = panda(position = P3(time, 0, 0))
p.count = 1
p.r=1
# Use this to keep the panda from going up until the third time it's clicked
def goUp(p, v):
    c = -p.count.now()*1.1  # You need to use now() to be able to use the if
    p.count = c            # Put a new value of count in the panda
    here = p.position.now()
    p.r=p.r.now()*.95
    p.color=color(p.r, 0, 0)# Only go up if the count is 3
    p.position = here + P3(0,0,localTime*c)

# Use "text" to watch the value of the count

p.react(lbp, goUp)

# Add two more if statements that move the panda left when the count is 1
# and right again when the count is 2.

start()