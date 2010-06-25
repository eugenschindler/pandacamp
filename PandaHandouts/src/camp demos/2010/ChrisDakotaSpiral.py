from Panda import *

# The "alarm" function generates an event at regular
# intervals - use "start=" and "step=" to control the timing.
c = alarm(start = 0, step = .00001)
def launch(w,x):
    b=panda(size=.2,position=P3C(2,localTime, localTime/2-3),hpr=HPR(localTime+pi*10,0,localTime))
    p=bunny(size=.4,position=P3C(-2,localTime,localTime/2-3),hpr=HPR(localTime+pi*10,0,localTime))
    p.color= interpolate (time, forever (at (orange) + to (4,red) + to (4, blue)+ to (4,orange)))
    b.color= interpolate (time, forever (at (blue) + to (4,brown) + to (4, red)+ to (4,blue)))
    world.color=black
# This launches a panda:

#def launch(w, x):
#    p = panda(position = P3(localTime-2, 0,0 ),size=.5)
#def bounce(m, v):
#    p.v = -p.v.now() # v is the velocity
#    m.position = p.position.now() + P3(0, 0, p.v*(localTime))
#p=panda(position=P3(localTime-2,0,0))
#p.v=1
#p.when((getY(p.position) > 0) | (getY(p.position) < 4), bounce)
## This calls the launch every 2 seconds

# Note that there is no particular model reacting here - you can
# have "free floating" reactions.  The object associated with this is the
# "world" object.
react(c, launch)
# Change the step on the alarm - what happens?
# Can you make the panda spin as it moves?
# Add a second launcher that uses the mouse button to fire

start()