from Panda import *

# This time we'll react to a key from the keyboard

text("Press a to spin")
text("Press e to give bunny a seizure ")
text("Press d to reverse")
text ("Press s to stop")
text ("Press h to light fire")
text ("Press g to extinguish fire")
p = bunny(position = P3(0,0,0))
def akey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr)+ time*time, 0, 0)
p.react(key('a'), akey) 



def dkey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr)+ -time*time, 0, 0)
p.react(key('d'), dkey)

def ekey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(time-6, time*50, time+2)
p.react(key('e'), ekey)

def skey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr), 0, 0)
p.react(key('s'), skey)

f=fireish (position=P3 (0,0,0))
def gkey(p,v=None):
    p.stop()
def hkey(p,v):
    p.start()
f.react(key('g'),gkey)
f.react(key('h'),hkey)
world.color=black
f.when1(time>0,gkey)
ambientlight (color=gray)
directionallight (color=white, hpr=HPR (time,.5,0))
# Add another reaction that will stop the panda
# from spinning.

# Use a function to add the reactions to the panda.  Then create a scene in
# which three models at different locations all react to the same keys.

# Finally, add two parameters to the function to specify the keys to start / stop
# so that each model can have a different set of keys to control it

start()