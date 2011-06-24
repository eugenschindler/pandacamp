from Panda import *

ambientLight(color = color(.5, .5, .5))
directionalLight(color = color(0.6, 0.6, 0.6), hpr = HPR(5,5,0))
def f(x,y):
    return (smoothStep(5-x))/2.0


s = golfCourse(f, 10, 10, -8, .2)

j = sphere(texture = "jupitermap.jpg", size = .2)
rollSphere(j, s, .5, .5, 10, 10)
addWallBounces(s, j)



#mouseControlCamera(camera)
camera.position = P3(5, -10, 6)
camera.hpr = HPR(0,6,0)
start()