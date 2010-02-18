from Panda import *

#for loops repeat over a list of numbers
#for loops can be nested

for i in range(-1,2):
    for j in range(-1,2):
         panda(position = P3(i, 0, j))

#keep the for loops the same, and modify the position so the pandas
#are more spread out
#for i in range(-1,2):
#    for j in range(-1,2):
#        panda(position = P3())

#add an HPR that depends on i or j in order to make the pandas farther right
#face to the right
#for i in range(0,3):
#    for j in range(0,3):
#        panda(position = P3(i-1, 0, j-1), hpr = HPR())

start()