from Panda import *
world.color=black
# Simple recursion (counting)

# Define a function to make a line of pandas of a given length
# You need the following:
#   A parameter "number" which tells you how many more panda to make
#   A parameter "place" which tells you where the last panda was placed
# Inside the function, you need to use "if" to determine whether
# we need more pandas.

# camera.position = P3(0, -20, 0)  # Stand back to see the herd of pandas!
def col(x, p, o):
    return (1+sin(x*p-o)/2)

def mycolor(o):
    return color(col(time, 3.2, o), col(time, 5.1, o), col(time, 6.2, o))
# This function puts a line of panda
def pandaLine(number, place, p1):
    if number > 0:
      p= bunny (position = P3(p1,0,place), hpr=HPR (time-2+place,time*2.1+place,time+2+place))
      p.color = mycolor(place/1.0)
      pandaLine(number-1,place+1, p1)

        # Place a panda at P3(place, 0, 0)
        # Continue the panda line by calling pandaLine
        # What should the new value of place be?
        # What should the new value of number be?

# Make a line of 10 pandas that starts at P3(-4,0,0)
pandaLine(10, -4, 0)
pandaLine(10, -4, 1)
pandaLine(10, -4, -1)
camera.position = P3(0, -2-time*3, 0)

# Can you make a line of 20 pandas?
# Can you put two pandas in a stack at each position?
# Can you have the roll change as well as the position?
# Can you make the line rise?

start()