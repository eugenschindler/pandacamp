from Panda import *
camera.position=P3(0,-50, 6)


balls = collection()

targets = collection()
targets.add(panda(position = P3(5,0,6),size = 2))
targets.add(panda(position = P3(-5,0,6), size = 2))
targets.add(panda(position = P3(sin(time/2) * 5, 5, (cos(time/2) * 5) + 6), size = 2))

# grassScene(position = P3(0,10,0), scale = 0.1)

#initial position and velocity for the first ball and the second ball.

gravity = P3(0,0,-25)

floor = 0
wallRight = 10
wallLeft = -10
wallDepth = 50

### Sets up the rectangles for reference.

br = 1 #Ball Radius
lowerLeft = P3(wallLeft-br,-wallDepth,0)
lowerRight = P3(wallRight+br,-wallDepth,0)
backLeft = P3(wallLeft-br,wallDepth,0)

floorRect = rectangle(lowerLeft,lowerRight,backLeft,blue)

### End of the reference rectangles.

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(gravity)
    b.position = p0 + integral(b.velocity)

def newBall(m, v):
    xdir = 10*getX(mouse.now())
    ydir = 10*getY(mouse.now())+15
    b = soccerBall(size = .6)
    b.when(getZ(b.position) < 1, disapear)
    balls.add(b)
    launch(b, P3(0,-40,4), P3(xdir,40, ydir))

def h(m,e):
    for p in e:
        (b,t) = p  
        lastFor(2, explosions(position=b.position.now()))
        lastFor(2, explosions(position=t.position.now()))
        b.exit()
        t.exit()
        

def disapear(b,v):
    explosion(position=b.position.now())
    balls.remove(b)
    b.exit()

react(lbp, newBall)
react(hit(balls, targets),h)

start()