# To change this template, choose Tools | Templates
# and open the template in the editor.

from Panda import *
wallUp = []
wallLeft = []
for i in range(30):
    row = []
    row1 = []
    for j in range(30):
        row.append([])
        row1.append([])
    wallUp.append(row)
    wallLeft.append(row1)


def readMaze(f):
    fileLoader = open(f,  "r")
    contents = fileLoader.read().split("\n")
    x = 0
    y = 0
    top = True
    for l in contents:
        y = 0
        if top:
            for c in l:
                if (y % 2 == 1):
                    wallUp[x/2][y/2] = c == "-"
                y = y + 1
        else:
            for c in l:
                if (y % 2 == 0):
                    wallLeft[x/2][y/2] = c == "|"
                y = y + 1
        x = x + 1
        top = not top

readMaze("maze.txt")

def moveRight(m):
    m.position = interpolate(localTime, at(P3(m.x1, m.y1, 0)) + to(1, P3(m.x1+1, m.y1, 0)))
    m.react1(localTimeIs(1), chooseMove)
    m.x1 = m.x1 + 1

def moveLeft(m):
    m.position = interpolate(localTime, at(P3(m.x1, m.y1, 0)) + to(1, P3(m.x1-1, m.y1, 0)))
    m.react1(localTimeIs(1), chooseMove)
    m.x1 = m.x1 - 1

def moveUp(m):
    m.position = interpolate(localTime, at(P3(m.x1, m.y1, 0)) + to(1, P3(m.x1, m.y1+1, 0)))
    m.react1(localTimeIs(1), chooseMove)
    m.y1 = m.y1 + 1

def moveDown(m):
    m.position = interpolate(localTime, at(P3(m.x1*-1, m.y1, 0)) + to(1, P3(m.x1, m.y1-1, 0)))
    m.react1(localTimeIs(1), chooseMove)
    m.y1 = m.y1 - 1

def chooseMove(m, v):
    n = 200
    while (n > 0):
        i = randomInt(4)
        print "i: ", i
        print wallUp
        if i == 0 and not wallUp[m.x1][m.y1]:
            print "up"
            moveUp(m)
            return
        elif i == 1  and not wallUp[m.x1][m.y1+1]:
            print "down"
            moveDown(m)
            return
        elif i == 2 and not wallLeft[m.x1][m.y1]:
            print "left"
            moveLeft(m)
            return
        elif i == 3 and not wallLeft[m.x1+1][m.y1]:
            print "right"
            moveRight(m)
            return
        n = n - 1
        print "Stuck!"

for i in range(30):
    for j in range(30):
        if wallUp[i][j]:
            rectangle(P3(i,j, 0), P3(i, j+1, 0), P3(i,j,1), color(0, random01(), random01()))
        if wallLeft[i][j]:
            rectangle(P3(i,j, 0), P3(i+1, j, 0), P3(i,j,1), color(0, random01(),random01()))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
p.x1 = static(0)
p.y1 = static(0)
#camera.position = P3(getX(mouse)*3, getY(mouse)*3, .4)
h = integral(getX(mouse))
speed = P3C(getY(mouse)+1, -h, 0)
camera.position = P3(3.5, 3.5,.4) + integral(speed)

camera.hpr = P3toHPR(speed)+ HPR(pi, 0, 0)
left = move(1, P3(1,0,0))
right = move(1, P3(-1, 0, 0))
up = move(1, P3(0, -1, 0))
down = move(1, P3(0, 1, 0))
# p.position = itime(at(P3(.5, .5, 0)) + left + left + down + down + right)


#p.react(key("d"), moveRight)
#p.react(key("a"), moveLeft)
#p.react(key("s"), moveDown)
#p.react(key("w"), moveUp)

start()
