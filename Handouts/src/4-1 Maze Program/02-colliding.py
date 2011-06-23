from Panda import *
score = var(0)
text(score)

p = panda(size = .4)
def hitB(m,v):
    #explosion(position=m.position.now())
    score.add(1)
    m.exit()

def hitJ(m,v):
    #explosion(position=m.position.now())
    score.add(-1)
    panda(position = m.position,size = .5,color = red)
    m.exit()


def wall_X(x,y):
    return mazeCube(x, y, color(0, random01(),random01()))

def open_b(x,y):
    b = bunny(position = P3(x+.5,y+.5,0),size=.5)
    b.react(hit(b,p),hitB)
    return b

def open_j(x,y):
    j = jeep(position = P3(x+.5,y+.5,0),size=.5)
    j.react(hit(j,p),hitJ)
    return j

def open_p(x, y):
    p = panda(position = P3(x+.5,y+.5,0),size=.3)
    p.x = static(x)
    p.y = static(y)
    return p

myMaze = maze("maze.txt", __name__,red)





#key commands
s = hold(0, tag(1, key("arrow_up")) + tag(0, keyUp("arrow_up")) +
             tag(-1, key("arrow_down")) + tag(0, keyUp("arrow_down")))


h = hold(0, tag(1, key("arrow_left")) + tag(0, keyUp("arrow_left")) +
                tag(-1, key("arrow_right")) + tag(0, keyUp("arrow_right")))

dir = integral(h)
speed = s
v = P3C(speed, dir,0)
hpr = HPR(dir,0,0)



p.hpr = HPR(dir+pi/2, 0, 0)
moveInMaze(p, myMaze, P3(1.5, 2.5, 0), v)

camera.position = P3(5, 5, 30)
camera.hpr = HPR(0, -pi/2, 0)



start()
