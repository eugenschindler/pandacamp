import g
#Fixed up a small typo that was causing considerable issues with rectangles.
#Tried to add comments to make it at least a little more readable(to me, anyway)
#It all works fine now, though I'm not sure if it did or didn't before.
#I can make triangles, rectangles and photos(with mirror-reversal and everything)
#Comments with more than two leading hashes (#####) are usually notes to myself and are
# not usually very helpful to anyone else.
#~Kendric 5-29-08

from Types import *
from Handle import *
from sys import exit
import direct.directbase.DirectStart

class GeometryHandle(Handle):
    def __init__(self, object, position=None, hpr=None, size = 1):
        Handle.__init__(self, name="dynamicGeometry")
        self.d.model = object
        ctl = newSignalRefd(self, "control", controlType, scEmptyControl)
        self.__dict__["control"] = ctl
        self.__dict__['position'] = newSignalRefd(self, 'position', P3Type, P3(0,0,0), ctl)
        self.__dict__['hpr']   = newSignalRefd(self, 'hpr', HPRType, HPR(0,0,0), ctl)
        self.__dict__['size'] = newSignalRefd(self, 'size', numType, 1, ctl)
        if size is not None:
             self.size.setBehavior(size)
        if position is not None:
             self.position.setBehavior(position)
        if hpr is not None:
             self.hpr.setBehavior(hpr)
        g.newModels.append(self)
    def refresh(self):
        Handle.refresh(self)
        p = self.position.now()
        self.d.model.setPos(p.x, p.y, p.z)
        d = self.hpr.now()
        self.d.model.setHpr(degrees(d.h), degrees(d.p), degrees(d.r))
        self.d.model.setScale(self.size.now())
    def kill():
        self.d.model.hide()
    def show():
        self.d.model.show()
    def reparentTo(self, handle):
        self.d.model.reparentTo(handle.d.model)
    def setTexture(self, texture):
        tex = loader.loadTexture(g.pandaPath +"/pictures/"+ texture)
        self.d.model.setTexture(tex)

def triangle(p1, p2, p3, c, position = None, hpr = None, size = None):
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkKeyType("triangle", p1, P3Type, "p1")
    checkKeyType("triangle", p2, P3Type, "p2")
    checkKeyType("triangle", p3, P3Type, "p3")
    checkKeyType("triangle", c, ColorType, "c")

    #getV3c4t2() means 3-dimensional Vector, 4-dimensional Color and 2-dimensional Texture Coordinates.
    format = GeomVertexFormat.getV3c4t2()

#####I believe this provides a link of some sort to the Geom.UHStatic collection of vertices.
#####This seems to be a necessary step to making the shapes appear on the screen.
    vdata = GeomVertexData('name', format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    normal = GeomVertexWriter(vdata, 'normal')
    color = GeomVertexWriter(vdata, 'color')
    texcoord = GeomVertexWriter(vdata, 'texcoord')

    #Populates the vertex and color things with data from the three triangle points.
    vertex.addData3f(p1.x, p1.y, p1.z)
    color.addData4f(c.r, c.g, c.b, c.a)

    vertex.addData3f(p2.x, p2.y, p2.z)
    color.addData4f(c.r, c.g, c.b, c.a)

    vertex.addData3f(p3.x, p3.y, p3.z)
    color.addData4f(c.r, c.g, c.b, c.a)

    #GeomTriangles contains a number of disconnected triangles, all apparently stored in a big pile.
    prim = GeomTriangles(Geom.UHStatic)

#####This seems to take the points we added in earlier and remove them.
#####Why this is all static, I don't understand.
    prim.addVertex(0)
    prim.addVertex(1)
    prim.addVertex(2)
    prim.closePrimitive()

    #Converting the vertices we just retrieved from the collection inside Geom.UHStatic into a node
#####
    geom = Geom(vdata)
    geom.addPrimitive(prim)

    node = GeomNode('gnode')
    node.addGeom(geom)

    #Adds the node we've just made into the render path, therefore making it appear on screen.
#####I believe that if we want an actory-thing, this might be the place to do it.
    nodePath = render.attachNewNode(node)
    nodePath.setTwoSided(True)

    result = GeometryHandle(nodePath, position, hpr, size)

    return result

#####I would imagine that this would be very similar to the triangle,
##### so I won't put comments in until I have it all figured out.
def rectangle(p1, p2, p3, c, position=None, hpr=None, size=None):
    checkKeyType("rectangle", p1, P3Type, "p1")
    checkKeyType("rectangle", p2, P3Type, "p2")
    checkKeyType("rectangle", p3, P3Type, "p3")
    p4 = p3 + p2 - p1
    checkKeyType("rectangle", c, ColorType, "c")

    format = GeomVertexFormat.getV3c4t2()
    vdata = GeomVertexData('name', format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    normal = GeomVertexWriter(vdata, 'normal')
    color = GeomVertexWriter(vdata, 'color')
    texcoord = GeomVertexWriter(vdata, 'texcoord')

    #If any of these are p3 where p2 should be or any mix-up along those lines, it'll render incorrectly,
    # often just drawing a triangle.
    vertex.addData3f(p1.x, p1.y, p1.z)
    color.addData4f(c.r, c.g, c.b, c.a)

    vertex.addData3f(p2.x, p2.y, p2.z)
    color.addData4f(c.r, c.g, c.b, c.a)

    vertex.addData3f(p3.x, p3.y, p3.z)
    color.addData4f(c.r, c.g, c.b, c.a)

    vertex.addData3f(p4.x, p4.y, p4.z)
    color.addData4f(c.r, c.g, c.b, c.a)

    prim = GeomTriangles(Geom.UHStatic)

    prim.addVertex(0)
    prim.addVertex(1)
    prim.addVertex(2)
    prim.closePrimitive()

#  Second
    prim.addVertex(1)
    prim.addVertex(3)
    prim.addVertex(2)
    prim.closePrimitive()

    geom = Geom(vdata)
    geom.addPrimitive(prim)

    node = GeomNode('gnode')
    node.addGeom(geom)

    nodePath = render.attachNewNode(node)
    nodePath.setTwoSided(True)

    result = GeometryHandle(nodePath, position, hpr, size)

    return result

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
