#works but thin on code 1/25/11 (TIFF)
from Panda import *

#for x in range(5):
#    panda(position = P3(x-2, 0, 0))
#
#for x in range(5):
#    for y in range(5):
#        panda(position = P3(x-2, 0, y-2))

def path(t):
    return P3(t-2, 0, sin(t*2))

for x in range(5):
    panda(position = path(time-x))

start()