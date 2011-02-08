# To change this template, choose Tools | Templates
# and open the template in the editor.

from Panda import *
wallUp = []
wallLeft = []


a = []
for i in xrange(15):
    a.append([])
    for j in xrange(15):
           a[i].append(i+j)




def readMaze(f):
    fileLoader = open(f,  "r")
    contents = fileLoader.read().split("\n")
    x = 0
    y = 0
    
    for l in contents:
        x = 0
        for c in l:
            if c == "x":
                a[x][y] = c
            x = x + 1

        y = y + 1
        

readMaze("maze.txt")

#def moveRight(m):
#    m.position = interpolate(localTime, at(P3(m.x1, m.y1, 0)) + to(1, P3(m.x1+1, m.y1, 0)))
#    m.react1(localTimeIs(1), chooseMove)
#    m.x1 = m.x1 + 1

#def moveLeft(m):
#    m.position = interpolate(localTime, at(P3(m.x1, m.y1, 0)) + to(1, P3(m.x1-1, m.y1, 0)))
#    m.react1(localTimeIs(1), chooseMove)
#    m.x1 = m.x1 - 1
#
#def moveUp(m):
#    m.position = interpolate(localTime, at(P3(m.x1, m.y1, 0)) + to(1, P3(m.x1, m.y1+1, 0)))
#    m.react1(localTimeIs(1), chooseMove)
#    m.y1 = m.y1 + 1
#
#def moveDown(m):
#    m.position = interpolate(localTime, at(P3(m.x1*-1, m.y1, 0)) + to(1, P3(m.x1, m.y1-1, 0)))
#    m.react1(localTimeIs(1), chooseMove)
#    m.y1 = m.y1 - 1
#
#def chooseMove(m, v):
#    n = 200
#    while (n > 0):
#        i = randomInt(4)
#        print "i: ", i
#        print wallUp
#        if i == 0 and not wallUp[m.x1][m.y1]:
#            print "up"
#            moveUp(m)
#            return
#        elif i == 1  and not wallUp[m.x1][m.y1+1]:
#            print "down"
#            moveDown(m)
#            return
#        elif i == 2 and not wallLeft[m.x1][m.y1]:
#            print "left"
#            moveLeft(m)
#            return
#        elif i == 3 and not wallLeft[m.x1+1][m.y1]:
#            print "right"
#            moveRight(m)
#            return
#        n = n - 1
#        print "Stuck!"

for i in range(15):
    for j in range(15):
        if a[i][j] == "x":
            cube("realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg", position = P3(i,j,0),size=.5)
           
        

player1 = panda(size = .2, position = P3(.5,.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p= panda(size = .2, position = P3(randomInt(10)+.5, randomInt(10)+.5,0))
#p.x1 = static(0)
#p.y1 = static(0)
camera.position = P3(5, 5, 20)
h = integral(getX(mouse))
speed = P3C(getY(mouse)+1, -h, 0)
#camera.position = P3(3.5, 3.5,.4) + integral(speed)

camera.hpr = HPR(0, -pi/2, 0)
#camera.position= P3(0,0,10)
#camera.hpr = HPR(0,0,0)
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
