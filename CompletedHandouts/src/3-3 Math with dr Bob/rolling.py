from Panda import *

def f(x,y):
    return x*x + y*y

surface(f, xmin = -1, ymin = -1, xmax = 1, ymax = 1, dx = .01, dy = .01, texture = "realpanda.jpg")


mouseControlCamera(camera)
start()