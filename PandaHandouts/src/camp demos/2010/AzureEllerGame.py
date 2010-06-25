from Panda import *
score = var(0)
restart = var(False)
text(score, size=2,position=P3(0,0,0))
print "Dodge the flying monkeys, if you get hit, click the Right Mouse Button to restart"
j=jeep(position=P3(0,0,-2.5),size=.5)
def zkey(p, v):
    j.position=j.position.now()+P3(-.5,0,0)

j.react(key('z'),zkey)


def xkey(p, v):
    if j.position<3:
        j.position=j.position.now()+P3(.5,0,0)
j.react(key('x'),xkey)

delta = 1
fire = 0
c = alarm(start = 0, step =1 )
leveltimer=alarm(start=0,step=5)
def setlevel(m,v):
    c.step=1.0/(time.now()+1)
    print "adjust level"
def endLevel(m, v):
    global fire
    fire = fireish(position = j.position.now())
    j.color = black
    restart.set(True)
    
    
react(leveltimer,setlevel)
def launch(m, v):
    print "Launch!"
    print restart.now()
    if not restart.now():
        print "Not restarted"
        global delta
        g = gorilla (position = P3(random01()*6-3, 0,4-localTime ),size= .2)
        print "drop"
        delta = delta * .99
        g.when1(restart, byebye)
        g.when1(getZ(g.position) < -3, scoreMe)
        g.when1(abs(g.position - j.position)<.4, endLevel)
        react1(localTimeIs(delta), launch)
    
react1(localTimeIs(delta), launch )

def scoreMe(m, v):
    score.add(1)
    m.exit()

def byebye(m, v):
    m.exit()

def restartGame(m, v):
    print  restart.now()
    if restart.now():
        global delta
        delta = 1
        fire.stop()
        jeep.color = white
        restart.set(False)
        print restart.now()
        launch(m, v)

react(lbp, restartGame)

#def collision(m,m2):



# react(c, launch)

    
    
start()
        
