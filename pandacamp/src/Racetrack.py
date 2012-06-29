import math
from DynamicGeometry import *
from Sound import *

import sys
from FRP import *

# This code creates a maze object from data stored in a file
# Each character in the file corresponds to a square in the maze.
# Uppercase letters correspond to walls, as defined by wall_C functions
# lowercase letters are objects in the maze, as defined by open_C functions.

# C is the character at location x,y
class MazeObject:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c

# This defines a default wall tile
def defaultWall(x,y):
        return mazeCube(x, y, color(0, random01(),random01()))

# txt is the file name, modname is the name of the Python module contain functions which elaborate maze objects

# racetrack item list
items = []
questionBlock = "questionBlock.JPG"
boost = "boost.png"
charge = "charge.png"
defense = "defense.png"
glide = "glide.png"
hp = "hp.png"
offense = "offense.png"
speed = "speed.png"
turn = "turn.png"
weight = "weight.png"

# item actions
bounce = "bounce"
spin = "spin"
both = "both"


class Racetrack:
    def __init__(self, txt, checkered = True, model = None):
        # for now the track will only have one object interacting with it
        self.model = model
        # reactive score
        self.score = var(0)
        # for ease of checkering
        self.tile = 1 if checkered else 0
        # default vocabulary dictionary
        # the key is the letter, the value is a list of attributes (for now the default texture image, surface friction, and centripetal force friction)
        self.vocab = dict({"r":["road.jpeg",0.45,0.35] ,"d":["dirt.jpg",0.85,0.85] ,"g":["grass.png",0.95,0.75] ,"w":["water.jpeg",0,0] ,"x":["bricks.jpg",0.95,0.95]})
        #read the txt and store it's size>>
        self.filename = txt
        self.type = "maze"
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        self.h = len(contents)  # Height is the number of lines
        self.w = 0  # Take a running max over line lenths
        for r in contents:
            self.w = max(self.w,len(r))
        self.bools = []
        self.chars = []
        self.objects = []

        #expand arrays.  These are all 2-D arrays
        for i in xrange(self.h):
            self.chars.append([]) # The character at each location
            self.objects.append([])  # The Panda object at each location
            self.bools.append([]) # A boolean: open / solid
            for j in xrange(self.w):
                   self.chars[i].append(" ")
                   self.objects[i].append(None)
                   self.bools[i].append(False)

        #populate  char array

        s = set()
        for ln in xrange(self.h):
            l = contents[ln]
            for cn in xrange(self.w):
                #if cn >= len(l):
                if cn < len(l):
                    #c = "r"
                #else:
                    c = l[cn]

                    # Add track features with tiled colors
                    # Need textures!
                    self.chars[ln][cn] = c
                    if c == "x":
                        feature = block(cn+0.5, self.h-ln-0.5, self.vocab[c][0])
                    else:
                        feature = ground(cn, self.h-ln-1, self.vocab[c][0], (self.tile*(ln+cn))%2)

                '''
                if c == "r":
                    if (ln+cn)%2==0:
                        #feature = floorRect(cn,self.h-ln-1,col=black)
                        #feature = floorRect(cn,self.h-ln-1,image="road.jpeg")
                        feature = floorRect(cn,self.h-ln-1,image=hp)
                    else:
                        feature = floorRect(cn,self.h-ln-1,col=color24(240,240,240),image="road.jpeg")
                elif c == "d":
                    if (ln+cn)%2==0:
                        feature = floorRect(cn,self.h-ln-1,image="dirt.jpg")
                    else:
                        feature = floorRect(cn,self.h-ln-1,col=color24(240,240,240),image="dirt.jpg")
                elif c == "g":
                    if (ln+cn)%2==0:
                        feature = floorRect(cn,self.h-ln-1,image="grass.png")
                    else:
                        feature = floorRect(cn,self.h-ln-1,col=color24(240,240,240),image="grass.png")
                elif c == "w":
                    if (ln+cn)%2==0:
                        feature = floorRect(cn,self.h-ln-1,image="water.jpeg")
                    else:
                        feature = floorRect(cn,self.h-ln-1,col=color24(240,240,240),image="water.jpeg")
                elif c == "x":
                    feature = mazeCube2(cn+0.5,self.h-ln-0.5)
                else:
                    feature = floorRect(cn+0.5,self.h-ln-0.5)
                '''

                self.objects[ln][cn] = feature
                self.bools[ln][cn]= self.chars[ln][cn].isupper()
                

        #        print self.chars[ln]

        # Create the floor - this can be a solid color or a picture
        #if color != None:
        #    rectangle(P3(0,0,0), P3(self.w, 0, 0), P3(0, self.h, 0), color)

    '''
    # Return the objects generated by a particular letter
    def find(self, c):
        res = []
        for i in range(len(self.chars)):
            for j in range(len(self.chars[i])):
                if (self.chars[i][j]==c):
                    res.append(self.objects[i][j])
        return res

    # Is the x, y coordinate if within a wall?  z is ignored.
    def collide(self, p):
        return self.bools[int(p.y)][int(p.x)]
    # Return the object initially at location x, y
    def get(self,p):
        return self.objects[int(p.y)][int(p.x)]

    # Used for force controllers within the maze.  Not being used because of problems in force controllers
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
    '''

    
    def item(self, name, pos, hpr0 = HPR(0,0,0), size = 0.2, action = None):
        if action == "bounce":
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0),hpr=hpr0)
        elif action == "spin":
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0))
        elif action == "both":
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0))
        else:
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0))
        items.append(item) 
        return items[-1]


    # Returns the friction of the current surface
    def friction(self, p):
        try:
            c = self.chars[int(p.y)-1][int(p.x)]
        except:
            c = "r"
        if c == " ":
            return self.vocab["r"][1]
        return self.vocab[c][1]

    # Lift friction!
    def getFriction(self, s):
        return (lift(lambda p:self.friction(p), "friction", [P3Type], numType))(s)

    # Returns the centripetal force of the current surface
    def cent(self, p):
        try:
            c = self.chars[int(p.y)-1][int(p.x)]
        except:
            c = "r"
        if c == " ":
            return self.vocab["r"][2]
        return self.vocab[c][2]

    # Lift centripetal!
    def getCent(self, s):
        return (lift(lambda p:self.cent(p), "dent", [P3Type], numType))(s)

    # This is used for cube collision
    def inwall(self, r, s, p):
        #s = now(model.size)
        radius = s*r
        #p = now(model.position)
        n = p + SP3(r,0,0)
        e = p + SP3(0,r,0)
        s = p - SP3(r,0,0)
        w = p - SP3(0,r,0)
        try:
            if self.chars[int(getY(n))][int(getX(n))] == "x":
                return True
            elif self.chars[int(getY(e))-1][int(getX(e))] == "x":
                return True
            elif self.chars[int(getY(s))][int(getX(s))] == "x":
                return True
            elif self.chars[int(getY(w))-1][int(getX(w))] == "x":
                return True
            else:
                return False
        except:
            return False

    def inWall(self, m):
        return (lift(lambda r,s,p:self.inwall(r,s,p), "inwall", [numType,numType,P3Type], boolType))(m.cRadius,m.size,m.position)

    def getRandomLoc(self):
        while(True):
            r1 = int(randomRange(0,self.w))
            r2 = int(randomRange(0,self.h))
            if self.chars[r1][r2] != "x":
                break
        return P3(r1+0.5,r2+0.5)


    def placeObj(self, texture, position = None, size = 0.2, duration = 10000, score = 0, reaction = None, sound = None):
        if position == None:
            position = getRandomLoc()
        obj = rectangle(P3(-size/2,0,0), P3(size/2,0,0), P3(-size/2,0,size), position = position, texture = texture, hpr = integral(HPR(pi/4,0,0)), duration = duration)

        def reactToHit(m,v):
            if sound != None:
                play(sound)
            self.score.add(score)
            obj.exit()
            #print "HIT!"
            if reaction != None:
                reaction(self.model,self)

        obj.when(dist(self.model.position,obj.position) < (self.model.cRadius*self.model.size)+size, reactToHit)


