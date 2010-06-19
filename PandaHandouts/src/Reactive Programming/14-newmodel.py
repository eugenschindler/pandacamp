from Panda import *

# The "alarm" function generates an event at regular
# intervals - use "start=" and "step=" to control the timing.
c = alarm(start = 0, step = 2)

# This launches a panda:

def launch(w, x):
    p = panda(position = P3(localTime-2, 0,0 ))

# This calls the launch every 2 seconds

# Note that there is no particular model reacting here - you can
# have "free floating" reactions.  The object associated with this is the
# "world" object.
react(c, launch)
# Change the step on the alarm - what happens?
# Can you make the panda spin as it moves?
# Add a second launcher that uses the mouse button to fire

start()