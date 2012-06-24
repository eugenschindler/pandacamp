             # allow use of actor
from direct.gui.DirectGui import *            # 2D GUI elements
from Maze import *
from Racetrack import *
from World import *
from Time import *
from Color import *
from Models import *
from Handle import *
from Numerics import *
from StaticNumerics import randomChoice, random01, random11, randomInt, shuffle
from Slider import *
from Text import *
from Signal import time, static
from FRP import *
# from Switch import *
from Light import *
from Sound import *
from Button import *
from Menu import *
from PEffect import *
from DynamicGeometry import *
from Interp import *
from TextBox import *
from PoseAndScriptFiles import *
from Utils import *
from Roll import *
from g import*

class Bezier:
    def __init__ (self, p00, p01, p02, p03):
        self.p00 = p00
        self.p01 = p01
        self.p02 = p02
        self.p03 = p03
#        bunny(position = self.p00)
#        bunny(position = self.p01)
#        bunny(position = self.p02)
#        bunny(position = self.p03)
#        print "p00 "+ str(p00)
#        print "p01 "+ str(p01)
#        print "p02 "+ str(p02)
#        print "p03 "+ str(p03)

    def interp(self, time):
        p10 = staticLerp(time, self.p00, self.p01)
        p11 = staticLerp(time, self.p01, self.p02)
        p12 = staticLerp(time, self.p02, self.p03)
        p20 = staticLerp(time, p10, p11)
        p21 = staticLerp(time, p11, p12)
        p30 = staticLerp(time, p20, p21)
        #print "p10 "+ str(p10)
        #print "p11 "+ str(p11)
        #print "p12 "+ str(p12)
        #print "p20 "+ str(p20)
        #print "p21 "+ str(p21)
        #print "p30 "+ str(p30)
        return (p30, p21-p20)

class PatchElement:
    def __init__(self, point, hpr, speed):
        self.point = point
        self.velocity = speed * HPRtoP3(hpr)
        self.roll = hpr.r
        self.duration = 0
        self.start = 0
        self.hpr = hpr
        self.speed = speed

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
            p01 = prev.point - prev.velocity * prev.duration*(1.0/3)
            p02 = pe.point + pe.velocity * prev.duration*(1.0/3)
            prev.bezier = Bezier(prev.point, p01, p02, pe.point)

    def interp(self, time):
        high = len(self.patchList)-2
        low = 0
        if time < 0:
            pe = self.patchList[0]
        elif(time >= self.duration):
            pe = self.patchList[high]
        else:
            while True:
               i = int((high+low)/2)
               pe1 =  self.patchList[i]

               if time >= pe1.start and time <= pe1.start + pe1.duration:
                   pe = pe1
                   break

               if time > pe1.start:
                   low = i + 1

               else:
                   high = i - 1

        localT = min(max((time - pe.start)/pe.duration, 0), 1)
        roll = staticLerpA(localT, pe.roll, pe.rollFinal)
        pos, v = pe.bezier.interp(localT)
        print "velocity "+str(v)
        hpr = sP3toHPR(v)
        print "hpr "+ str(hpr)
        return (pos, SHPR(pi+hpr.h, hpr.p, roll))

    def getPos(self, s):
        return lift(lambda t: self.interp(t)[0], "bezierControl", [numType], P3Type)(s)
    def getHPR(self, s):
        return lift(lambda t: self.interp(t)[1], "bezierControl", [numType], HPRType)(s)
    def duration(self):
        return self.patchList[len(self.patchList)- 1].start
    def saveToFile(self, fname):
        file = g.pandaPath + "/Scripts/" + fname + ".csv"
        result = []
        for patch in self.patchList:
            result.append(str(patch.point.x) + "," + str(patch.point.y) + "," + str(patch.point.z) + "," +
                          str(patch.hpr.h) + ", " + str(patch.hpr.p) + ", " + str(patch.hpr.r) + "," +
                          str(patch.speed) + "\n")
        saver = open(file ,"w")
        saver.writelines(result)
        saver.close()
        status.set("Path " + fileName + " written to disk")


def deltaT(p1, v1, p2, v2):
        distance = abs(p1 - p2)
        speed = (abs(v1) + abs(v2))*1/2
        deltaT = distance/speed
        return deltaT



#p = panda(position = P3C(1,time/5, sin(time*4)/5))
#pointForward(p)

#text(norm(deriv(p.position)))
#text(HPRtoP3(p.hpr))

def saveCamera(name):
    status = var("Ready")
    text(status, position = P2(0, .95))
    text(" ")
    text(format("Camera: %s", camera.position))
    sTime = slider(min = 0 , max = 1, label = "t", position = P2(.8, .8))
    speed = slider(max = 100, min = 1, label = "Speed", position = P2(.8, .72))
    roll = slider(max = 2*pi, label = "Roll", position = P2(.8, .64))
    spb = button("Save Point")
    sfb = button("Save File")
    pathb = button("Show Path")
    pvb = button("Preview")
    spline = Patch()
    previewing = var(0)
    rp = rbuttonPull
    def addPoint(m, v):
        cp = now(camera.position)
        chpr = now(camera.hpr)
        spline.add( cp, chpr, now(speed))
        status.set("Added a point at " + str(cp) + " hpr = " + str(chpr))  # Should say where and how many
        #bunny(position = cp, hpr = chpr)
        
    react(spb,addPoint)
    def camerapreview(m, v):
        if now(previewing) == 0:
            camera.position = spline.getPos(sTime * bs.duration())
            camera.hpr = spline.getHPR(sTime*bs.duration())
            status.set("Preview mode - move camera with time slider")
        else:
            camera.hpr = HPR(getX(rp), getY(rp), roll)  # Control the camera hpr with the
            v = choose(lbutton, -speed, 0)  # left button to move
            pos = now(camera.position) + integral(v*HPRtoP3(camera.hpr))
            camera.position = pos
            status.set("Exiting preview mode")
        previewing.set(1-now(previewing))
    react(pvb, camerapreview)

    def preview(m, v):
        t = 0
        while t< bs.duration():
            ppos, phpr = bs.interp(t)
            panda(size = .5, position = ppos, hpr = phpr)
            t = t +.1
        status.set("Camera path visualized")
        #  Add bunnies
    react(pathb, preview)

    def saveFile(m, v):
        spline.saveToFile(name)
        status.set("Saved to file")
    react(sfb, saveFile)
    #text(format("Camera is at %f", camera.position))
    camera.hpr = HPR(getX(rp), getY(rp), roll)  # Control the camera hpr with the
    v = choose(lbutton, -speed, 0)  # left button to move
    pos = integral(v*HPRtoP3(camera.hpr))
    camera.position = pos


def launchCamera(fileName):
    spline = Patch()
    file = findCSV(fileName)
    if file is not None:
        fileLoader = open(file,  "r")
        contents = fileLoader.read().split("\n")
        for line in contents:
            data = line.split(",")
            if len(data) == 7:
                    x = float(data[0].strip())
                    y = float(data[1].strip())
                    z = float(data[2].strip())
                    h = float(data[3].strip())
                    p = float(data[4].strip())
                    r = float(data[5].strip())
                    speed = float(data[6].strip)
                    hpr = HPR(h, p, r)
                    point = P3(x,y,z)

                    spline.add(point, hpr, speed)
        fileLoader.close()
        # Fly the camera here
    else:
        print "File " + fileName + " not found."

