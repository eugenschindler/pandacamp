# Needs to be fleshed out / completed as of Jan. 25 2011.

from Panda import *

camera.position = P3(0,-15,0)

#make a spiral of pandas
for i in range(0,30):
    panda(position = P3(cos(i*.5)*(i*.2), 0, sin(i*.5)*(i*.2)))

#make the spiral bigger or smaller, more or less spread out, or contain more or fewer pandas
for i in range(0,30):
    panda(position = P3(cos()*(), 0, sin()*()))

#play with the y-coordinate of the position to make the spiral come toward the screen
for i in range(0,30):
    panda(position = P3(cos(i*.5)*(i*.2), 0 , sin(i*.5)*(i*.2)))

start()