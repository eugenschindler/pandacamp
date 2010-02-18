from Panda import *

# This is called a "list" - here's a list of models:
models = [panda, jeep, soccerball]

# You can choose a random element from this list using rand():

# m = rand(models)



# Start with the line of pandas from before:

def pandaLine(place, number):
    if number > 0:
        m = rand(models)
        m(position = P3(place, 0, 0))
        print m
        pandaLine(place+1, number-1)

# Make a line of pandas starting at -2 with 5 pandas.

# Alter this to choose a random model instead of just pandas using rand

# pandaLine(-2, 5)
p = panda(position = P3(0,0,0))


def rmove(m, v):
    m.position = m.position.now() + \
         localTime*P3(2*rand()-1, 2*rand()-1, 2*rand()-1)
    m.react1(localTimeIs(rand()+1), rmove)
p.react1(localTimeIs(1), rmove)
start()