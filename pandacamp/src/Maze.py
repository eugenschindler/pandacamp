import math
from DynamicGeometry import *

import sys
from FRP import *
class MazeObject:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
def defaultWall(x,y):
        return mazeCube(x, y, color(0, random01(),random01()))
    
class Maze:
    def __init__(self, txt, modname, color):
#        print modname
#        def wall_X(x,y):
#            return self.mazecube(x, y, color(0, random01(),random01()))
        #read the txt and store it's size>>
        self.filename = txt
        self.type = "maze"
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        self.h = len(contents)
        self.w = 0
        for r in contents:
            self.w = max(self.w,len(r))
        

        self.bools = []
        self.chars = []
        self.objects = []

        #expand arrays
        for i in xrange(self.h):
            self.chars.append([])
            self.objects.append([])
            self.bools.append([])
            for j in xrange(self.w):
                   self.chars[i].append(" ")
                   self.objects[i].append(None)
                   self.bools[i].append(False)

        #populate  char array

        print self.h
        print self.w
        print len(self.chars)
        print len(self.chars[0])
        s = set()
        #print dir(sys.modules[modname])
        #print sys.modules[modname]
        for ln in xrange(self.h):
            l = contents[ln]

            print l
            for cn in xrange(self.w):
                if cn >= len(l):
                    c = " "
                else:
                    c = l[cn]

                self.chars[ln][cn] = c
                if(c==" "):
                    feature = None
                else:
                    if(c.isupper()):
                        f= "sys.modules[modname].wall_"+c
                        if not(("wall_"+c) in dir(sys.modules[modname])):
                            feature = defaultWall(cn,self.h-ln-1)
                            s.add("No wall_ method for "+c+". Used default wall")
                        else:
                            feature = eval(f)(cn,self.h-ln-1)
                    else:
                        f= "sys.modules[modname].open_"+c
                        if not(("open_"+c) in dir(sys.modules[modname])):
                            s.add("No open_ method for "+c+". Used empty space")
                        else:
                            feature = eval(f)(cn,self.h-ln-1)

                self.objects[ln][cn] = feature
                self.bools[ln][cn]= self.chars[ln][cn].isupper()

            print self.chars[ln]


        for e in s:
            print e
        rectangle(P3(0,0,0), P3(self.w, 0, 0), P3(0, self.h, 0), color)

    

    def find(self, c):
        res = []
        for i in range(len(self.chars)):
            for j in range(len(self.chars[i])):
                if (self.chars[i][j]==c):
                    res.append(self.objects[i][j])
        return res

    def collide(self, p):
        return self.bools[int(p.y)][int(p.x)]
    
    def get(self,p):
        return self.objects[int(p.y)][int(p.x)]

    def wallForce(self, s,r):
        return lift(lambda x,r: wallForceStatic(self, x,r), "wallForce", [P3Type,P3Type], P3Type)(s,r)
    
    def wallHit(self, rad, pos):
        return lift(lambda rad,pos: wallHitStatic(self, rad, pos), "wallForce", [numType,P3Type], P3Type)(rad, pos)
    
    def openings(self, (x, y), (x0, y0)):
        res = []
        dir = None
        if x0 == -1:
            dir = (0, 1)
        else:
            dir = (y-y0, x0-x)
        if not self.bools[x+dir[0]][y+dir[1]]:
            res = res + [(x+dir[0], y+dir[1])]
        dir = (-dir[1], dir[0])
        if not self.bools[x+dir[0]][y+dir[1]]:
            res = res + [(x+dir[0], y+dir[1])]
        dir = (-dir[1], dir[0])
        if not self.bools[x+dir[0]][y+dir[1]]:
            res = res + [(x+dir[0], y+dir[1])]
        dir = (-dir[1], dir[0])
        if not self.bools[x+dir[0]][y+dir[1]]:
            res = res + [(x+dir[0], y+dir[1])]
        return res
        

def mazeCube(x,y,col = None,north=None,south=None,east=None,west=None,top=None,bottom=None):
        if(col == None):
            col = color(0, random01(),random01())
        if(north == None):
            north = col
        if(south == None):
            south = col
        if(east == None):
            east = col
        if(west == None):
            west = col
        if(top == None):
            top = col
        if(bottom == None):
            bottom = col

        return cube(
            north,
            south,
            east,
            west,
            top,
            bottom,
            position = P3(x+.5,y+.5,0),size=.49)


def maze(f,m, color = springGreen):
    return Maze(f,m, color)

