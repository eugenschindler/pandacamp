from Panda import *
# You can add more photos to your nametag by placing some geometric solids in your animation

# You can put an arbitrary number of photos in a wheel, 6 photos on a cube, or 4 on a tetrahedron

a = photoWheel(["picture.jpg", "van.jpg", "hurst.jpg" ,"raft.jpg", "talk.jpg", "camplogo.jpg", "rocks.jpg"])
b = photoWheel(["picture.jpg", "van.jpg", "hurst.jpg" ,"raft.jpg", "talk.jpg", "camplogo.jpg", "rocks.jpg"])

a.hpr = HPR(0, cos(time), time*1)
a.position = P3(-2,0,1)
grassScene (position = P3(1,0,0))
b.hpr = HPR(time*1, sin(time), 0)
b.position = P3 (2,0,1)
p = r2d2 ()
p.hpr = HPR (1.5,0,0)
path = at(P3(-4,0,-2)) + to(4, P3(4, 0, -2)) 
p.position = itime(repeat (999,path))
fireish (position = a.position)
fireish (position = b.position)
#cube(t1, t2, t3, t4, t5, t6)

from Panda import *


# blastPicture takes a picture and slices it up into a bunch of rectangles.  Each of these has
# properties .x, .y, and .location.  If you put each fragment in its .location you'll see the picture
# is fully assembled.  

fragments = blastPicture("picture.jpg", 5, 5)  # Cut a panda into 25 squares

for p in fragments:
    path = at (P3(randomRange(-3, 3),0, randomRange(-2, 2))) + to(3, p.location)+ to (1,p.location)

    p.position = itime(repeat (999,path))



start()

#tetra(t1, t2, t3, t4)


    
start()