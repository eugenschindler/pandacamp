from Panda import *
# We've been limited by not being able to observe the old value of something like a position or hpr
# when computing the new value.  Within a reaction function, you can use .now() to get the current
# (constant) value of a signal like position or hpr.
sunset()
# Let's move a panda up and down from it's current location
text("type s to start, a and d to m")
hg = hangGlider()
# This takes the panda, looks at the current position,
# and starts going up from this position
r3 =russianBuilding(position=P3(0,0,-4.4),size=3)
#r3.score = static(1)
r5 =russianBuilding(position=P3(2.5,0,-4.4),size=3)
r1 = russianBuilding(position=P3(-2.5,0,-4.4),size=3)
r2 = russianBuilding(position=P3(-1.25,0,-4.4),size=3)
r4 =russianBuilding(position=P3(1.25,0,-4.4),size=3)

r1.score = static(1);
r2.score =static(1);
r3.score =static(1);
r4.score =static(1);
r5.score =static(1);

c= alarm(start=0,step=3)
gravity = P3(0,0,-5)

lives = var(5)
text(lives)

text(choose(lives > 0, "OMG Bunnies!", "Game Over"))

def goDown(hg, v):
    here = hg.position.now()
    hg.position = here + P3(0,0,-1.5)

def goLeft(hg, v):
    here = hg.position.now()
    hg.position = here + P3(-localTime*4.5,0,0)

def goRight(hg, v):
    here = hg.position.now()
    hg.position = here + P3(localTime*4,0,0)



hg.react1(key("s"), goDown)
hg.react(key("a"), goLeft)
hg.react(key("d"), goRight)

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(gravity)
    b.position = p0 + integral(b.velocity)

def bounceFloor(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = P3((random01()*2)-2, getY(v), -getZ(v))
    launch(m, p, v1)
    s=sound("boing.wav")
    s.play()

def bounce2(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = P3((random01()*2), getY(v), -getZ(v))
    launch(m, p, v1)
    s=sound("boing.wav")
    s.play()

def blowup(m,v):
    loc = float(getX(m.position).now())
    if (loc>1.5):
     if r5.score >0:
            r5.position = P3(100, 0, 0)
            r5.score =  0
            lives.sub(1);
    if (loc>.5) & (loc<=1.5):

        if r4.score >0:
            r4.position = P3(100, 0, 0)
            r4.score =  0
            lives.sub(1);
    if (loc>-.5) & (loc<=.5):

        if r3.score >0:
            r3.position = P3(100, 0, 0)
            r3.score =  0
            lives.sub(1);
    if (loc>-1.5) & (loc<=-.5):

        if r2.score >0:
            r2.position = P3(100, 0, 0)
            r2.score =  0
            lives.sub(1);
    if (loc<=-1.5):

        if r1.score >0:
            r1.position = P3(100, 0, 0)
            r1.score =  0
            lives.sub(1);



   # print loc
def lose1(m,l):
      if m.score >0:
            m.exit()
            m.score =  0
            l = l-1;


def newBall(m, v):
    p = bunny()
    p.size=.5
    launch(p, P3(random01()*6-3,0,2), P3(0,0, 0))
    p.when((getX(p.position) < -3) | (getX(p.position) > 3), byebye)
    p.when((getZ(p.position) < -1.3)& (getZ(p.position) > -1.5)& (getZ(p.velocity) < 0)&(getX(p.position)> getX(hg.position)-1)&(getX(p.position)<= getX(hg.position)), bounceFloor)
    p.when((getZ(p.position) < -1.3)& (getZ(p.position) > -1.5)& (getZ(p.velocity) < 0)&(getX(p.position)> getX(hg.position))&(getX(p.position)< getX(hg.position)+1), bounce2)
    p.when1((getZ(p.position) < -1.5),blowup)

react(c, newBall)

def byebye(m, v):
    m.exit()



start()