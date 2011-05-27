from Panda import *


#p.react(key('s'), skey)

c = alarm(start = 0, step = 2)

    # Write a function to create a new bear and send it
    # moving right across the screen.  Use "localTime"
    # to create your motion.
def launch(w, x):
    panda (position=P3 (localTime-2,0,0),hpr=HPR (time*time, time*2, time-4))
# This calls the launch every 2 seconds

# Note that there is no particular model reacting here - you can
# have "free floating" reactions.  The object associated with this is the
# world object.
react(c, launch)
start()
