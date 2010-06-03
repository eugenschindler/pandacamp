# intro to Panda/09-color.py
from Panda import *

# Explore colors
# The "color" function has three parameters: red, green, blue
# These are numbers between 0 and 1
# If you add a 4th number it controls transparency
# How would you make the "negative" of a color?
# Try using the color on the panda using "color="

panda(color=red, position = P3(0,4,0))

#Set up RGB sliders and Text
re = slider(min = -1 ,max = 1, label = "red")
gr = slider(min = -1 ,max = 1, label = "green")
bl = slider(min = -1 ,max = 1, label = "blue")

text(format("Red: %5.3f  Green: %5.3f  Blue: %5.3f", re, gr, bl))

world.color = color(re,gr,bl)

# negative color:
panda(color=color(1-re,1-gr,1-bl), position =P3(0,4,2))

start()