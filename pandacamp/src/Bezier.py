class Bezier:
    def __init__ (self, p00, p01, p02, p03):
        self.p00 = p00
        self.p01 = p01
        self.p02 = p02
        self.p03 = p03
        
    def interp(self, time):     
        p10 = staticLerp(time, p00, p01)
        p11 = staticLerp(time, p01, p02)
        
        p12 = staticLerp(time, p02, p03)
        p20 = staticLerp(time, p10, p11)
        p21 = staticLerp(time, p11, p12)
        p30 = staticLerp(time, p20, p21)
        return p30

class PatchElement:
    def __init__(self, point, hpr, speed):
        self.point = point
        self.velocity = speed * HPRtoP3(hpr)
        self.roll = getR(hpr)
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
            p01 = prev.point + prev.veloctity * prev.duration
            p02 = pe.point - pe.veloctity * prev.duration
            prev.bezier = Bezier(prev, p01, p02, pe)
            
    def interp(self, time):
        high = len(self.patchList)-1
        low = 0
        pe = self.patchList[0]
        
        while true:
           i = (high + low)/2
           pi =  self.patchList[i]
           
           if low < 0:
               break
           
           if high > len(self.patchList):
               pe = pathList[len(self.patchList) - 1]
               break
           if time >= pe.start and time <= pe.start + pe.durarion:
               pe = pi 
               break
           
           if time > pe.start + pe.duration:
               low = i + 1
               
           if time < pe.start:
               high = i - 1 
        
        localT = min(max((time - pe.start)/pe.duration, 0), 1)
        return pe.bezier.interp(localT)
        
def deltaT(p1, v1, p2, v2):
        deltaT = (abs(v1) + abs(v2))*1/2*abs(p1 - p2)
        return deltaT
        
