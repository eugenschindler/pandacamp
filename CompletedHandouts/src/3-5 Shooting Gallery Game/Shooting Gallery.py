from Panda import *

camera.position=P3(0,-50, 6)


balls = collection()

targets = collection()
targets.add(panda(position = P3(5,0,6),size = 2))
targets.add(panda(position = P3(-5,0,6), size = 2))

# grassScene(position = P3(0,10,0), scale = 0.1)

#initial position and velocity for the first ball and the second ball.

gravity = P3(0,0,-25)

floor = 3
wallRight = 10
wallLeft = -10

### Sets up the rectangles for reference.
wallDepth = 20
br = 1 #Ball Radius
lowerLeft = P3(wallLeft-br,-wallDepth,floor-br)
lowerRight = P3(wallRight+br,-wallDepth,floor-br)
backLeft = P3(wallLeft-br,wallDepth,floor-br)

floorRect = rectangle(lowerLeft,lowerRight,backLeft,blue)

### End of the reference rectangles.

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(gravity)
    b.position = p0 + integral(b.velocity)

def reflectFloor(b,v):
   p1 = b.position.now()
   v1 = b.velocity.now()
   p0 = P3(p1.x, p1.y, 2*floor-p1.z)
   v0 = P3(v1.x, v1.y, -.94*v1.z)
   launch(b, p0, v0)

def newBall(m, v):
    xdir = 10*getX(mouse.now())
    ydir = 10*getY(mouse.now())+15
    b = soccerBall(size = .6)
    balls.add(b)
    launch(b, P3(0,-40,4), P3(xdir,40, ydir))

def h(m,e):
    (b,t) = e
    b.exit()
    t.exit()

def disapear(b,v):
    balls.remove(b)
    print "Bang!"
    b.exit()

react(lbp, newBall)
#react(hit(balls, targets),h)


start()