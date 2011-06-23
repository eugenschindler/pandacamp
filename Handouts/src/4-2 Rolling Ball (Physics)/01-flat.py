from Panda import *

def f(x,y):
    return 0

surface(f, xmin = -10, ymin = -10, xmax = 10, ymax = 10, dx = 10, dy = 10, texture = "realpanda.jpg")
b = soccerBall(size = .5)
p = P2(0,0)


mouseControlCamera(camera)
start()