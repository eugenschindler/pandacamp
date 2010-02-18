import math
from Panda import *

grassScene()

#panda cams
q = panda(size = .2, color = red)
z = panda(size = .2)
z.position = P3 (0,0,70)
z.HPR = P3(pi, 3*pi/2,0)

#script = loadScript("script.csv")



#sonic
runner = sonic()

#other cars
q0 = P3(0,0,0)
p0 = P3(0,0,0)
v0 = P3(0,0,0)

#key commands
v = hold(v0, tag(P3(-3, 0, 0), key("a")) +
             tag(P3(0, -3, 0), key("s")) +
             tag(P3(0, 3, 0), key("w")) +
             tag(P3(3, 0, 0), key("d")) +
             tag(P3(0, 0, 0), key("h")))


#sonic vars
p = p0 + integral(v)
dir = deriv(P3(0,0,0), p)
runner.position = p
hpr = P3toHPR(dir)
runner.hpr = HPR(getH(hpr), getP(hpr), 0)
#runner.control = interpolate(time, cycle(-1,script["walking"]))

#pancam sliders
qs = slider(position = P2(.95, .95), max = 2, init= .5, pageSize = 1)


#Fric slider
fs = slider(position = P2(.1, .95), max = 0, min = -2,init= -.5, pageSize = 1)





setType(q.vel, P3Type)
springLoc = runner.position

spring = qs * (springLoc - q.position)
friction = q.vel * fs
force =  spring + friction
q.vel = integral(force)
q.position = integral(q.vel)
pdif =runner.position - q.position
vect = P3toHPR(pdif)
q.hpr = HPR(getH(vect),0,0)



camera.position = choose(lbutton, P3((getX(q.position)),(getY(q.position)),1), P3 (0,0,35))
camera.hpr = choose(lbutton, HPR(getH(q.hpr)+radians(180),getP(q.hpr),0), HPR(0, 3*pi/2,0))



start()