from Panda import *
# take the panda texture in pictures/panda.jpg and edit it to include
# some text or a pictures.  You can do this with any model - not just the panda!
# Change the file names of pandaInvert and pandaW to your own panda skins.

def setTexture(p, v):
  p.setTexture(v)

p = panda(position = P3(0,0,-1))

p.hpr=HPR(time,0,0)

b1 = button("regular")
b2 = button("Invert")
b3 = button("W")

p.react(tag("panda.jpg", b1)+tag("pandaInvert.jpg", b2)+tag("pandaW.jpg", b3), setTexture)

start()