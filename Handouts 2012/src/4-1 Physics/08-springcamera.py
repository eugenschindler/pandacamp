

import math
from Panda import *

grassScene()

#panda cams
q = panda(size = .2, color = red)
z = panda(size = .2)
z.position = P3 (0,0,70)
z.HPR = HPR(pi, 3*pi/2,0)

#sonic
#runner = sonic()
runner = panda()
#other cars
#q0 = P3(0,0,0)
p0 = P3(0,0,0) # initial position
v0 = P3(0,0,0) # initial velocity

#key commands
v = hold(v0, key("arrow_left", P3(-3, 0, 0)) +
             key("arrow_down", P3(0, -3, 0)) +
             key("arrow_up", P3(0, 3, 0)) +
             key("arrow_right", P3(3, 0, 0)) +
             key("space", P3(0, 0, 0)))


#sonic vars
p = p0 + integral(v) # initial position
runner.position = p # set the position
hpr = P3toHPR(v) # set hpr using arrows
runner.hpr = HPR(getH(hpr), getP(hpr), 0) # no rolling!

#camera sliders
#spring constant slider
qs = slider(label = "Spring Constant", position = P2(.95, .95), max = 2, init= .5, pageSize = 1)
#friction slider
fs = slider(label = "Friction", position = P2(.1, .95), max = 0, min = -2,init= -.5, pageSize = 1)


setType(q.vel, P3Type) # circular logic - prevents type inference issues
#springLoc = runner.position # initial position of the spring
springLoc = -3*HPRtoP3(runner.hpr) + runner.position

#springLoc = 

spring = qs * (springLoc - q.position) # force of spring = spring constant * spring vector
#friction = q.vel * fs # force that pushes against motion of camera - this is absolut
friction = (q.vel - integral(v)) * fs # force that pushes against motion of camera - this is relative
force =  spring + friction # total force on camera = sum of forces
q.vel = integral(force) # turn force into position
q.position = integral(q.vel)
pdif =runner.position - q.position # controls cameras hpr
vect = P3toHPR(pdif)
q.hpr = HPR(getH(vect),0,0)

# camera position
camera.position = choose(lbutton, P3((getX(q.position)),(getY(q.position)),1), P3 (0,0,35))
camera.hpr = choose(lbutton, HPR(getH(q.hpr)+radians(180),getP(q.hpr),0), HPR(0, 3*pi/2,0))


start()
