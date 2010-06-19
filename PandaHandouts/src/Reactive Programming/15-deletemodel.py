from Panda import *

# The timeIs event happens at given absolute time
# There is also a localTimeIs event
p = panda(position = P3(0,0,0))

def byebye(m, v):
    m.exit()

p.react(timeIs(1), byebye)

# Write a python function that creates a new panda at a given place that waits for
# a particular time before exiting.
# Create two pandas that disappear at different times.

# Use the alarm clock from the previous example to launch pandas.  Add a reaction
# to each one that removes the panda if it is clicked with the left button.

start()