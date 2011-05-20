from cgi import length
class MazeObject:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c

class Maze:
    def __init__(self, txt):

        #read the txt and store it's size
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        h = contents.length
        w = contents[0].length # find max length

        bools = []
        chars = []
        objects = []

        #expand arrays
        for i in xrange(h):
            chars.append([])
            objects.append([])
            bools.append([])
            for j in xrange(w):
                   chars[i].append(" ")
                   objects[i].append(None)
                   bools[i].append(False)

        #populate  char array
        x = 0
        y = 0
        for l in contents:
            x = 0
            for c in l:
                chars[x][y] = c
                if(c==" "):
                    feature = None
                else:
                    if(c.isupper()):
                        f= "wall-"+c       
                    else:
                        f= "open-"+c    
                    if(f in dir()):
                        feature = eval(f)(x,y)
                    else:
                        feature = MazeObject(x,y,c)
                objects[x][y] = feature
                bools[x][y]= char[x][y].isupper()
                x = x + 1
            y = y + 1
        
       #populate bool and object arrays
        for i in range(h):
            for j in range(w):
                objects[i][j] = "derrr" # Run the open-'chars[h][j]:
                bools[i][j]= char[h][j].isupper()

                    
    def find(self, c):
        res = []
        for i in range(h):
            for j in range(w):
                if (chars[i][j]==c):
                    res.append(objects[i][j])
        return res

    def collide(self, p):
        return bools[int(p.x)][int(p.y)]
    
    def get(self,p):
        return objects[int(p.x)][int(p.y)]

    def mazecube(self,x,y,c = None,north=None,south=None,east=None,west=None,top=None,bottom=None):
        if(c == None):
            c = color(0, random01(),random01())
        if(north == None):
            north = c
        if(south == None):
            south = c
        if(east == None):
            east = c
        if(west == None):
            west = c
        if(top == None):
            top = c
        if(bottom == None):
            bottom = c

        return cube(
            north,
            south,
            east,
            west,
            top,
            bottom,
            position = P3(x+.5,y+.5,0),size=.5)