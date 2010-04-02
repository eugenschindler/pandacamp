from Panda import *

#Static models and behaviors
camera.position = P3(0, -16, 0)
camera.hpr = HPR(0, 0, 0)

#three pandas rotating on H P and R respectively
panda(position = P3(-1.5,0,0), hpr = HPR(time,0,0))
panda(position = P3(.5,0,0), hpr = HPR(0,time,0))
panda(position = P3(2.5,0,0), hpr = HPR(0,0, time))



#control RGB of point light
r1 = slider(max = 1, min = 0, label="Red 1")
g1 = slider(max = 1, min = 0, label="Green 1")
b1 = slider(max = 1, min = 0, label="Blue 1")
color1 = color(r1, g1, b1)
#control RGB of ambient light
r2 = slider(max = 1, min = 0, label="Red 2")
g2 = slider(max = 1, min = 0, label="Green 2")
b2 = slider(max = 1, min = 0, label="Blue 2")
color2 = color(r2, g2, b2)

#slider that controls position of point light 1
pl1 = slider(max = 7, min = 0, label="Position 1")

#slider that controls position of point light 2
pl2 = slider(max = 7, min = 0, label="Position 2")

lightpos1 = P3C(4, pl1, .25)
lightpos2 = P3C(4, pl2, .25)
#a small panda matching the movement of the light source
sphere(position = lightpos1, size = .2, color = color1)
sphere(position = lightpos2, size = .2, color = color2)
#the point light source
pointlight(color = color1, position = P3C(4, pl1, .25))
pointlight(color = color2, position = P3C(4, pl2, .25))
#an ambient light source
al = ambientlight(color = color(.4, .4, .4))
world.color = black

# Note how the different colors of light blend.  Try some other models
# besides the pandas.  Make the lights move on their own instead of with a slider.

# Try lightpos1 = P3C(4, pl1, .25) - P3(4,0,0)


start()
