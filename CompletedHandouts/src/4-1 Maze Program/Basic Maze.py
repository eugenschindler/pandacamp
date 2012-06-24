# Basic Maze.py
from Panda import *



grassScene()

def wall_X(x,y):
        return mazeCube(x, y, color(0, random01(),random01()))

def open_b(x,y):
        return bunny(position = P3(x+.5,y+.5,0),size=.5)

def open_j(x,y):
        return jeep(position = P3(x+.5,y+.5,0),size=.5)

m2 = Maze("maze.txt", __name__, green)


p0 = P3(1.5,1.5,.5)

#key commands
speed = hold(0.0, key("arrow_up", 2) + keyUp("arrow_up", 0)+ 
                  key("arrow_down", -2) + keyUp("arrow_down", 0))


heading = hold(0.0, key("arrow_left", 2) + keyUp("arrow_left", 0) + 
                    key("arrow_right", -2)+keyUp("arrow_right", 0))

dir = integral(heading)
text(speed)
text(dir)
v = P3C(speed, dir,0)
hpr = HPR(dir,0,0)

#camera.hpr = hpr + HPR(-pi/2, 0, 0)
#camera.position = integral(v) + p0
# To put the camera up above use stuff like this instead
camera.position = P3(5, 5, 20)
camera.hpr = HPR(0, -pi/2, 0)

start()
