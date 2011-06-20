from Panda import *

def f(x,y):
    return (x*x + y*y)/10

s = surface(f, xmin = -1, ymin = -1, xmax = 1, ymax = 1, texture = "realpanda.jpg")

b = soccerBall(size = .1)
rollSphere(b, s, .5, .5, 1, 0)

j = sphere(texture = "jupitermap.jpg", size = .2)
rollSphere(j, s, -.5, .5, -1, 0)

mouseControlCamera(camera)


start()