from Panda import *

world.color=black
c = alarm(start = 0, step = .05)
def launch(w,x):
    b=panda(size=.2,position=P3C(2,localTime, localTime/4-3),hpr=HPR(localTime+pi*10,0,localTime))
    p=bunny(size=.4,position=P3C(-2,localTime,localTime/4-3),hpr=HPR(localTime+pi*10,0,localTime))
    p.color= interpolate (time, forever (at (orange) + to (4,red) + to (4, blue)+ to (4,orange)))
    b.color= interpolate (time, forever (at (blue) + to (4,brown) + to (4, red)+ to (4,blue)))


react(c, launch)


start()