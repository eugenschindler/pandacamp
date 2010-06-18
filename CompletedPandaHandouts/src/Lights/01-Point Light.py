from Panda import *
# This is a scene with three moving pandas:

camera.position = P3(0, -16, 0)
camera.hpr = HPR(0, 0, 0)
world.color = black
#three pandas rotating on H P and R respectively
p1 = panda(position = P3(-1.5,0,0), hpr = HPR(time,0,0))
p2 = panda(position = P3(.5,0,0), hpr = HPR(0,time,0))
p2 = panda(position = P3(2.5,0,0), hpr = HPR(0,0, time))

# When you don't specify a light source by default you get what is called
# ambient light (light that comes from no direction)

# When you add a light source of your own, this ambient light is turned off.

# Note that there is a black background behind the pandas - there is no light
# except for the point light

lightplace = P3(5, 0, 5)
lightcolor = white
# Change the color and location of the point light and see what happens.
# Try two different pointlights with two different locations and colors.

pointlight(position = lightplace, color = lightcolor)
pointlight(position = P3(0,5,-5), color = green)
start()
