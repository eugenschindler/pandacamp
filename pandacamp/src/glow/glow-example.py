## Simple example of the Glow Filter.
## Author: Adam Bell (ventosproject@gmail.com)
## Project: PandaCamp (http://code.google.com/p/pandacamp/)

# glow-example.py REQUIRES Adam Bell's update to "World.py",
# or a further modification for the Glow filters.

from Panda import *
# Imports everything from PandaCamp's Panda.py

gorilla(hpr = HPR(time/8, 0, 0), position = P3(0,0,-.4))
# Adds a gorilla model centered and rotates counter-clockwise slowly.

camera.position = P3(0,-5,0)
# Moves the camera back 5 units so the panda can be seen.

world.color = black
# Sets the world color to black. This will help make the high-contrast so the glowing is easier to see.

Glow(amount = 2)
# Calls the class "Glow()" from "World.py".
# "amount = 1" tells glowShader to be at it's current minimal amount.
# The glowShader can currently handle whole numbers 1, 2, 3, and 4.

start()