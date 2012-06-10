# Done

# This creates top level GUI signals and the world and cam objects.

import g  # Global names
import direct.directbase.DirectStart          # start panda
from direct.showbase import DirectObject      # for event handling
from direct.actor import Actor                # allow use of actor
from direct.gui.DirectGui import *
from panda3d.core import PandaNode,NodePath
from panda3d.core import ColorBlendAttrib
from panda3d.core import Vec4
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from copy import copy
from Handle import *
from FRP import tag, hold, typedVar
from direct.showbase.DirectObject import DirectObject
import sys,os
loadPrcFileData("", "prefer-parasite-buffer #f")
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import OnscreenText
from random import *

def makeFilterBuffer(srcbuffer, name, sort, prog):
    blurBuffer=base.win.makeTextureBuffer(name, 512, 512)
    blurBuffer.setSort(sort)
    blurBuffer.setClearColor(Vec4(1,0,0,1))
    blurCamera=base.makeCamera2d(blurBuffer)
    blurScene=NodePath("new Scene") 
    blurCamera.node().setScene(blurScene)
    shader = loader.loadShader(prog)
    card = srcbuffer.getTextureCard()
    card.reparentTo(blurScene)
    card.setShader(shader)
    return blurBuffer


class Glow():
    def __init__(self, name = 'glow', amount = 0):
        print "Glow enabled!"
        
        ## Glow by Adam Bell (ventosproject@gmail.com)
        ## with some original code from Kwasi Mensah (kmensah@andrew.cmu.edu)
        ## for PandaCamp (code.google.com/p/pandacamp/)
        
        #The shader is important (but yet a variable). 
        
        ## The next part I'll replace with a single file as soon 
        ## as I can work with variables in the *.SHA files.
        if amount == 0:
            print "glowShader set to it's default value of 1."
            amount = 1
        
        ## Custom number for a positive non-integer or above 4.
        if amount > 0:
            customFile = open('shaders/glowShader.sha', 'w')
            line1 = "//Cg\n"
            line2 = "//\n"
            line3 = "\n"
            line4 = "void vshader(float4 vtx_position : POSITION, \n"
            line5 = "            float2 vtx_texcoord0 : TEXCOORD0,\n"
            line6 = "            uniform float4x4 mat_modelproj,\n"
            line7 = "	     out float4 l_position : POSITION,\n"
            line8 = "	     out float2 l_texcoord0 : TEXCOORD0)\n"
            line9 = "{\n"
            line10 = "	l_position=mul(mat_modelproj, vtx_position);\n"
            line11 = "	l_texcoord0=vtx_texcoord0;\n"
            line12 = "}\n"
            line13 = "            \n"
            line14 = "void fshader(float2 l_texcoord0 : TEXCOORD0,\n"
            line15 = "       	     uniform sampler2D tex_0 : TEXUNIT0,\n"
            line16 = "	     out float4 o_color : COLOR)\n"
            line17 = "{\n"
            line18 = "	float4 texColor=tex2D(tex_0, l_texcoord0);\n"
            line19 = "	o_color=texColor*%s*(texColor.w - 0.5);\n" % amount
            line20 = "}\n"
            line21 = " "
            fileContent = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18, line19, line20, line21]
            customFile.writelines(''.join(fileContent))
            customFile.close()
            glowShader = loader.loadShader("shaders/glowShader.sha")
            print "glowShader set as " + str(amount) + "!"
            
        if amount < 0:
            raise TypeError('Only positive numbers work for the glowShader!')


        # except that only the glowing materials should show up nonblack.
        base.disableMouse()
        glowBuffer=base.win.makeTextureBuffer("Glow scene", 512, 512)
        glowBuffer.setSort(-3)
        glowBuffer.setClearColor(Vec4(0,0,0,1))
        
        glowCamera=base.makeCamera(glowBuffer, lens=base.cam.node().getLens())
        
        # Tell the glow camera to use the glow shader
        tempnode = NodePath(PandaNode("temp node"))
        tempnode.setShader(glowShader)
        glowCamera.node().setInitialState(tempnode.getState())
        
        # X and Y shaders to make the earlier "glowShader.sha" work (or effective).
        blurXBuffer=makeFilterBuffer(glowBuffer,  "Blur X", -2, "shaders/XBlurShader.sha")
        blurYBuffer=makeFilterBuffer(blurXBuffer, "Blur Y", -1, "shaders/YBlurShader.sha")
        self.finalcard = blurYBuffer.getTextureCard()
        self.finalcard.reparentTo(render2d)
        self.finalcard.setAttrib(ColorBlendAttrib.make(ColorBlendAttrib.MAdd))
        
        # Panda contains a built-in viewer that lets you view the results of
        # your render-to-texture operations.  This code configures the viewer.
        base.bufferViewer.setPosition("llcorner")
        base.bufferViewer.setLayout("hline")
        base.bufferViewer.setCardSize(0.652,0)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)
                        
