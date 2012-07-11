from Panda import*

warpSpeed(position = P3(0,10,0))

def slide1():
    world.color = red
    warpSpeed(position = P3(0,10,0))
    a = photoWheel(["emacs-b-gone.jpg", "lunch.jpg", "sitting.jpg", "what.jpg"], size = 1.8)
    a.position = P3(0,0,-.5)
    a.hpr = HPR(time*.5, time*.0001, time*.0001)
    atTime(12,to2)
def to2():
    resetWorld()
    slide2()
   
    
def slide2():
    world.color = green
    warpSpeed(position = P3(0,10,0))
    fragments = blastPicture("thecar.jpg", 5, 5)
    for p in fragments:
        path = at(p.location) + to(2 + (p.x + 5*p.y)*.2, p.location) + to(4, P3(randomRange(-10,10), randomRange(-10,10), 6))
        p.hpr = HPR(randomRange(-3,3)*time,randomRange(-3,3)*time, randomRange(-3,3)*time)*step(localTime-(2+(p.x+5*p.y)*.2))
        p.position = interpolate(localTime, path)
    atTime(21,to3)

def to3():
    resetWorld()
    slide3()
    
def slide3():
    world.color = blue
    warpSpeed(position = P3(0,10,0))
    a = photoWheel(["downtheriver.jpg", "everate.jpg", "goingin.jpg", "rowing1.jpg", "goodtime.jpg", "intheheat.jpg"], size = 1.8)
    a.position = P3(0,0,-.5)
    a.hpr = HPR(time*.5, time*.0001, time*.0001)
    atTime(34,to4)

def to4():
    resetWorld()
    slide4()
   
    
def slide4():
    world.color = purple
    warpSpeed(position = P3(0,10,0))
    fragments = blastPicture("mache.jpg", 5, 5)
    for p in fragments:
        path = at(p.location) + to(2 + (p.x + 5*p.y)*.2, p.location) + to(4, P3(randomRange(-10,10), randomRange(-10,10), 6))
        p.hpr = HPR(randomRange(-3,3)*time,randomRange(-3,3)*time, randomRange(-3,3)*time)*step(localTime-(2+(p.x+5*p.y)*.2))
        p.position = interpolate(localTime, path)
    
    atTime(44,to5)

def to5():
    resetWorld()
    slide5()
    
def slide5():
    world.color = orange
    warpSpeed(position = P3(0,10,0))
    a = photoWheel(["floatingdown.jpg", "goingdown.jpg", "goinging1.jpg", "rowing2.jpg", "me.jpg", "ok.jpg"], size = 1.8)
    a.position = P3(0,0,-.5)
    a.hpr = HPR(time*.5, time*.0001, time*.0001)
    atTime(59,to6)
    

def to6():
    resetWorld()
    slide6()
   
    
def slide6():
    world.color = green
    warpSpeed(position = P3(0,10,0))
    fragments = blastPicture("group.jpg", 5, 5)
    #group.jpg.size = 
    for p in fragments:
        path = at(p.location) + to(2 + (p.x + 5*p.y)*.2, p.location) + to(4, P3(randomRange(-10,10), randomRange(-10,10), 6))
        p.hpr = HPR(randomRange(-3,3)*time,randomRange(-3,3)*time, randomRange(-3,3)*time)*step(localTime-(2+(p.x+5*p.y)*.2))
        p.position = interpolate(localTime, path)
    
    atTime(70,to7)
    
def to7():
    resetWorld()
    slide7()
    
def slide7():
    world.color = orange
    warpSpeed(position = P3(0,10,0))
    a = photoWheel(["theraft.jpg", "weee.jpg", "whereami.jpg", "wipe-out1.jpg", "wipe-out2.jpg", "you.jpg"], size = 1.8)
    a.position = P3(0,0,-.5)
    a.hpr = HPR(time*.5, time*.0001, time*.0001)
    atTime(88,to8)
    
def to8():
    resetWorld()
    slide7()
    
def slide8():
    world.color = blue
    warpSpeed(position = P3(0,10,0))
    a = photoWheel(["thedean.jpg", "thedean2.jpg", "thedaen3.jpg"], size = 1.8)
    a.position = P3(0,0,-.5)
    a.hpr = HPR(time*.5, time*.0001, time*.0001)
    












atTime(0,slide1)

start()