from Panda import *
# Most of the particle effects use two colors: an initial and final color.
# The color attribute is the initial color, the endColor attribute is the color
# that the particles turn to as they get older.

# Some of these effects can't change colors (firish and sparkles)

# Experiment with the colors of these effects.

# Once you're done with this, you can look at the particle panel in the utils
# to see what other sorts of parameters can be adjusted in these effects.


color1 = sliderColor(label = "c1")

color2 = sliderColor(label = "c2")

# intervalRings(position = P3(0,0,0),color = color1, endColor = color2, size = .1)
# likeFountainWater(position = P3(0,0,0))
# shakenSparkles(position = P3(0,0,0))
# warpSpeed(position = P3(0,0,0))
#heavySnow(position = P3(0,0,0))
#lightSnow(position = P3(0,0,0))
warpSpeed(position = P3(0,0,0),color = color1, endColor = color2)
#fireish(position = P3(0,0,0))

start()