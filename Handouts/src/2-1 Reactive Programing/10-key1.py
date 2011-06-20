from Panda import *

# This time we'll react to a key from the keyboard

text("Press a to spin")
text("Press s to stop")
p = panda(position = P3(0,0,0))
# When the "a" key is pressed, spin the panda
def akey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr)+ localTime, 0, 0)
p.react(key('a'), akey)
# Add another reaction that will stop the panda
# from spinning.

# Use a function to add the reactions to the panda.  Then create a scene in
# which three models at different locations all react to the same keys.

# Finally, add two parameters to the function to specify the keys to start / stop
# so that each model can have a different set of keys to control it

def skey(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr), 0, 0)
p.react(keyUp('a'), skey)


start()