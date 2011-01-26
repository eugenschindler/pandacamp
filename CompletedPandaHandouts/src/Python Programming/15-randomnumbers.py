# exactly the same as 14-randomnumbers.py as of Jan. 25 2011.
from Panda import *
import random

camera.position = P3(0,-25,0)

count = 0
while(count < 15):
    i = random.randint(-4,4)
    j = random.randint(-4,4)
    k = random.randint(-4,4)
    panda(position = P3(i,j,k), hpr = HPR(i,j,k))
    count = count + 1

start()