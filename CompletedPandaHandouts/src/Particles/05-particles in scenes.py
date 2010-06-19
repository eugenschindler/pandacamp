from Panda import *

# Here's an example of an amusing effect.  Play with the position and hpr
# and you can make the explosions go in different directions.
r2d2()

def boom(p, v):
    explosion(position = P3(0,0,1), hpr = HPR(0, localTime, 0))

react(alarm(start = 0, step = 1), boom)

start()