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

def triangle(p1, p2, p3, color = None, position = None, hpr = None, size = None, texture = None, texP1 = P2(0,0), texP2 = P2(1, 0), texP3 = P2(0, 1)):
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkKeyType("triangle", p1, P3Type, "p1")
    checkKeyType("triangle", p2, P3Type, "p2")
    checkKeyType("triangle", p3, P3Type, "p3")
    nodePath = mesh([p1, p2, p3], [texP1, texP2, texP3], [[0,1,2]], white)
    result = GeometryHandle(nodePath, position, hpr, size, color, texture)
    return result

def rectangle(p1, p2, p3, color = None, position=None, hpr=None, size=None, texture = None):
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkKeyType("rectangle", p1, P3Type, "p1")
    checkKeyType("rectangle", p2, P3Type, "p2")
    checkKeyType("rectangle", p3, P3Type, "p3")
    p4 = p3 + p2 - p1
    nodePath = mesh([p1, p2, p3, p4], [P2(0,0), P2(1,0), P2(0,1), P2(1,1)], [[0,1,2], [1, 2, 3]], white)
    result = GeometryHandle(nodePath, position, hpr, size, color, texture)
    return result

# This should be deleted - I've left it here to keep from killing old demos.  The only thing that rectangle
# can't do is place a different photo on each side.  That's not really important since you can glue two of these
# together.

#####Essentially just a rectangle, but with a texture instead?
def photo(p1, p2, p3, texture, reverseTexture=None, firstSide=True,position=None, hpr=None, size=None):
    checkKeyType("rectangle", p1, P3Type, "p1")
    checkKeyType("rectangle", p2, P3Type, "p2")
    checkKeyType("rectangle", p3, P3Type, "p3")
    p4 = p3 + p2 - p1
    checkKeyType("rectangle", texture, stringType, "texture")

    format = GeomVertexFormat.getV3c4t2()
    vdata = GeomVertexData('name', format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    normal = GeomVertexWriter(vdata, 'normal')
    color = GeomVertexWriter(vdata, 'color')
    texcoord = GeomVertexWriter(vdata, 'texcoord')

    vertex.addData3f(p1.x, p1.y, p1.z)
    texcoord.addData2f(0,0)

    vertex.addData3f(p2.x, p2.y, p2.z)
    texcoord.addData2f(1,0)

    vertex.addData3f(p3.x, p3.y, p3.z)
    texcoord.addData2f(0,1)

    vertex.addData3f(p4.x, p4.y, p4.z)
    texcoord.addData2f(1,1)

    prim = GeomTriangles(Geom.UHStatic)

    prim.addVertex(0)
    prim.addVertex(1)
    prim.addVertex(2)
    prim.closePrimitive()

    prim.addVertex(1)
    prim.addVertex(3)
    prim.addVertex(2)
    prim.closePrimitive()

    geom = Geom(vdata)
    geom.addPrimitive(prim)

    node = GeomNode('gnode')
    node.addGeom(geom)

    nodePath = render.attachNewNode(node)
    nodePath.setTwoSided(False)


    result = GeometryHandle(nodePath, position, hpr, size)

    tex = loader.loadTexture(g.pandaPath+"/pictures/"+texture)
    if tex == None:
        print "Texture file " + texture + " not found."
        exit()
    nodePath.setTexture(tex)
    if firstSide:
      if reverseTexture is None:
        reverseTexture = texture
      reverseSide = photo(p2, p1, p4, reverseTexture, firstSide=False,position= position, hpr=hpr, size=1)
      reverseSide.reparentTo(result)
    return result


    