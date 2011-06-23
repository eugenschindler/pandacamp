
from Panda import *



grassScene()


def open_b(x,y):
        return bunny(position = P3(x+.5,y+.5,0),size=.5)

def open_j(x,y):
        return jeep(position = P3(x+.5,y+.5,0),size=.5)

m2 = Maze("maze.txt", __name__)
runner = find1InMaze(m2,"b")

p0 = P3(1.5,1.5,.5)

forvel = hold(0.0, key("arrow_up", 2) + keyUp("arrow_up", 0)+
                   key("arrow_down",-2)+keyUp("arrow_down", 0))

turnvel = hold(0.0,key("arrow_left", 2) + keyUp("arrow_left", 0) + 
                   key("arrow_right", -2)+keyUp("arrow_right", 0))
                  
heading = integral(turnvel)

runv = P3C(forvel, heading, 0)

#camera.hpr = hpr + HPR(-pi/2, 0, 0)
#camera.position = integral(v) + p0
#To put the camera up above use stuff like this instead
camera.position = P3(5, 5, 20)
camera.hpr = HPR(0, -pi/2, 0)

start()
