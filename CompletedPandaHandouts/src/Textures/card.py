from Panda import *
cp0 = color(.2,0,0)
cp1 = color(.2,1,.01)
cp2 = color(.2,0,.5)
cp3 = color(0,0,0)
world.color = itimef(at(cp0) + to(1,cp1)+ to(2, cp2)+ to(1,cp3))

r2 = r2d2(position = P3(1, 5, 1), size = 2)
r2.setTexture("r2strange.png")

# These are 3 corners of the photo
xp1 = P3(1,0,-1)
xp2 = P3(-1,0,-1)
xp3 = P3(1,0,1)
# Place photos in /panda/lib/pictures - you can change these to any photo
# in this area.  If you only give one .jpg to photo it will be the
# same on both sides.


xp = photo(xp1,xp2,xp3, "wave.jpg")

xpos = P3(time-3, 0, sin(time*3))

xorient = at(HPR(0,0,0))+to(1, HPR(0,0,0)) + to(.5, HPR(0,0,pi)) + to(.5, HPR(0,0,2*pi-.01))

xp.position = xpos
xp.hpr =itimef(xorient)

xd = photo(xp1,xp2,xp3, "holdon.jpg")
xi1 = at(P3(-3, 0, -3)) + to (3,P3(2,0,2)) + to (2, P3(2,3,-99)) + to (9999, P3 (0,0,-999999))
xd.position = itimef(xi1)
xd.hpr = HPR(time*5, 0, 0)


lightlocation = P3C(4, time*2, 1)
lightlocation2 = P3C(3, time*5,3)
lightlocation3 = P3C(2, time*7, 2)
lightcolor = color(0,0,1)
lightcolor2 = color(1,0,0)
lightcolor3 = color(0,1,0)
ambientlight(color = gray)
soccerBall(position = lightlocation, size = .1)
soccerBall(position = lightlocation2, size = .1)
soccerBall(position = lightlocation3, size = .1)


pointlight(color = lightcolor, position = lightlocation)
pointlight(color = lightcolor2, position = lightlocation2)
pointlight(color = lightcolor3, position = lightlocation3)


bu = bunny()
bu.size = 4
bu.setTexture("bunny.png")
bu.position = P3C (3,time,abs(sin(time*5)))+P3(1, 5, 1)
bu.hpr = HPR(time+pi,0,0)
def wheel(p):
    total = len(p)
    radius = 1.2
    height = 1.2
    cp = P3(0,0,0)
    center = triangle(cp,cp,cp, white)

    for i in range(total):
      r = (2*pi/total)*i
      r2 = (2*pi/total)*(i+1)
      p1 = P3C(radius, r, height)
      p2 = P3C(radius, r, 0)
      p3 = P3C(radius, r2, 0)
      ph = photo(p2,p3,p1, p[i])
      ph.reparentTo(center)
    return center

w = wheel(["Ryan.JPG", "bo.JPG", "Justin.JPG", "matt.jpg", "Bec's REZ.JPG"])
w.hpr = HPR(time*1.5, 0,0)
w.size = 2
i = at(P3(-12, 0, -2)) + to(3, P3(2, 2, 2)) + to(3, P3(2,2,-4)) + to(3, P3(-2,0,2)) + to(3, P3(-2,0,-2))
w.position = itimef(i)

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
# s=r2d2 (position = P3(3.5,2,-3),hpr = HPR(time*2,0,0))
# s.setTexture("r2.png")

start()
