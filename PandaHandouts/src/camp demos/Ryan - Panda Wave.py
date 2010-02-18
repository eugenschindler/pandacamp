from Panda import *

# Simple recursion (counting)
grassScene(position=P3(0,-30,-2),size=3)
# Define a function to make a line of pandas of a given length
# You need the following:
#   A parameter "number" which tells you how many more panda to make
#   A parameter "place" which tells you where the last panda was placed
# Inside the function, you need to use "if" to determine whether
# we need more pandas.

  # Stand back to see the herd of pandas!
camera.position = P3(20,-75,1)
# This function puts a line of panda
def pandaLine(number, place):
    if number > 0:
        panda(position = P3(place,0,0),hpr = HPR (0,time+place,0),size = cos(time+place)+ 1.1)
        pandaLine(number-1,place+1)
        # Place a panda at P3(place, 0, 0)
        # Continue the panda line by calling pandaLine
        # What should the new value of place be?
        # What should the new value of number be?

# Make a line of 10 pandas that starts at P3(-4,0,0)
pandaLine(50,-4)


lightlocation = P3C(4, time*3, .25)
lightcolor = blue
ambientlight(color = color(.1, .5, .1))
directionallight(color = lightcolor, hpr = HPR(0,pi/2,0))
# Can you make a line of 20 pandas?
# Can you put two pandas in a stack at each position?
# Can you have the roll change as well as the position?
# Can you make the line rise?

start()