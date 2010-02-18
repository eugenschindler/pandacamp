from Panda import *
# This is an example of what you can do with a group of photos.
# This used cylindrical coordinates to make a wheel of pictures.

# Give the wheel an interesting trajectory and add some of your own
# pictures to it.


def wheel(p):
    total = len(p)
    radius = 1
    height = 1
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

w = wheel(["earthmap1k.jpg", "moonmap1k.jpg", "earthlights1k.jpg", "moonbump1k.jpg"])
w.hpr = HPR(time, 0,0)

mouseControlCamera(camera)
start()