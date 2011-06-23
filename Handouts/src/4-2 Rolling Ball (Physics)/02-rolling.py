from Panda import *

def f(x,y):
    return (sin(x)+cos(y))*3
def death(m,v):
    lastFor(4,fireish(position = m.position.now()))
    
s = surface(f, xmin = -10, ymin = -10, xmax = 10, ymax = 10, texture = "diagnolColors.jpg")

b = soccerBall(size = .2)
rollSphere(b, s, 2, -2, 2, 1)

j = sphere(texture = "jupitermap.jpg", size = .2)
rollSphere(j, s, 0, 0, 5, 6)

goal=sphere(texture = "venusmap.jpg", size = .5,position = P3(3, 4, f(3,4)+1))
goal.react1(hit(goal,b),death)
goal.react1(hit(goal,j),death)


camera.position = P3(0, 0, 20)
camera.hpr = HPR(0,1.5*pi,0)


start()