from Panda import *
from math import * 

def f(x,y):
    return math.exp(x*y)+sin(y)+cos(x)
s = surface(f, xmin = -15, ymin = -15, xmax = 10, ymax =10, texture = "diagnolColors.jpg")

b = soccerBall(size = .2)
rollSphere(b, s, -8, -1, 2, 2)

j = sphere(texture = "jupitermap.jpg", size = .2)
rollSphere(j, s, 0, 0, 0, 0)

camera.position = P3(.5, -1, 40)
camera.hpr = HPR(0,-.5*pi,0)

start()