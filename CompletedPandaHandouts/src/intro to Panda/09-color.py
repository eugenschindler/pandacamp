# intro to Panda/09-color.py
from Panda import *

# Explore colors
# The "color" function has three parameters: red, green, blue
# These are numbers between 0 and 1
# Set the world's background color using sliderColor
# recolor the panda by setting its color using a slider

panda(color=red, position = P3(0,4,0))

#Set up RGB sliders and Text
c = sliderColor(label = "Color")
pc = slider(min = 0, max = 1, init = 0)

text(c)

world.color = c

panda(color=color(0, pc, 0), position =P3(0,4,2))

start()