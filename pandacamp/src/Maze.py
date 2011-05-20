from cgi import length
class Maze:
    def __init__(self, txt):

        #read the txt and store it's size
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        h = contents.length
        w = contents[0].length

        bools = []
        chars = []
        objects = []

        #expand arrays
        for i in xrange(h):
            chars.append([])
            objects.append([])
            bools.append([])
            for j in xrange(w):
                   chars[i].append(i+j)
                   objects[i].append(i+j)
                   bools[i].append(i+j)

        #populate  char array
        x = 0
        y = 0
        for l in contents:
            x = 0
            for c in l:
                chars[x][y] = c
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