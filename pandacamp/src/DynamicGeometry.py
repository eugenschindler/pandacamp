import g

from Types import *
from Handle import *
from sys import exit

class GeometryHandle(Handle):
    def __init__(self, object, position=None, hpr=None, size = 1, color = None, texture = None):
        Handle.__init__(self, name="dynamicGeometry")
        self.d.model = object
        self.d.onScreen = False
        ctl = newSignalRefd(self, "control", controlType, scEmptyControl)
        self.__dict__["control"] = ctl
        self.__dict__['position'] = newSignalRefd(self, 'position', P3Type, P3(0,0,0), ctl)
        self.__dict__['hpr']   = newSignalRefd(self, 'hpr', HPRType, HPR(0,0,0), ctl)
        self.__dict__['size'] = newSignalRefd(self, 'size', numType, 1, ctl)
        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType, noColor, ctl)
        if size is not None:
             self.size.setBehavior(size)
        if position is not None:
             self.position.setBehavior(position)
        if hpr is not None:
             self.hpr.setBehavior(hpr)
        if color is not None:
             self.color.setBehavior(color)
        if texture is not None:
          tex = loader.loadTexture(g.pandaPath+"/pictures/"+texture)
          self.d.model.setTexture(tex)
        g.newModels.append(self)
    def refresh(self):
        Handle.refresh(self)
        p = self.position.now()
        self.d.model.setPos(p.x, p.y, p.z)
        d = self.hpr.now()
        self.d.model.setHpr(degrees(d.h), degrees(d.p), degrees(d.r))
        self.d.model.setScale(self.size.now())
        c = self.color.now()
        if c.a != 0:   # This signals that there is no color to paint on the model
           self.d.model.setColor(c.toVBase4())
    def kill():
        self.d.model.hide()
    def show():
        self.d.model.show()
    def reparentTo(self, handle):
        self.d.model.reparentTo(handle.d.model)
    def setTexture(self, texture):
        tex = loader.loadTexture(g.pandaPath +"/pictures/"+ texture)
        self.d.model.setTexture(tex)
    def setTexture2(self, texture):
        if self.d.twoSided:
            self.d.sideTwo.setTexture(texture)

# This creates a model on the fly.  The array of spacePoints and texturePoints have to be the same length.
# The spacePoints contains P3 objects and texturePoints contains P2 objects.
# The triangles array contains triples of points, one for each triangle.
# The color is just a default - either color or texture override this.

def mesh(spacePoints, texturePoints, triangles, c):
#getV3c4t2() means 3-dimensional Vector, 4-dimensional Color and 2-dimensional Texture Coordinates.
    format = GeomVertexFormat.getV3c4t2()

