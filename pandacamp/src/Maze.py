from cgi import length
class Maze:
    def __init__(self, txt):
        
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        x = 0
        y = 0
        h = contents.length
        w = contents[0].length

        chars = []
        #expand char array
        for i in xrange(h):
            chars.append([])
            for j in xrange(w):
                   chars[i].append(i+j)
        #populate  char array           
        for l in contents:
            x = 0
            for c in l:
                chars[x][y] = c
                x = x + 1
            y = y + 1
        
        
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
                if a[i][j] == "b":
                     bunny(position = P3(i,j,0),size=.5)
                if a[i][j] == "j":
                     jeep(position = P3(i,j,0),size=.5)
