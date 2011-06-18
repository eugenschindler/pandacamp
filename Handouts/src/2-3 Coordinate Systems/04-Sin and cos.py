from Panda import *

c = alarm(step = 1)

def launch(m,v):
    p = panda(position = P3C(cos(localTime)*2, sin(localTime)*2, sin(localTime)*2))
    pointForward(p)

react(c, launch)

camera.position = P3(cos(time)*15,sin(time)*15,0)
camera.hpr = HPR(pi/2+time,0,0)

grassScene()
start()