class Shadow():
    
    def shadow(self):
            # Preliminary capabilities check.
            if (base.win.getGsg().getSupportsBasicShaders()==0):
                self.t=addTitle("It appears that shaders are not supported. They willn't work, sorry.")
                return
            if (base.win.getGsg().getSupportsDepthTexture()==0):
                self.t=addTitle("It appears that depth textures are not supported. They willn't work, sorry.")
                return
            # creating the offscreen buffer.
        
            winprops = WindowProperties.size(512,512)
            props = FrameBufferProperties()
            props.setRgbColor(1)
            props.setAlphaBits(1)
            props.setDepthBits(1)
            LBuffer = base.graphicsEngine.makeOutput(
                     base.pipe, "offscreen buffer", -2,
                     props, winprops,
                     GraphicsPipe.BFRefuseWindow,
                     base.win.getGsg(), base.win)
        
            if (LBuffer == None):
               self.t=addTitle("The video driver cannot create an offscreen buffer.")
               return
            Ldepthmap = Texture()
            LBuffer.addRenderTexture(Ldepthmap, GraphicsOutput.RTMBindOrCopy, GraphicsOutput.RTPDepthStencil)
            if (base.win.getGsg().getSupportsShadowFilter()):
                Ldepthmap.setMinfilter(Texture.FTShadow)
                Ldepthmap.setMagfilter(Texture.FTShadow) 
            # Adding a color texture is totally unnecessary, but it helps with debugging.
            Lcolormap = Texture()
            LBuffer.addRenderTexture(Lcolormap, GraphicsOutput.RTMBindOrCopy, GraphicsOutput.RTPColor)
        
            base.disableMouse()
            # Load the scene.
        
            cm=CardMaker('')
            cm.setFrame(-2,2,-2,2)
            floor = render.attachNewNode(PandaNode("floor"))
            for y in range(12):
                for x in range(12):
                    nn = floor.attachNewNode(cm.generate())
                    nn.setP(-90)
                    nn.setPos((x-6)*4, (y-6)*4, 0)
            floor.flattenStrong()
            self.LCam=base.makeCamera(LBuffer)
            # default values
            self.ambient=0.2
            self.cameraSelection = 0
            self.lightSelection = 0
            # setting up shader
            render.setShaderInput('light',self.LCam)
            render.setShaderInput('Ldepthmap',Ldepthmap)
            render.setShaderInput('ambient',self.ambient,0,0,1.0)
            render.setShaderInput('texDisable',0,0,0,0)
            render.setShaderInput('scale',1,1,1,1)
            render.setShaderInput('push',1,1,1,0)
            # Put a shader on the Light camera.
            lci = NodePath(PandaNode("Light Camera Initializer"))
            lci.setShader(Shader.load('shaders/caster.sha'))
            self.LCam.node().setInitialState(lci.getState())
            # Put a shader on the Main camera.
            # Some video cards have special hardware for shadow maps.
            # If the card has that, use it.  If not, use a different
            # shader that does not require hardware support.
            mci = NodePath(PandaNode("Initiating Shadows"))
            if (base.win.getGsg().getSupportsShadowFilter()):
                mci.setShader(Shader.load('shaders/shadow.sha'))
            else:
                mci.setShader(Shader.load('shaders/shadow-nosupport.sha'))
            base.cam.node().setInitialState(mci.getState())
        
    def __init__(self, ifon = 1):
        if ifon == 1:
            Shadow.shadow(self)
            print "Shadows are on."
        if ifon == 0:
            print "Advanced Shadow is off."
            return
       

