from Panda import *
lightlocation = P3C(2, time/2, sin(time)*3)
lightcolor = white
ambientlight( color = color(.4*sin(time)+.4, .4, .4))
pointlight(color = lightcolor, position = lightlocation)
sphere(position = lightlocation, size = .3, color = color(.4*sin(time)+.1, .5, .5))
# These are 3 corners of the photo
p1 = P3(1,0,-1)
p2 = P3(-1,0,-1)
p3 = P3(1,0,1)
# Place photos in /panda/lib/pictures - you can change these to any photo
# in this area.  If you only give one .jpg to photo it will be the
# same on both sides.
photo = photo(p1,p2,p3, "koolz.JPG")

pos = at(P3(-3,0,0))+to(3,P3(0,2,2.5))+to(3, P3(3,0,1))+to(4,P3(0,2.5,-2.5))
orient = at(HPR(0,0,0))+to(1.5,HPR(pi/6, pi/6, pi/4))

photo.position = itimef(pos)
photo.hpr = itimef(orient)

# Add another photo to the scene and give it an interesting trajectory.
# Change the size as it moves.

start()