from Panda import *
# Take the panda texture in pictures/panda.jpg and edit it to include
# some text or a pictures.  You can do this with any model - not just the panda!
# Change the file names of pandaInvert and pandaW to your own panda skins.
# Use Gimp to create a negative and add text to the other.
# Create three pandas using the original, invert and text textures.

panda(texture = "pandaW.jpg", hpr = HPR(time, time*1.2, time*time/5))

start()