'''
# This creates a solid cube in the maze.  There are siz textures.  The first texture is the default.
# x and y are in maze coordinates.
# If no color is given a random color is chosen.
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
            # Use size = .49 so that the textures on adjacent cubes don't touch
'''

# This creates a cube in the maze with one color. If no color is given then gray is used.
def block(x, y, image):
    #return cube(image,image,image,image,image,image,position = P3(x,y,0),size = 0.5)
    return cube(image,image,image,image,image,image,position = P3(x,y,0),size = 0.5)

# This creates a colored floor rectangle. If no color is given then gray is used.
def floorRect(x, y, col = None, image = None):
    return rectangle(P3(x,y,0), P3(x,y+1,0), P3(x+1,y,0), color = col, texture = image)

def ground(x, y, image, rotation):
    #return rectangle(P3(x,y+rotation,0), P3(x+rotation,y+1,0), P3(x+1,y,0), color = Color(240,240,240,rotation))
    col = 100+(100*rotation)
    #print col
    # the checkerboard coloring doesn't work. is there a bug in the color interpolation code?
    return rectangle(P3(x,y+rotation,0), P3(x+rotation,y+1,0), P3(x+(1+rotation)%2,y,0), texture = image, color = Color(col,col,col))


'''
# Create a maze from a file (f)  The value of m
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

# Not presently used
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

# I think this should be changed to take an initial point and return that if
# movement is impossible.
# Given a maze m, an object with a radius rad, and a proposed point d return
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
    # This should probably retain the z coordinate of the input ...
    return P3(x,y,0)

# Return a value between mi and ma
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
'''

