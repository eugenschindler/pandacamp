from Panda import *

ambientLight(color = color(.5, .5, .5))
directionalLight(color = color(0.6, 0.6, 0.6), hpr = sliderHPR())
def f(x,y):
    return (smoothStep(5-x))/2.0


b = soccerBall(size = .2)


s = golfCourse(10, 10, f, b)

j = sphere(texture = "jupitermap.jpg", size = .2)
rollSphere(j, s, 0, 0, 0, 0)
rollSphere(b, s, 2, 2, -1, -1)



mouseControlCamera(camera)

start()