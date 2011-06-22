from Panda import *

def f(x,y):
    return 
s = surface(f, xmin = -10, ymin = -10, xmax = 10, ymax = 10, texture = "diagnolColors.jpg")

b = soccerBall(size = .2)
rollSphere(b, s, 2, -2, 2, 1)

j = sphere(texture = "jupitermap.jpg", size = .2)
rollSphere(j, s, 0, 0, 0, 0)

camera.position = P3(0, 0, 20)
camera.hpr = HPR(0,1.5*pi,0)


start()