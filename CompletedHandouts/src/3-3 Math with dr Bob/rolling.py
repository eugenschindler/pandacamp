from Panda import *

def f(x,y):
    return sin(x)+cos(y)
s = surface(f, xmin = -5, ymin = -5, xmax = 5, ymax = 5, texture = "realPanda")

b = soccerBall(size = .1)
rollSphere(b, s, .5, .5, 1, 0)

j = sphere(texture = "jupitermap.jpg", size = .2)
rollSphere(j, s, .5, .5, 2, 0)

camera.position = P3(0, 0, 20)
#camera.position = sliderP3()
#$camera.hpr = sliderHPR()
camera.hpr = HPR(0,1.5*pi,0)


start()