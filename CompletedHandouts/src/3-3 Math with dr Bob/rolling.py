from Panda import *

def f(x,y):
    return x*x + y*y

s = surface(f, xmin = -1, ymin = -1, xmax = 1, ymax = 1, dx = .1, dy = .1, texture = "realpanda.jpg")

b = ball(size = .1)

g = -9.8
x0 = .5
y0 = .5
xv0 = 0
yv0 = 0
b = 0
p = P3()

xa = g * s.parX(p)/(1 + parX(f, p)*parX(f, p) + parY(f, p) * parY(f, p))
xv = integral(xa) + xv0    
yv = integral(ya) + yv0
xpos = integral(xv) + x0    
ypos = integral(yv) + y0


p = P3(xPos, yPos, s.f(xPos, yPos))
ball.position = p

mouseControlCamera(camera)
start()