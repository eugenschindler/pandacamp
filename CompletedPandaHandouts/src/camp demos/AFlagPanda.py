from Panda import *

# Simple recursion (counting)
w = warpSpeed(position = P3(0,0,0), size = 0)
# Define a function to make a line of pandas of a given length
# You need the following:
#   A parameter "number" which tells you how many more panda to make
#   A parameter "place" which tells you where the last panda was placed
# Inside the function, you need to use "if" to determine whether
# we need more pandas.

camera.position = P3(0, -20, 0)  # Stand back to see the herd of pandas!
def changepanda1(model):
    model.color=red
def stopspark(pe):
    pe.stop()
  
def changepanda2(model):
    model.color=blue
def changepanda3(model):
    model.color=white
def spark(p):
    w = warpSpeed(position = P3(0,0,0), size = 1)
    w.when1(localTime>2,stopspark)


# This function puts a line of panda
def pandaLine(number, place):
    if number > 0:
        p1=panda(position = P3 (place, time*7, place),size=1+time/8,)
        p2=panda(position = P3 (place, time*7, -place),size=1+time/8)
        p3=panda(position = P3 (0, time*7, place),size=1+time/8)
        p4=panda(position = P3 (place, time*7, 0),size=1+time/8)
        p5=pandaLine(number-1, place+2)
        p1.when(time>8*pi, changepanda1)
        p2.when(time>8*pi, changepanda2)
        p3.when(time>8*pi, changepanda3)
        


        # Place a panda at P3(place, 0, 0)
        # Continue the panda line by calling pandaLine
        # What should the new value of place be?
        # What should the new value of number be?

# Make a line of 10 pandas that starts at P3(-4,0,0)
pandaLine(100, -100)

when1(time>8*pi,spark)
# Can you make a line of 20 pandas?
# Can you put two pandas in a stack at each position?
# Can you have the roll change as well as the position?
# Can you make the line rise?

start()