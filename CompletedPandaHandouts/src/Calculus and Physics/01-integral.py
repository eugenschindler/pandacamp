#works fine 1/25/11 (TIFF)
from Panda import *
# Adjust the slider to set the speed of the panda.
# The "integral" operation turns speed into position.

s = slider(min = -1, max = 1, init = 0)
text(format("Speed: %5.3f", s))

p = panda(position = P3(integral(s), 0, 0))
text(format("Position: %5.3f", getX(p.position)))
start()