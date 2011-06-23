from Panda import *


def wall_X(x,y):
        return mazeCube(x, y, color(0, random01(),random01()))

def open_b(x,y):
        return bunny(position = P3(x+.5,y+.5,0),size=.5)

def open_j(x,y):
        return jeep(position = P3(x+.5,y+.5,0),size=.5)

def open_p(x, y):
    return panda(position = P3(x+.5,y+.5,0),size=.3)

myMaze = maze("maze.txt", __name__)

runner = find1InMaze(myMaze, "p")
runner.color = blue


#key commands
s = hold(0, tag(1, key("arrow_up")) +
             tag(-1, key("arrow_down")))


h = hold(0, tag(1, key("arrow_left")) + tag(0, keyUp("arrow_left")) +
                tag(-1, key("arrow_right")) + tag(0, keyUp("arrow_right")))

dir = integral(h)
speed = s
v = P3C(speed, dir,0)
hpr = HPR(dir,0,0)


p = panda(size = .4)
p.hpr = HPR(dir+pi/2, 0, 0)
moveInMaze(p, myMaze, P3(1.5, 1.5, 0), v)

camera.position = P3(5, 5, 20)
camera.hpr = HPR(0, -pi/2, 0)

#camera.hpr = hpr + HPR(-pi/2, 0, 0)
#camera.position = integral(v) + p0

start()
