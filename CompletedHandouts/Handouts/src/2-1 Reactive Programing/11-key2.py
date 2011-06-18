from Panda import *


# Use the "key value" to control things
# If you add a second parameter to key, like key('a', 1), then this
# is the event value that comes with the key.
# This is important if you combine different events - using "+", you can
# listen for more than one event at once, for example
#  key('a') + key('b')
# triggers when you type a or b.  But to make different things happen for
# a and b, you need to give them different values.

text("Press z to spin, x to stop, c to reverse")

p = panda(position = P3(0,0,0))

def sethpr(m, v):
    m.hpr = m.hpr.now() + localTime*v


p.react(key('z', HPR(1, 0, 0)) + key('x', HPR(0,0,0)) + key('c', HPR(-1, 0, 0)), sethpr)
# Now use the same reaction function and add a
# second react event that will stop the spinning
# Once you've done that, you can remove the second
# reaction and instead combine the two events using +:
# this combines two event streams into 1
# Finally, add a third event that spins backwards

start()