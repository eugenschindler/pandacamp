from Panda import *

ball = soccerball()

ball2 = soccerball()
# grassScene(position = P3(0,10,0), scale = 0.1)

camera.position=P3(0,-50, 6)

#initial position and velocity for the first ball and the second ball.
ballv0 = P3(2,1,3)
ballp0 = P3(0,0,1)
ball2v0 = P3(3.5,0,5)
ball2p0 = P3(1,0,6)
a = P3(0,0,-30)

floor = 3
wallRight = 10
wallLeft = -10

### Sets up the rectangles for reference.
wallDepth = 10
br = 1 #Ball Radius
lowerLeft = P3(wallLeft-br,-wallDepth,floor-br)
lowerRight = P3(wallRight+br,-wallDepth,floor-br)
backLeft = P3(wallLeft-br,wallDepth,floor-br)
backRight = P3(wallRight+br,wallDepth,floor-br)
frontLeft = P3(wallLeft-br,-wallDepth,15)
frontRight = P3(wallRight+br,-wallDepth,15)
leftRect = rectangle(lowerLeft,frontLeft,backLeft,red)
floorRect = rectangle(lowerLeft,lowerRight,backLeft,blue)
rightRect = rectangle(lowerRight,frontRight,backRight,green)
### End of the reference rectangles.

def addReflect(b):
    b.when(getZ(b.position) < floor, reflectFloor)
    b.when(getX(b.position) > wallRight, reflectRight)
    b.when(getX(b.position) < wallLeft, reflectLeft)

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(a)
    b.position = p0 + integral(b.velocity)

def reflectFloor(b):
   p1 = b.position.now()
   v1 = b.velocity.now()
   p0 = P3(p1.x, p1.y, 2*floor-p1.z)
   v0 = P3(v1.x, v1.y, -1.1*v1.z)
   launch(b, p0, v0)

def reflectRight(b):
   p1 = b.position.now()
   v1 = b.velocity.now()
   p0 = P3(2*wallRight-p1.x, p1.y, p1.z)
   v0 = P3(-v1.x, v1.y, v1.z)
   print "Reflecting right"
   launch(b, p0, v0)

def reflectLeft(b):
   p1 = b.position.now()
   v1 = b.velocity.now()
   p0 = P3(2*wallLeft-p1.x, p1.y, p1.z)
   v0 = P3(-v1.x, v1.y, v1.z)
   print "Reflecting left"
   launch(b, p0, v0)


addReflect(ball)
addReflect(ball2)

launch(ball, ballp0, ballv0)
launch(ball2, ball2p0, ball2v0)

start()