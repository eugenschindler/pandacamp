
from Panda import *

# leftClick is a way to detect clicks on a particular model.

def countDown(p, v):
    c = p.count.now()-1 # You need to use now() to be able to use the if
    if (c == 0):
        p.hpr = HPR(pi, 0, 0)  # Turn backwards when the count is 0
    p.count = c

p = panda()
p.count = 3.0
p.react(leftClick(p), countDown)
text(p.count)

# Add a second panda with a different initial count.  Use the same reaction function.
#

start()