from Panda import*

class Bezier:
    def __init__ (self, p00, p01, p02, p03):
        self.p00 = p00
        self.p01 = p01
        self.p02 = p02
        self.p03 = p03
        
    def interp(self, time):     
        p10 = staticLerp(time, self.p00, self.p01)
        p11 = staticLerp(time, self.p01, self.p02)
        p12 = staticLerp(time, self.p02, self.p03)
        p20 = staticLerp(time, p10, p11)
        p21 = staticLerp(time, p11, p12)
        p30 = staticLerp(time, p20, p21)
        return (p30, p21-p20)

class PatchElement:
    def __init__(self, point, hpr, speed):
        self.point = point
        self.velocity = speed * HPRtoP3(hpr)
        self.roll = hpr.r
        self.duration = 0
        self.start = 0
        
class Patch:
    def __init__ (self):
        self.patchList = []
        
    def add(self, point, hpr, speed):
        pe = PatchElement(point, hpr, speed)
        self.patchList.append(pe)
        
        if len(self.patchList) >= 2:
            prev = self.patchList[len(self.patchList)- 2]
            prev.duration = deltaT(pe.point, pe.velocity, prev.point, prev.velocity)
            pe.start = prev.start + prev.duration
            prev.rollFinal = hpr.r
            p01 = prev.point + prev.velocity * prev.duration
            p02 = pe.point - pe.velocity * prev.duration
            prev.bezier = Bezier(prev.point, p01, p02, pe.point)
            
    def interp(self, time):
        high = len(self.patchList)-1
        low = 0
        pe = self.patchList[0]
        
        while True:
           i = (high + low)/2
           pe1 =  self.patchList[i]
           
           if low > 0:
               break
           
           if high < len(self.patchList):
               pe = self.patchList[len(self.patchList) - 2]
               break
           if time >= pe.start and time <= pe.start + pe.duration:
               pe = pe1 
               break
           
           if time > pe.start + pe.duration:
               low = i + 1
               
           if time < pe.start:
               high = i - 1 
        
        localT = min(max((time - pe.start)/pe.duration, 0), 1)
        roll = staticLerp(localT, pe.roll, pe.rollFinal)
        pos, v = pe.bezier.interp(localT)
        hpr = sP3toHPR(v)
        return (pos, SHPR(pi+hpr.h, hpr.p, roll))
    
    def getPos(self, s):
        return lift(lambda t: self.interp(t)[0], "bezierControl", [numType], P3Type)(s)
    def getHPR(self, s):
        return lift(lambda t: self.interp(t)[1], "bezierControl", [numType], HPRType)(s)
    def duration(self):
        return self.patchList[len(self.patchList)- 1].start
    
    
def deltaT(p1, v1, p2, v2):
        distance = abs(p1 - p2)
        speed = (abs(v1) + abs(v2))*1/2
        deltaT = distance/speed
        return deltaT
        



#p = panda(position = P3C(1,time/5, sin(time*4)/5))
#pointForward(p)

#text(norm(deriv(p.position)))
#text(HPRtoP3(p.hpr))
'''
p = Patch()
p.add(P3(0,0,0), HPR(pi/2, 0, 0), 1)
p.add(P3(1,0,0), HPR(pi/2,2,0), 1)
p.add(P3(2,0,0), HPR(pi/2, 0,0), 2)
t = -0.1
while t< 5:

    panda(size = .05, position = p.interp(t))
    t = t +.1'''
sTime = slider(min = 0 , max = 1, label = "t")
speed = slider(max = 100, min = 1, label = "Speed")
b = button("Save Point")
bs = Patch()

def addPoint(m, v):
    cp = now(camera.position)
    chpr = now(camera.hpr)
    bs.add( cp, chpr, now(speed))
    bunny(position = cp, hpr = chpr)
    
react(b,addPoint)
rp = rbuttonPull

text(camera.position)
grassScene()
camera.hpr = HPR(getX(rp), getY(rp), 0)
v = choose(lbutton, -speed, 0)
pos = integral(v*HPRtoP3(camera.hpr))
camera.position = pos

pb = button("Preview")
cp = button("cameraPrev")


def camerapreview(m, v):
   camera.position = bs.getPos(sTime * bs.duration())
   camera.hpr = bs.getHPR(sTime*bs.duration())

   
react(cp, camerapreview)

def preview(m, v):
    t = 0
    while t< bs.duration():
        ppos, phpr = bs.interp(t)
        panda(size = .5, position = ppos, hpr = phpr)
        t = t +.1
        
        
react(pb, preview)


start()