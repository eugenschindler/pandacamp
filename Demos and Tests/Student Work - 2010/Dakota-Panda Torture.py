# intro to Panda/08-mouse.py
from Panda import *

# Use the mouse to control your panda
# Mouse values are in P2(-1,-1) to P2(1,1)

# Show where the mouse currently is usint text()
camera.position = P3(0, -16, 0)
camera.hpr = HPR(0, 0, 0)
world.color = black
pl1=pointLight(position = P3(0,0,0))
pl2=PLight(position = P3(2,0,0))
pl3=pointLight(position = P3(-2,0,0))
ambientLight (color=red)
pl1.color = interpolate(time, forever(at(orange) + to(4, red) + to(4, blue)+ to (4,orange)))
pl2.color = interpolate(time, forever(at(orange) + to(4, red) + to(4, blue)+ to (4,orange)))
pl3.color = interpolate(time, forever(at(orange) + to(4, red) + to(4, blue) + to (4,orange)))
# How can you get the mouse value to cover a specific range?
# Change parameters so that the mouse is controlling the panda's
# position or hpr.
# Use getX and getY to take just the X or Y coordinate out of the
# mouse position.
Evil =sound("evilLaugh.wav")
text ("press k to kill panda 1")
text ("press s to kill panda 2")
text ("press t to kill panda 3")
text ("press p to PURGE")
text ("press d to reset")
text ("press a to Create new pandas")


p = panda(hpr=HPR(0,time/2,0),position=P3(0,0,0))
p1 = panda(hpr=HPR(0,time/2,0),position=P3(2,0,0))
p2 = panda(hpr=HPR(0,time/2,0),position=P3(-2,0,0))
f= fireish (position=P3 (0,50000,0))
pl1=pointLight(position = P3(0,0,0))
pl2=pointLight(position = P3(2,0,0))
pl3=pointLight(position = P3(-2,0,0))
p.color = interpolate(time, forever(at(orange) + to(4, red) + to(4, blue)+ to (4,orange)))
p1.color = interpolate(time, forever(at(orange) + to(4, red) + to(4, blue)+ to (4,orange)))
p2.color = interpolate(time, forever(at(orange) + to(4, red) + to(4, blue) + to (4,orange)))
def kkey(m, v):
    f=fireish(position=m.position)
    f.react1 (key ("d"),Reset)
    Evil.play ()
    m.exit()
def Reset(m, v):
    m.stop()
def pkey1(m, v):
    w = warpFace (position=P3 (0,0,0),texture="explosion.png")
    w.react1(key('d'), Reset)
    w.react1 (key ('d'),Reset)
def pkey (m,v):
    m.exit ()

def End (m,v):
    pass

def Create (m,v):
    p=panda (position =P3(0,-localTime*2,0),size=random01()*1+.5,hpr=HPR(0,localTime,0))
    p1=panda (position =P3(1,-localTime*2,0),size=random01()*1+.5,hpr=HPR (0,localTime,0))
    p2=panda (position =P3(-1,-localTime*2,0),size=random01()*1+.5,hpr=HPR (0,localTime,0))
    p.react1(key('k'),kkey)
    p.react1(key('p'),pkey)
    p1.react(key('s'),kkey)
    p1.react(key('p'),pkey)
    p2.react(key('p'),pkey)
    p2.react(key('t'),kkey)
    #n.stop ()








    
    
react (key ("a"),Create)
#n.react (key ("p"),End)
#p.react (key ("d"),End)
p.react(key('k'),kkey)
p1.react(key('s'),kkey)
p2.react(key('t'),kkey)
p.react(key('p'),pkey)
p1.react(key('p'),pkey)
p2.react(key('p'),pkey)
react(key('p'), pkey1)
start()