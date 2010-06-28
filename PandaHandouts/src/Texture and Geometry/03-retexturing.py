from Panda import *
# take the panda texture in pictures/panda.jpg and edit it to include
# some text or a pictures.  You can do this with any model - not just the panda!
# Change the file names of pandaInvert and pandaW to your own panda skins.

# Use GIMP to alter the skin of one of the built in models 

p1 = panda(position = P3(-2, 0, 0), hpr = HPR(time, 0, 0))
p2 = panda(position = P3(0, 0, 0), hpr = HPR(time, 0, 0), texture = "pandaInvert.jpg")
p3 = panda(position = P3(2, 0, 0), hpr = HPR(time, 0, 0), texture = "pandaW.jpg")


start()