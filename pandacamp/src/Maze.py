import math
from DynamicGeometry import *
from sets import Set
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
    def __init__(self, txt, modname):
#        print modname
#        def wall_X(x,y):
#            return self.mazecube(x, y, color(0, random01(),random01()))
        #read the txt and store it's size
        self.filename = txt
        self.type = "maze"
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        self.h = len(contents)
        self.w = len(contents[0])# find max length

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
        x = 0
        y = 0
        s = Set()
        #print dir(sys.modules[modname])
        #print sys.modules[modname]
        for l in contents:
            x = 0
            for c in l:
                self.chars[x][y] = c
                if(c==" "):
                    feature = None
                else:
                    if(c.isupper()):
                        f= "sys.modules[modname].wall_"+c
                        if not(("wall_"+c) in dir(sys.modules[modname])):
                            feature = defaultWall(x,y)
                            s.add("No wall_ method for "+c+". Used default wall")
                        else:
                            feature = eval(f)(x,y)
                    else:
                        f= "sys.modules[modname].open_"+c
                        if not(("open_"+c) in dir(sys.modules[modname])):
                            s.add("No open_ method for "+c+". Used empty space")
                        else:
                            feature = eval(f)(x,y)
                    
                    #else:
                    #    feature = MazeObject(x,y,c)
                self.objects[x][y] = feature
                self.bools[x][y]= self.chars[x][y].isupper()
                x = x + 1
            y = y + 1
        for e in s:
            print e
       #populate bool and object arrays
#        for i in range(h):
#            for j in range(w):
#                self.objects[i][j] = "derrr" # Run the open-'self.chars[h][j]:
#                self.bools[i][j]= self.chars[i][j].isupper()

    

    def find(self, c):
        res = []
        for i in range(len(self.chars)):
            for j in range(len(self.chars[i])):
                if (self.chars[i][j]==c):
                    res.append(self.objects[i][j])
        return res

    def collide(self, p):
        return self.bools[int(p.x)][int(p.y)]
    
    def get(self,p):
        return self.objects[int(p.x)][int(p.y)]

    def wallForce(self, s,r):
        return lift(lambda x,r: wallForceStatic(self, x,r), "wallForce", [P3Type,P3Type], P3Type)(s,r)
    
    def wallHit(self, rad, pos):
        return lift(lambda rad,pos: wallHitStatic(self, rad, pos), "wallForce", [numType,P3Type], P3Type)(rad, pos)
   

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
            position = P3(x+.5,y+.5,0),size=.5)


def maze(f,m):
    return Maze(f,m)

def findInMaze(m,c):
    print getPType(m)
    if getPType(m) != "maze":
        print "dsf"
        exit()
    return m.find(c)

def find1InMaze(m,c):
    if getPType(m) != "maze":
        print "Not a Maze"
        exit()
    x = m.find(c)
    if (len(x) == 0):
        print "no objects in array"
        exit   
    return x[0]

def mazeWall(m,p):
    if (p.x >= m.w) or (p.x <= 0) or (p.y >= m.h) or (p.y <= 0):
        return False
    else:
        return m.bools[int(p.x)][int(p.y)]

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
        if mazeWall(maze, p2):
            p2 = oldPos
        return ((t, p2), p2)
    model.position = tracker(f, (g.currentTime, p0), vel, P3Type)