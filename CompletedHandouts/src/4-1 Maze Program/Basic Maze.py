
from Panda import *



grassScene()

#def wall_X(x,y):
#        return mazeCube(x, y, color(0, random01(),random01()))

def open_b(x,y):
        return bunny(position = P3(x+.5,y+.5,0),size=.5)

def open_j(x,y):
        return jeep(position = P3(x+.5,y+.5,0),size=.5)

m2 = Maze("maze.txt", __name__)

thing = find1InMaze(m2,"b")
#for b in thing:
thing.hpr = HPR(time,0,0)


p0 = P3(1.5,1.5,0)

#key commands
s = hold(0, tag(.2, key("arrow_up")) +
             tag(-.2, key("arrow_down")))


h = hold(0, tag(.2, key("arrow_left")) +
                tag(-.2, key("arrow_right")))

dir = integral(h)
speed = s
text(speed)
text(dir)
v = P3C(speed, dir,0)
hpr = HPR(dir,0,0)

camera.hpr = hpr + HPR(-pi/2, 0, 0)
camera.position = integral(v) + p0


#camera.position = P3(5, 5, 20)
#camera.hpr = HPR(0, -pi/2, 0)

start()