def findInMaze(m,c):
    print getPType(m)
    if getPType(m) != "maze":
        print "Not a maze"
        exit()
    return m.find(c)

def find1InMaze(m,c):
    if getPType(m) != "maze":
        print "Not a Maze"
        exit()
    x = m.find(c)
    if (len(x) == 0):
        print "no objects in array"
        exit()
    if len(x) > 1:
        print "too many " + c + " objects in maze"
        exit()
    return x[0]

def mazeWall(m,p):
    if (p.x >= m.w) or (p.x <= 0) or (p.y >= m.h) or (p.y <= 0):
        return False
    else:
        return m.bools[int(p.y)][int(m.h-(p.x)-1)]

def wallForceStatic(m,p,r):
    res = SP3(0,0,0)
    lx = sFraction(p.x)
    ly = sFraction(p.y)
    dirx = r.x > p.x
    diry = r.y > p.y
    dist = sqrt((r.x - p.x)*(r.x - p.x) + (r.y - p.y)*(r.y - p.y))
    frx = sFloor(r.x)
    fry = sFloor(r.y)
    fpx = sFloor(p.x)
    fpy = sFloor(p.y)


    if mazeWall(m,p + P3(1,0,0)) and lx >.8:
        res = res + P3(-1,0,0)*((lx-.8)*5)
        print fry
        if not (fry == fpy):
            if diry:
                res = res + P3(0,1,0)*.4*dist
            else:
                res = res + P3(0,-1,0)*.4*dist
    if mazeWall(m,p + P3(-1,0,0))and lx <.2:
        res = res + P3(1,0,0)* ((.2-lx)*5)
        if not (fry == fpy):
            if diry:
                res = res + P3(0,1,0)*.4*dist
            else:
                res = res + P3(0,-1,0)*.4*dist
    if mazeWall(m,p + P3(0,1,0)) and ly >.8:
        res = res + P3(0,-1,0)*((ly-.8)*5)
        if not (frx == fpx):
            if dirx:
                res = res + P3(1,0,0)*.4*dist
            else:
                res = res + P3(-1,0,0)*.4*dist
    if mazeWall(m,p + P3(0,-1,0))and ly <.2:
        res = res + P3(0,1,0)* ((.2-ly)*5)
        if not (frx == fpx):
            if dirx:
                res = res + P3(1,0,0)*.4*dist
            else:
                res = res + P3(-1,0,0)*.4*dist
    return res


def wallHitStatic(m,rad,d):
    up = 5000
    down = -5000
    left = -5000
    right = 5000
    if mazeWall(m,P3(d.x,d.y+1,0)):
        up = ceiling(d.y)-rad
        
    if mazeWall(m,P3(d.x,d.y-1,0)):
        down = floor(d.y)+rad
        
    if mazeWall(m,P3(d.x-1,d.y,0)):
        left = floor(d.x)+rad
        
    if mazeWall(m,P3(d.x+1,d.y,0)):
        right = ceiling(d.x)-rad
        
    x= clamp(d.x,left,right)
    y= clamp(d.y,down,up)
    
    return P3(x,y,0)

def clamp(x,mi,ma):
   x = max(x,mi)
   x = min(x,ma)
   return x
    
def moveInMaze(model, maze, p0, vel):
    def f(s, v):
        (oldTime, oldPos) = s
        t = g.currentTime
        p1 = oldPos + v*(t - oldTime)
        p2 = wallHitStatic(maze, model.cRadius * model.size.now() , p1)
#        print "Try: " + str(p1) + " Corrected: " + str(p2)
        if mazeWall(maze, p2):
            print "In wall"
            p2 = oldPos
        return ((t, p2), p2)
    model.position = tracker(f, (g.currentTime, p0), vel, P3Type)


def mazeStrategy(model, maze, strategy, vel, s0, pos, lastPos = (-1, -1)):
    def chooseDir(m, d):
        (s, pos, lastPos) = d
        mazeStrategy(model, maze, strategy, vel, s, pos, lastPos)
    deltaT = 1/(vel + 0.0)
    (s, newPos) = strategy(s0, maze.openings(pos, lastPos), pos)
    vv = P3(newPos[0] - pos[0], newPos[1] - pos[1], 0)
    model.position = P3(pos[0]+.5, pos[1]+.5, 0) + integral(vv * vel)
    model.hpr = P3toHPR(vv)
    model.react1(tag((s, newPos, pos), localTimeIs(deltaT)), chooseDir)
