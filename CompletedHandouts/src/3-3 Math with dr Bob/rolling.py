from Panda import *

def f(x,y):
    if x < 0:
        return 0
    else:
        return x

s = surface(f, xmin = -1, ymin = -1, xmax = 1, ymax = 1, texture = "realpanda.jpg")

b = soccerBall(size = .1)

g = -9.8
x0 = .5
y0 = .5
xv0 = 1
yv0 = 0
drag = .3
setType(b.xpos, numType)
setType(b.ypos, numType)
setType(b.xv, numType)
setType(b.yv, numType)
setType(b.xa, numType)
setType(b.ya, numType)
dx = s.dx(b.xpos, b.ypos)
dy = s.dy(b.xpos, b.ypos)
den = (1 + dx*dx + dy*dy)
b.xa = g * dx/den - drag*b.xv
b.ya = g * dy/den - drag*b.yv
b.xv = integral(b.xa) + xv0    
b.yv = integral(b.ya) + yv0
b.xpos = integral(b.xv) + x0    
b.ypos = integral(b.yv) + y0


p = P3(b.xpos, b.ypos, s.f(b.xpos, b.ypos))
b.position = p

mouseControlCamera(camera)
start()