from Panda import *

# The "alarm" function generates an event at regular
# intervals - use "start=" and "step=" to control the timing.
c = alarm(start = 0, step = 2)
c1 = alarm(start = 9, step = 2)
c2 = alarm(start = 18, step = 2)

camera.position = P3(0, -16, 0)
camera.hpr = HPR(0, 0, 0)
world.color = orange
pl=pointLight(position=P3(5,-5,-5),color=black)
# This launches a panda:
#p = hangGlider(position =P3(0,0,0))


def launch(m, x):
   
    p = hangGlider(position = P3C(cos(pi/2)*localTime/10, sin(pi/2)*localTime*3,localTime/10-2 ),size=.2,hpr=HPR(localTime+pi,0,localTime))
    p1 = hangGlider(position = P3C(-localTime/10, localTime*3,localTime/10-2 ),size=.2,hpr=HPR(localTime+pi,0,localTime))
    p2 = hangGlider(position = P3C(localTime/10, localTime*3,localTime/10-2 ),size=.2,hpr=HPR(localTime+pi,0,localTime))

def launch1(m, x):
    p = boeing707(position = P3C(cos(pi/2)*localTime/10, sin(pi/2)*localTime*3,localTime/10-1),size=.2,hpr=HPR(localTime+pi,0,localTime))
    p1 = boeing707(position = P3C(-localTime/10, localTime*3,localTime/10-1 ),size=.2,hpr=HPR(localTime+pi,0,localTime+2))
    p2 = boeing707(position = P3C(localTime/10, localTime*3,localTime/10-1),size=.2,hpr=HPR(localTime+pi,0,localTime+2))

def launch2(m, x):
    p = boyBalloon(position = P3C(cos(pi/2)*localTime/10, sin(pi/2)*localTime*3,localTime/10 ),size=.6,hpr=HPR(localTime+pi,0,localTime))
    p1 = boyBalloon(position = P3C(-localTime/10, localTime*3,localTime/10),size=.6,hpr=HPR(localTime+pi,0,localTime+4))
    p2 = boyBalloon(position = P3C(localTime/10, localTime*3,localTime/10 ),size=.6,hpr=HPR(localTime+pi,0,localTime+4))

#    p.when((getY(p.position) > -2), launch(p.position))


#    p3 = hangGlider(position = P3C(-localTime/10, localTime*3,localTime/10-2 ),size=.2,hpr=HPR(localTime+pi,0,localTime))
#    p4 = hangGlider(position = P3C(localTime/10, localTime*3,localTime/10-2 ),size=.2,hpr=HPR(localTime+pi,0,localTime))
#    p5 = hangGlider(position = P3C(-localTime/10, localTime*3,localTime/10-2 ),size=.2,hpr=HPR(localTime+pi,0,localTime))
# This calls the launch every 2 seconds

# Note that there is no particular model reacting here - you can
# have "free floating" reactions.  The object associated with this is the
# "world" object.
react(c, launch)
react(c1, launch1)
react(c2, launch2)

# Change the step on the alarm - what happens?
# Can you make the panda spin as it moves?
# Add a second launcher that uses the mouse button to fire

start()