
# Measuring distance using "dist"
from Panda import *

p1 = P3(-4,0,2.2)
v1 = P3(1,0,0)#+P3C(0,pi/4,0)
p2 = P3(4,0,2.2)
v2 = P3(-1, 0,0)

count = 0


    #j = random.randint(-4,4)
    #k = random.randint(-4,4)
    #panda(position = P3(i,j,k), hpr = HPR(i,j,k))

def dropPanda(m,v):
    p=panda(size=.2)
    launch(p,m.position.now()-P3(0,0,.4),P3(0,0,0),P3(0,0,-1.5))
    p.react1(leftClick(p), point)
def launch(b, p0, v0, a):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(a)
    b.position = p0 + integral(b.velocity)
def point(m,v):
    explosion(position = m.position.now(),color=color(random01(),random01(),random01())) #,color = color(random01(),random01(),random01()))
    m.exit()
    score.add(nextScore.now())  # Score whatever the current score is
    #nextScore.set(0)            # Prevent scoring twice at the same position
def spaz(m,v):
    world.color=interpolate(time,forever(at(blue)+to(.05,green)+to(.05,orange)+to(.05,red)+to(.05,blue)))
    #p=boeing707(position=P3(0,0,0),hpr=HPR(time*100000,0,0),size=.5)
##def pandaLine(number, place,p):
#    if number > 0:
#        p1=panda(position=place,hpr=HPR(0,p,0))
#        p1.color=interpolate(time+number,forever(at(blue)+to(.01,red)+to(.01,orange)+to(.01,brown)+to(.01,green)))
#        pandaLine(number-1,place+P3(1,0,0),p+.3)
def explode(m,v):
    #explosions(position=m1.position.now())
    warpFace(position=P3(10,0,0),texture='fire1.png')
    world.color=orange
    fireish(position=P3(-5,0,-3))
    fireish(position=P3(-4,0,-3))
    fireish(position=P3(-3,0,-3))
    fireish(position=P3(-2,0,-3))
    fireish(position=P3(-1,0,-3))
    fireish(position=P3(0,0,-3))
    fireish(position=P3(1,0,-3))
    fireish(position=P3(2,0,-3))
    fireish(position=P3(3,0,-3))
    fireish(position=P3(4,0,-3))
    fireish(position=P3(5,0,-3))
#    fireish(position=P3(1,-3,-2))
#    fireish(position=P3(-1,-3,-2))
#    m1.exit()
#    m2.exit()

delay=.01
delay1=.1
def plane(m,v):
    global delay
    m1 = boeing707(position = p1 + v1*localTime*2,hpr=HPR(pi/2,0,0))
    i = random01()*6-2
    m1.when1(abs(m1.position-P3(i,0,2.2))<2,dropPanda)
    delay=random01()*2+1
    #delay1=random01()*2
    react1(localTimeIs(delay),plane)
    #react1(localTimeIs(delay1),e)
    #print "hello"
world.color=black
score = var(0)     # Score
nextScore = var(1) # How much to score
text(score)
react(key('a'),explode)
react(key('s'),spaz)
#pandaLine(10, P3(-5,0,3),time*3)
#m2 = soccerBall(position = p2 + v2*time)
#likeFountainWater(position=p1+v1*time)
#likeFountainWater(position=p2+v1*time)
# Display the distance between the balls using "text"
#c = alarm(start = 0, step = 1)
#react(c,plane)
react1(localTimeIs(delay),plane)
start()

