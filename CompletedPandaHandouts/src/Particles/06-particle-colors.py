from Panda import *
# Most of the particle effects use two colors: an initial and final color.
# The color attribute is the initial color, the endColor attribute is the color
# that the particles turn to as they get older.

# Some of these effects can't change colors (firish and sparkles)

# Experiment with the colors of these effects.

# Once you're done with this, you can look at the particle panel in the utils
# to see what other sorts of parameters can be adjusted in these effects.

r1 = slider(label = "r1")
g1 = slider(label = "g1")
b1 = slider(label = "b1")
color1 = color(r1, g1, b1)

r2 = slider(label = "r2")
g2 = slider(label = "g2")
b2 = slider(label = "b2")
color2 = color(r2, g2, b2)

# intervalRings(position = P3(0,0,0),color = color1, endColor = color2, size = .1)
# likeFountainWater(position = P3(0,0,0))
# shakenSparkles(position = P3(0,0,0))
# warpSpeed(position = P3(0,0,0))
#heavySnow(position = P3(0,0,0))
#lightSnow(position = P3(0,0,0))
warpSpeed(position = P3(0,0,0),color = color1, endColor = color2)
#fireish(position = P3(0,0,0))

start()