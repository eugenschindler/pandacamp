from Panda import *

s = sphere(texture = "f.jpg")
s.size = -10
s.hpr=HPR(sin(time),time*2,cos(time))

# blastPicture takes a picture and slices it up into a bunch of rectangles.  Each of these has
# properties .x, .y, and .location.  If you put each fragment in its .location you'll see the picture
# is fully assembled.  

fragments = blastPicture("nic2.jpg", 5, 5)  # Cut a panda into 25 squares
for p in fragments:
    p.position = p.location
    p.hpr = HPR(time*random01(), cos(time*sin(time)), 0)

c = cube("smile.jpg", "action.jpg", "nic3.jpg", "nic.jpg", "nic2.jpg", "nic3.jpg")
c.hpr=HPR(time,step(time-5)*time/2,0)
c.position = P3(-2,0,0)
c.size = 0.5
ralph(position = P3(0,0,1.5),hpr=HPR(time,sin(time*2)/2,0))
text("Nic", position = P2(0,-.8), size= 2, color = purple)
c2 = cube("reach.jpg", "nic2.jpg", "repell.jpg", "nic.jpg", "climb.jpg", "nic3.jpg")
c2.hpr=HPR(-time,step(time- 5)*time/2,0)
c2.position = P3(2,0,0)
c2.size = 0.5
play("ChickenDanceCUT.wav")
start()