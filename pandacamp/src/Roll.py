from Numerics import *
from World import *
from FRP import *
from StaticNumerics import *

def surfaceNormal(f, p):
    delta = 0.001
    p1 = SP3(p.x + delta, p.y, f(p.x + delta, p.y))
    p2 = SP3(p.x, p.y + delta, f(p.x, p.y + delta))
    a = p1 - p
    b = p2 - p
    return normP3(crossProduct(a, b))

def rotate(ball, ballV, f, p):
    UP = surfaceNormal(f, p)
    prevRot = LRotationf(ball.getQuat())
    axis = UP.cross(ballV)
    newRot = LRotationf(axis, 45.5 * dt * ballV.length())
    ball.setQuat(prevRot * newRot)