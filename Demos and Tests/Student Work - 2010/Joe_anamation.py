from Panda import *

c = alarm(start = 0, step = .1)
b = P3C(3, time, sin(time*3))
camera.position = P3(0,-20,5)
camera.hpr = HPR (0,0,time)

def launch(w, x):
    p = panda(position = P3(sin(localTime),0,cos(time)+(localTime*1)))
    db = deriv(P3(0,0,0), b)
    p.color = color(0,random01(),random01())
    p.hpr = HPR(0,-pi/2,0)

react(c, launch)

def launch(w, x):
    p = panda(position = P3(cos(localTime),0,sin(time)+(localTime*1)))
    p.color = color(random01(),0,random01())
    db = deriv(P3(0,0,0), b)
    p.hpr = HPR(0,-pi/2,0)

react(c, launch)

world.color = black
pointLight(position= P3(sin(localTime), cos(localTime), 0))
ambientLight(color = Color(1,1,1))


start()