class Camera(Handle):
  def __init__(self):
     g.cam = self
     Handle.__init__(self, name = "camera")
     self.__dict__['position'] = newSignalRefd(self, 'position', P3Type, P3(0, -10, 0))
     self.__dict__['hpr'] = newSignalRefd(self, 'hpr', HPRType, HPR(0, 0, 0))

  def refresh(self):
    # Sample signals for position / HPR and give them to the Panda3D camera
    Handle.refresh(self)
    p = self.position.now()
    g.panda3dCamera.setPos(p.x, p.y, p.z)
    p = self.hpr.now()
    g.panda3dCamera.setHpr(degrees(p.h), degrees(p.p), degrees(p.r))

class World(Handle):
# This initialization code sets up global variables in g as well as the
# world object internals
  def __init__(self):
     g.world = self
     Handle.__init__(self, isWorld = True, name = "World")
     # Signals native to the world object - note that all have defaults
     self.__dict__['color']   = newSignalRefd(self, 'color', ColorType, gray)

  def refresh(self):
    Handle.refresh(self)
    # Check all world-level events
    for w in g.reactEvents:
        w.check()
    c = self.color.now()
    base.setBackgroundColor(c.r, c.g, c.b)

  def kill(self):
       print "World object received a kill signal"
       exit()

def initializeGlobals():
     base.disableMouse()  # this takes the mouse away from Panda3D
     g.panda3dCamera = camera
     g.directObj = DirectObject()
     g.eventSignals = {}
     g.newEvents = {}
     g.events = {}
     g.reactEvents = []
     g.newModels = []
     g.tracking = False
     g.nextNE2dY = .95         # Positioning for 2-D controls
     g.nextNW2dY = .95
     g.tccontext = None
     # Set up the events / behaviors that deal with the mouse
     g.lbp = getEventSignal("mouse1", True)
     g.rbp = getEventSignal("mouse3", True)
     g.lbr = getEventSignal("mouse1-up", True)
     g.rbr = getEventSignal("mouse3-up", True)
     g.mouse = typedVar(SP2(0,0), P2Type)
     g.lbutton = hold(False, tag(True, g.lbp) + tag(False, g.lbr))
     g.rbutton = hold(False, tag(True, g.rbp) + tag(False, g.rbr))
     g.initMousePos = True
     g.mousePos = SP2(0,0)
     g.lbuttonPull = typedVar(SP2(0,0), P2Type)
     g.rbuttonPull = typedVar(SP2(0,0), P2Type)



  # These methods handle signals from the GUI
  # Cache keypress events so there's no duplication of key events - not
  # sure this is useful but it can't hurt.  Probably not a good idea to
  # have multiple accepts for the same event.
  
def getEventSignal(ename, val):
        if g.eventSignals.has_key(ename):
            return tag(val, g.eventSignals[ename])
        e = EventMonitor(ename)
        g.eventSignals[ename] = e
        g.directObj.accept(ename, lambda: postEvent(ename))
        return tag(val, e)

# This saves event occurances in g.newEvents
def postEvent(ename, val = True):
        g.newEvents[ename] = val

# Initialize the environment
initTime()     #  Sets current time to 0
base.enableParticles()

# Exported vocabulary
world = World()
initializeGlobals()
# The underlying Panda3D system uses the name "camera" so we'll use "cam" instead
camera = Camera()
# Bring the GUI behaviors / events to the user namespace
mouse = g.mouse
lbp = g.lbp
lbr = g.lbr
rbp = g.rbp
rbr = g.rbr
lbutton = g.lbutton
rbutton = g.rbutton
rbuttonPull = g.rbuttonPull
lbuttonPull = g.lbuttonPull

def react(event, handler):
    world.react(event, handler)

def react1(event, handler):
    world.react1(event, handler)

def when(event, handler):
    world.when(event, handler)

def when1(event, handler):
    world.when1(event, handler)

def key(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname, val)

def keyUp(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname + "-up", val)

def leftClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-leftclick", val)

def rightClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-rightclick", val)

allKeyNames = ["escape", "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12", 
               "backspace", "insert", "home", "page_up", "num_lock",
               "tab",  "delete", "end", "page_down",
               "enter", "arrow_left", "arrow_up", "arrow_down", "arrow_right", 
               "space"]
def checkValidKey(s):
    if s == " ":
        return "space"
    if s == "left-arrow":
        return "arrow_left"
    if s == "right-arrow":
        return "arrow_right"
    if s == "up-arrow":
        return "arrow_up"
    if s == "down-arrow":
        return "arrow_down"
    if type(s) is type("s"):
        if len(s) == 1 or s in allKeyNames:
            return s
    badKeyName(s)
