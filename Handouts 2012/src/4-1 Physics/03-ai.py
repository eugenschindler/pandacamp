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


camera.position = P3(5, 5, 20)
camera.hpr = HPR(0, -pi/2, 0)

def randomStrategy(s, openings, loc):
    if len(openings) > 1:
         openings = openings[0:len(openings)-1]
    r = randomChoice(openings)
    return (s, r)

p = panda(size = .3, color = red)
mazeStrategy(p, myMaze, randomStrategy, 10, 0, (1, 1))
start()
