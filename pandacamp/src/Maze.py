from DynamicGeometry import *
import sys
class MazeObject:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c

class Maze:
    def __init__(self, txt, modname):
        print modname
#        def wall_X(x,y):
#            return self.mazecube(x, y, color(0, random01(),random01()))
        
        print("derr")
        #read the txt and store it's size
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        h = len(contents)
        w = len(contents[0])# find max length

        self.bools = []
        self.chars = []
        self.objects = []

        #expand arrays
        for i in xrange(h):
            self.chars.append([])
            self.objects.append([])
            self.bools.append([])
            for j in xrange(w):
                   self.chars[i].append(" ")
                   self.objects[i].append(None)
                   self.bools[i].append(False)

        #populate  char array
        x = 0
        y = 0
        print dir()
        print sys.modules[modname]
        for l in contents:
            x = 0
            for c in l:
                self.chars[x][y] = c
                if(c==" "):
                    feature = None
                else:
                    if(c.isupper()):
                        f= "sys.modules[modname].wall_"+c
                    else:
                        f= "sys.modules[modname].open_"+c
                    #if(f in dir()):
                    feature = eval(f)(x,y)
                    #else:
                    #    feature = MazeObject(x,y,c)
                self.objects[x][y] = feature
                self.bools[x][y]= self.chars[x][y].isupper()
                x = x + 1
            y = y + 1
        
       #populate bool and object arrays
#        for i in range(h):
#            for j in range(w):
#                self.objects[i][j] = "derrr" # Run the open-'self.chars[h][j]:
#                self.bools[i][j]= self.chars[i][j].isupper()

                    
    def find(self, c):
        res = []
        for i in range(h):
            for j in range(w):
                if (self.chars[i][j]==c):
                    res.append(self.objects[i][j])
        return res

    def collide(self, p):
        return self.bools[int(p.x)][int(p.y)]
    
    def get(self,p):
        return self.objects[int(p.x)][int(p.y)]
   
    @staticmethod
    def mazecube(x,y,col = None,north=None,south=None,east=None,west=None,top=None,bottom=None):
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

