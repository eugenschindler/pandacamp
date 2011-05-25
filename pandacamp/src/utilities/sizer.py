from Panda import *
# Problems with the photo - need to use a rectangle instead.
# No way to see which way is forward
# No mark on the floor to show where feet should go
collisionObjects = [[]]
collisionType = ["cyl"]

maxHPR = pi

h = slider(position = P2(1,.85), min=-maxHPR,max = maxHPR, init = 0, label = "H")
p = slider(position = P2(1,.8), min=-maxHPR,max = maxHPR,init=0,label = "P")
r = slider(position = P2(1,.75), min=-maxHPR,max = maxHPR, init = 0, label = "R")

maxPos = 1
x = slider(position = P2(1,.55), min=-maxPos,max = maxPos, init = 0, label = "X")
y = slider(position = P2(1,.5), min=-maxPos,max = maxPos, init = 0, label = "Y")
z = slider(position = P2(1,.45), min=-maxPos,max = maxPos, init = 0, label = "Z")

size = slider(position = P2(1,.25), min=1,max = 10, init = 1, label = "Size")
lightangle = slider(position = P2(1, .15), min = 0, max = 2*pi, init = 2, label = "Light")

cRadius = slider(position = P2(1, -.25), min = 0, max = 1, init = 1, label = "Radius")
cBottom = slider(position = P2(1, -0.3), min = -1, max = 1, init = 0, label = "Bottom")
cTop = slider(position = P2(1, -0.35), min = -1, max = 1, init = 1, label = "Top")
sizeOffset = accum(1, key("q", times(10)) + key("a",times(.1)))
#Height and Zoom factor, doesn't do anything to the model.
text("Camera Pitch", position=P2(1,-.05))
height = slider(position = P2(1,-.1), min=-.5, max=.5, init = 0)
text("Camera Zoom",position=P2(1,.05))
zoom = slider(position = P2(1,0),min=0,max=10,init=5)
####################
##This is the model you'd have to change

# model = panda(position = P3(x,y,z), hpr = HPR(h, p, r), size=size*sizeOffset)
model = modelHandle(fileName = "panda-model.egg.pz", position = P3(x,y,z), hpr = HPR(h, p, r), size=size*sizeOffset)
####################

overhead = hold(False, key('u', True) + key('s', False))
angle = getX(lbuttonPull)*pi
camera.position = choose(overhead, P3(0,0,10), P3(sin(angle)*zoom, cos(angle)*zoom,-getY(lbuttonPull)))
camera.hpr = choose(overhead, HPR(0, -pi/2, 0), HPR(-angle+pi,height*pi,0))


##############
#Reference Rectangle Generation:
floor = -1
wallRight = 1
wallLeft = -1
wallDepth = 1
lowerLeft = P3(wallLeft,-wallDepth,floor)
lowerRight = P3(wallRight,-wallDepth,floor)
backLeft = P3(wallLeft,wallDepth,floor)
backRight = P3(wallRight,wallDepth,floor)
frontLeft = P3(wallLeft,-wallDepth,1)
frontRight = P3(wallRight,-wallDepth,1)
ts = .2
leftRect = rectangle(lowerLeft,frontLeft,backLeft,red)
#floorRect = photo(lowerLeft,lowerRight,backLeft,"/models/forestSky/m0cm0.png")
centerRect = rectangle(P3(wallLeft,-wallDepth,floor+1),P3(wallRight,-wallDepth,floor+1),\
             P3(wallLeft,wallDepth,floor+1),purple)
targetRect = rectangle(P3(ts* wallLeft,-ts* wallDepth,floor+1.001),P3(ts*wallRight,-ts*wallDepth,floor+1.001),\
             P3(ts*wallLeft,ts*wallDepth,floor+1.001),white)

rightRect = rectangle(lowerRight,frontRight,backRight,green)
noseRect = rectangle(P3(-0.05, -1, 0.001), P3(0.05, -1, 0.001), P3(-0.05, -1, 0.1), yellow)

##############

text("Model Sizer")
text("Mouse Controls Camera")
text("'q' = 10x larger, 'a' = 10x smaller")
text("Size slider for finer scale detail.")
text("u moves camera up, s to side")
text(model.hpr, position=P2(1,.9))
text(model.position,position=P2(1,.6))
text(model.size, position=P2(1,.3))
directionalLight(color = white, hpr = HPR(lightangle, 0 ,0))
ambientLight(color = color(.5, .5, .5))
def printer(w, x):
    print "localSize = " + str(model.size.now()) + ", localPosition = " + \
        str(model.position.now()) + ", localOrientation = " + str(model.hpr.now()) + \
        ", cRadius = " + str(cRadius.now()) + ", cFloor = " + str(cBottom.now()) + \
        ", cTop = " + str(cTop.now()) + ", cType = '" + str(collisionType[0]) + "'"

printButton = button("Print to Console", position = P2(1, -.8), size = .5)
react(printButton, printer)
collisionMenu = menu(["No Collision", "Sphere", "Cylinder", "TopBottom"], position = P2(-.9, -.9), size = .5)
def collision(w, x):
    for o in collisionObjects[0]:
        o.exit()
    if x == "No Collision":
        collisionObjects[0] = []
    elif x == "Sphere":
        collisionType[0] = "sphere"
        collisionObjects[0] = [sphere(size = cRadius)]  # Assumes the sphere model is correctly sized!
    elif x == "Cylinder":
        collisionType[0] = "cyl"
        mod = emptyModel()
        for i in range(20):
            a1 = i/20.0*2*pi
            a2 = (i+1)/20.0*2*pi
            r = rectangle(P3C(1, a1, -4), P3C(1, a2, -4), P3C(1, a1, 4), gold)
            r.reparentTo(mod)
        mod.size = cRadius
        collisionObjects[0] = [mod]
    else:
        collisionType[0] = "cyl"
        botRect = rectangle(P3(wallLeft,-wallDepth,floor+1),P3(wallRight,-wallDepth,floor+1),\
             P3(wallLeft,wallDepth,floor+1),brown)
        topRect = rectangle(P3(wallLeft,-wallDepth,floor+1),P3(wallRight,-wallDepth,floor+1),\
             P3(wallLeft,wallDepth,floor+1),lightBlue)
        botRect.position = P3(0,0,cBottom)
        topRect.position = P3(0,0,cTop)
        collisionObjects[0] = [topRect, botRect]
react(collisionMenu, collision)
start()