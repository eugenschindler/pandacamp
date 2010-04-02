from Panda import *


# Use the "key value" to control things
# If you add a second parameter to key, like key('a', 1), then this
# is the event value that comes with the key.
# This is important if you combine different events - using "+", you can
# listen for more than one event at once, for example
#  key('a') + key('b')
# triggers when you type a or b.  But to make different things happen for
# a and b, you need to give them different values.

text("Z to spin, X to stop, C to reverse")
text("W A S D to move")

p = panda(position = P3(0,0,0))
# When the "a" key is pressed, spin the panda
# Note that the v in the reaction is being used
def zkey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr)+ time-5, time*55, time)
p.react(key('z', localTime), zkey)
def xkey(p, v):
    hpr = p.hpr.now()
    pos = p.position.now()
    p.hpr = HPR(getH(hpr),getP(hpr),getR(hpr))
    p.position=P3(getX(pos),getY(pos),getZ(pos))
p.react(key('x', localTime), xkey)
def ckey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr)+ time-15, localTime*localTime, -time)
p.react(key('c', localTime), ckey)

def pos(p,v):
    position = p. position.now()
    p.position = position+v

def wkey(p, v):
    hpr = p.hpr.now()
    p.position = P3(0, localTime, 0)
p.react(key('w', localTime), wkey)

def skey(p, v):
    hpr = p.hpr.now()
    p.position = P3(0, -localTime, 0)
p.react(key('s', localTime), skey)

def akey(p, v):
    hpr = p.hpr.now()
    p.position = P3(-localTime, 0, 0)
p.react(key('a', localTime), akey)

def dkey(p, v):
    hpr = p.hpr.now()
    p.position = P3(localTime, 0, 0)
p.react(key('d', localTime), dkey)


# Now use the same reaction function and add a
# second react event that will stop the spinning
# Once you've done that, you can remove the second
# reaction and instead combine the two events using +:
# this combines two event streams into 1
# Finally, add a third event that spins backwards

start()