# To change this template, choose Tools | Templates
# and open the template in the editor.

from Panda import *



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


for i in range(15):
    for j in range(15):
        if a[i][j] == "x":
            cube(
            color(0, random01(),random01()),
            color(0, random01(),random01()),
            color(0, random01(),random01()),
            color(0, random01(),random01()),
            color(0, random01(),random01()),
            color(0, random01(),random01()),
            position = P3(i,j,0),size=.5)
           
        

player1 = panda(size = .2, position = P3(.5,.5,0))

camera.position = P3(5, 5, 20)
h = integral(getX(mouse))
speed = P3C(getY(mouse)+1, -h, 0)


camera.hpr = HPR(0, -pi/2, 0)




runner = panda(size = .4)

#other cars
q0 = P3(0,0,0)
p0 = P3(1,1,0)
v0 = P3(0,0,0)

#key commands
v = hold(v0, tag(P3(-1, 0, 0), key("a")) +
             tag(P3(0, -1, 0), key("s")) +
             tag(P3(0, 1, 0), key("w")) +
             tag(P3(1, 0, 0), key("d")) +
             tag(P3(0, 0, 0), key("h")))


#sonic vars
p = p0 + integral(v)
dir = deriv(P3(0,0,0), p)
runner.position = p
hpr = P3toHPR(dir)
runner.hpr = HPR(getH(hpr), getP(hpr), 0)


start()
