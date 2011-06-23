from Numerics import *
from World import *
from FRP import *
from StaticNumerics import *
from DynamicGeometry import *

def surfaceNormal(f, p):
    delta = 0.001
    p1 = SP3(p.x + delta, p.y, f(p.x + delta, p.y))
    p2 = SP3(p.x, p.y + delta, f(p.x, p.y + delta))
    a = p1 - p
    b = p2 - p
    return normP3(crossProduct(a, b))

def rotateTextureOnBall(ball, ballV, UP, angle):
    prevRot = LRotationf(ball.getQuat())
    axis = UP.cross(ballV)
    newRot = LRotationf(axis, degrees(angle)) #45.5*200 * ballV.length())  # Removed dt since ballV is already scaled by dt
    ball.setQuat(prevRot * newRot)
    
    
def parX(f, p):
    delta = 0.001
    return (f(p.x + delta, p.y)-f(p.x, p.y)) / delta
 
def parY(f, p):
    delta = 0.001
    return(f(p.x, p.y + delta)-f(p.x, p.y)) / delta

def rollTexture(model,surface, contact, p0):
    def f(s, newPos):
        oldPos = s
        v = newPos - oldPos
        vdir = normP3(v)
        angle = absP3(v)/model.size.now()
        bv = Vec3(vdir.x, vdir.y, vdir.z)
        norm = surface.sNormal(newPos.x, newPos.y)
        nv = Vec3(norm.x, norm.y, norm.z)
        rotateTextureOnBall(model.d.model, bv, nv, angle)
        ballCenter = newPos + model.size.now()*norm
        return (newPos, ballCenter)
    model.position = tracker(f, p0, contact, P3Type)
    model.d.noHPR = True

def golfCourse(h,w,fn, ballp0):
    wall = P3(0,0,1)
    p1 = P3(0,0,0)
    p2 = P3(w,0,0)
    p3 = P3(w,h, 0)
    p4 = P3(0,h,0)
    
    r1 = rectangle(p1, p2, p1 + wall, color = brown)
    r2 = rectangle(p2, p3, p2 + wall, color = brown)
    r3 = rectangle(p3, p4, p3 + wall, color = brown)
    r4 = rectangle(p4, p1, p4 + wall, color = brown)
    
    s = surface(fn, xmin = 0, ymin = 0, xmax = w, ymax = h, texture = "grass.jpg")
    return s
    
    
def rollSphere(model, surface, x0, y0, xv0, yv0, g = -9.8, drag = .2):
    setType(model.xpos, numType)
    setType(model.ypos, numType)
    setType(model.xv, numType)
    setType(model.yv, numType)
    setType(model.xa, numType)
    setType(model.ya, numType)
    dx = surface.dx(model.xpos, model.ypos)
    dy = surface.dy(model.xpos, model.ypos)
    den = (1 + dx*dx + dy*dy)
    model.xa = g * dx/den - drag*model.xv
    model.ya = g * dy/den - drag*model.yv
    model.xv = integral(model.xa) + xv0    
    model.yv = integral(model.ya) + yv0
    model.xpos = integral(model.xv) + x0    
    model.ypos = integral(model.yv) + y0
    rollTexture(model, surface, P3(model.xpos, model.ypos, surface.f(model.xpos, model.ypos)), P3(x0, y0, surface.f(x0, y0)))
