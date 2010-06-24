
from Panda import *
# Adjust the slider to set the speed of the panda.
# The "integral" operation turns speed into position.
grassScene()
panda()

speed= hold(P3(0,0,0), key("arrow_up", P3(0,1,0)) + key("arrow_down", P3(0,-1,0))
      + key("arrow_right", P3(1,0,0)) + key("arrow_left", P3(-1, 0, 0)))

# speed = P3(getX(mouse), getY(mouse), 0)
#
#h = integral(getX(mouse))
#text(h)
#speed = P3C(getY(mouse)+1, -h, 0)
text(speed)
camera.position = P3(0, -5, .4) + integral(speed)

camera.hpr = P3toHPR(speed)+ HPR(pi, 0, 0)
start()
