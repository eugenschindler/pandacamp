from Panda import *

# This path is a square
path = at(P3(-1.5,0,-1.5)) \
   + forever(move(1, P3(3, 0, 0)) + \
        move(1, P3(0,0,3)) +  \
        move(1, P3(-3, 0, 0)) +  \
        move(1, P3(0,0,-3)))

def go(t,  color):
    panda(position = interpolate(t, path), color = color)

go(time, red)
go(time+1, blue)
go(time*2, green)
go(time+2, yellow)
go(time*time, white)
start()