#####I believe this provides a link of some sort to the Geom.UHStatic collection of vertices.
#####This seems to be a necessary step to making the shapes appear on the screen.
    vdata = GeomVertexData('name', format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    normal = GeomVertexWriter(vdata, 'normal')
    color = GeomVertexWriter(vdata, 'color')
    texcoord = GeomVertexWriter(vdata, 'texcoord')
    for p in spacePoints:
        vertex.addData3f(p.x, p.y, p.z)
        color.addData4f(c.r, c.g, c.b, c.a)
    for p in texturePoints:
        texcoord.addData2f(p.x, p.y)
    geom = Geom(vdata)
    for triangle in triangles:

    #GeomTriangles contains a number of disconnected triangles, all apparently stored in a big pile.
        prim = GeomTriangles(Geom.UHStatic)

#####This seems to take the points we added in earlier and remove them.
#####Why this is all static, I don't understand.
        prim.addVertex(triangle[0])
        prim.addVertex(triangle[1])
        prim.addVertex(triangle[2])
        prim.closePrimitive()

    #Converting the vertices we just retrieved from the collection inside Geom.UHStatic into a node
#####
    
        geom.addPrimitive(prim)

    node = GeomNode('gnode')
    node.addGeom(geom)

    #Adds the node we've just made into the render path, therefore making it appear on screen.
#####I believe that if we want an actory-thing, this might be the place to do it.
    nodePath = render.attachNewNode(node)
    nodePath.setTwoSided(True)
    return nodePath

def emptyModel(color = None, position = None, hpr = None, size = None):
    nodePath = mesh([],[], [], white)
    result = GeometryHandle(nodePath, position, hpr, size, color, None)
    return result

def triangle(p1, p2, p3, color = None, position = None, hpr = None, size = None, texture = None, texP1 = P2(0,0), texP2 = P2(1, 0), texP3 = P2(0, 1), side2 = None):
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkKeyType("triangle", p1, P3Type, "p1")
    checkKeyType("triangle", p2, P3Type, "p2")
    checkKeyType("triangle", p3, P3Type, "p3")
    nodePath = mesh([p1, p2, p3], [texP1, texP2, texP3], [[0,1,2]], white)
    if (side2 is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position, hpr, size, color, texture)
        if side2 is not False:
            otherSide = triangle(p2, p1, p3, texture = side2, side2 = False, texP1 = texP1, texP2 = texP2, texP3 = texP3)
            otherSide.reparentTo(result)
            result.d.twoSided = True
            result.d.sideTwo = otherSide
        return result
    result = GeometryHandle(nodePath, position, hpr, size, color, texture)
    result.d.twoSided = False
    return result

def rectangle(p1, p2, p3, color = None, position=None, hpr=None, size=None, texture = None, side2 = None,
              texP1 = P2(0,0), texP2 = P2(1,0), texP3 = P2(0,1), texP4 = P2(1,1)):
    # If side2 is a string, it is interpreted as a file name in the pictures area
    # If side2 is False, the texture is one sided (invisible from the back)
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkKeyType("rectangle", p1, P3Type, "p1")
    checkKeyType("rectangle", p2, P3Type, "p2")
    checkKeyType("rectangle", p3, P3Type, "p3")
    p4 = p3 + p2 - p1
    nodePath = mesh([p1, p2, p3, p4], [texP1, texP2, texP3, texP4], [[0,1,2], [2, 1, 3]], white)
    if (side2 is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position, hpr, size, color, texture)
        if side2 is not False:  
            otherSide = rectangle(p2, p1, p4, texture = side2, side2 = False, texP1 = texP1, texP2 = texP2, texP3 = texP3, texP4 = texP4)
            otherSide.reparentTo(result)
            result.d.twoSided = True
            result.d.sideTwo = otherSide
        return result
    result = GeometryHandle(nodePath, position, hpr, size, color, texture)
    result.d.twoSided = False
    return result

def unitSquare(**a):
    return rectangle(P3(-1, 0, -1), P3(1, 0, -1), P3(-1, 0, 0), **a)

def photoWheel(p, radius = 1.2, height = 1.2):
    total = len(p)
    center = emptyModel()
    for i in range(total):
      r = (2*pi/total)*i
      r2 = (2*pi/total)*(i+1)
      p1 = P3C(radius, r, height)
      p2 = P3C(radius, r, 0)
      p3 = P3C(radius, r2, 0)
      ph = rectangle(p2,p3,p1, texture = p[i])
      ph.reparentTo(center)
    return center

def cube(t1, t2, t3, t4, t5, t6):
    center = emptyModel()
    v1 = P3(1,1,1)
    v2 = P3(1,1,-1)
    v3 = P3(1, -1, 1)
    v4 = P3(1, -1, -1)
    v5 = P3(-1,1,1)
    v6 = P3(-1,1,-1)
    v7 = P3(-1, -1, 1)
    v8 = P3(-1, -1, -1)
    f1 = rectangle(v8, v4, v7, texture = t1)
    f2 = rectangle(v4, v2, v3, texture = t2)
    f3 = rectangle(v2, v6, v1, texture = t3)
    f4 = rectangle(v6, v8, v5, texture = t4)
    f5 = rectangle(v7, v3, v5, texture = t5)
    f6 = rectangle(v2, v6, v4, texture = t6)
    f1.reparentTo(center)
    f2.reparentTo(center)
    f3.reparentTo(center)
    f4.reparentTo(center)
    f5.reparentTo(center)
    f6.reparentTo(center)
    return center