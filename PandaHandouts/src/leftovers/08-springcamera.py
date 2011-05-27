import math
from Panda import *

grassScene()

#panda cams
#q = panda(size = .2, color = red)
#z = panda(size = .2)
#q = panda(size = .2, color = red)
w = panda(size = .2, color = blue)
#e = panda(size = .2, color = green)
#r = panda(size = .2, color = yellow)
#t = panda(size = .2, color = purple)
#y = panda(size = .2)
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
#qs = slider(position = P2(.95, .95), max = 2, init= .5, pageSize = 1)


#Fric slider
#fs = slider(position = P2(.1, .95), max = 0, min = -2,init= -.5, pageSize = 1)


#pancam sliders
#qs = Slider(position = P2(.95, .95), max = 2, init= .5, pageSize = 1)
ws = Slider(position = P2(.95, .85), max = 2, init= .5, pageSize = 1)
#es = Slider(position = P2(.95, .75), max = 2, init= .5, pageSize = 1)
#rs = Slider(position = P2(.95, .65), max = 2, init= .5, pageSize = 1)
#ts = Slider(position = P2(.95, .55), max = 2, init= .5, pageSize = 1)
#ys = Slider(position = P2(.95, .45), max = 2, init= .5, pageSize = 1)


#Fric slider
fs = Slider(position = P2(.1, .95), max = 0, min = -2,init= -.5, pageSize = 1)
text(fs.value)
text(ws.value)

##-2 .5

####################
#Every Panda can be given a unique equation, try some of your own.
####################
#def funcq(x,y):
#    return 1


#def funce(x,y):
#    return sqrt(x*x + y*y) * sqrt(x*x + y*y)
#
#def funcr(x,y):
#    return (x*x + y*y)
#
#def funct(x,y):
#    return 1 / (1+ sqrt(x*x + y*y))
#
#def funcy(x,y):
#    return (1+ sin(sqrt(x*x + y*y)/2))

def funcw(x,y):
    return sqrt(x*x + y*y)

def campan (h,j,f):
    setType(h.vel, P3Type)

    springLoc = p
    x = getX(springLoc-h.position)
    y = getY(springLoc-h.position)
    springK = j.value * (f(x,y))
    spring = springK * (springLoc - h.position)
    friction =  h.vel * fs.value
    force =  spring + friction
    h.vel = integral(force) + v0
    h.position = integral(h.vel) + q0
    pdif =runner.position - h.position
    vect = P3toHPR(pdif)
    h.hpr = HPR(getH(vect),0,0)

campan (w, ws, funcw)

#campan (q, qs, funcq)

#campan (e, es, funce)
#campan (r, rs, funcr)
#campan (t, ts, funct)
#campan (y, ys, funcy)



#setType(q.vel, P3Type)
#springLoc = runner.position
#
#spring = qs * (springLoc - q.position)
#friction = q.vel * fs
#force =  spring + friction
#q.vel = integral(force)
#q.position = integral(q.vel)
#pdif =runner.position - q.position
#vect = P3toHPR(pdif)
#q.hpr = HPR(getH(vect),0,0)



camera.position = choose(lbutton, P3((getX(w.position)),(getY(w.position)),1), P3 (0,0,35))
camera.hpr = choose(lbutton, HPR(getH(w.hpr)+radians(180),getP(w.hpr),0), HPR(0, 3*pi/2,0))



start()