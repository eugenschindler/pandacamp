from Panda import *

# The "alarm" function generates an event at regular
# intervals - use "start=" and "step=" to control this.
c = alarm(start = 0, step = 2)
def exit(m, v):
    m.exit()
def exit1(m, v):
    m.exit()
def fp(p0, dir,myhpr):
    p = panda(position = p0 + localTime * dir, hpr = myhpr)
    p.size = interpolate(localTime, at(1)+ to(2, 0))
    p.react(localTimeIs(2), exit1)
def endexp(m, v):
    m.stop()
def byebye(m, v):
    e = fireish(position = m.position.now(),size=7)
    e.react(localTimeIs(.2), endexp)
    p = m.position.now()
    fp(p, P3(2,3,3.5),HPR(1,6,time*3))
    fp(p, P3(-2.7,0,3),HPR(sin(time)*8,1,5))
    fp(p, P3(1.1,-5,.5),HPR(0,time*5,pi))
    fp(p, P3(5,1,-5),HPR(time,sin(time),time*10))
    fp(p, P3(-3.6,0,-2.3),HPR(sin(time),0,localTime*20))
    fp(p, P3(-5,.6,0),HPR(0,sin(time),time*10))
    fp(p, P3(8.1,1.5,1),HPR(sin(time),9,0))
    m.exit()
   
    # Write a function to create a new bear and send it
    # moving right across the screen.  Use "localTime"
    # to create your motion.
def launch(w, x):
    p = panda(position = P3(0, time/10,0 ), hpr = HPR(0,time,localTime))
    p.react(localTimeIs(30), exit)
    p.react(timeIs (30), byebye)


# This calls the launch every 2 seconds

# Note that there is no particular model reacting here - you can
# have "free floating" reactions.  The object associated with this is the
# world object.

react(c, launch)
# Can you make the panda spin as it moves?
# Add a second launcher that uses the mouse button to fire

start()