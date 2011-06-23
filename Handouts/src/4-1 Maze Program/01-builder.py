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

thing = findInMaze(myMaze,"b")
for b in thing:
    b.hpr = HPR(time,0,0)

runner = find1InMaze(myMaze, "p")
runner.color = blue


camera.position = P3(5, 5, 20)
camera.hpr = HPR(0, -pi/2, 0)

start()
