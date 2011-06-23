from Panda import *

def f(x,y):
    return (x*x - y*y)/5 + cos(x-.1)*5
def death(m,v):
    fireish(position = m.position.now())
    m.exit()
s = surface(f, xmin = -15, ymin = -15, xmax = 15, ymax = 15, texture = "diagnolColors.jpg")

b = soccerBall(size = .2)
rollSphere(b, s, 1, .1, 2, 0)

j = sphere(texture = "jupitermap.jpg", size = .3)
rollSphere(j, s, -10, 0, 8, 0)



camera.position = P3(0, 0, 50)
camera.hpr = HPR(0,1.5*pi,0)

goal=sphere(texture = "venusmap.jpg", size = .5,position = P3(3, 2, f(3,2)+2))
goal.react1(hit(goal,b),death)
goal.react1(hit(goal,j),death)

start()