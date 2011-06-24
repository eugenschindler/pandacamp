from Panda import *
pow = slider(min=0, max=4, label= "power")
ang = slider(min=0, max=2*pi, label="angle")
v=P3C(pow, ang, 0)
ambientLight(color = color(.5, .5, .5))
directionalLight(color = color(0.6, 0.6, 0.6), hpr = HPR(5,5,0))
def f(x,y):
    return (smoothStep(y-5))/2.0
s = golfCourse(f, 10, 10, -8, .2)
b = sphere(size = .2, color= white)
rollSphere(b, s, 5, 1, 0, 0)
h = sphere(position=P3(5,9,s.f(5,9)),size = .3, color = black)
def hole(m,val):
    m.position= m.position.now()
    text("win")
def stroke(m,val):
    rollSphere(b,s,b.xpos.now(),b.ypos.now(),getX(v).now(),getY(v).now())    
b.react(lbp, stroke)
b.react1(hit(b,h),hole)
addWallBounces(s, b)
camera.position =choose(rbutton,P3 (5,5,20),P3(5,-10,6))
camera.hpr = choose(rbutton, HPR(0,-pi/2,0), HPR(0,6,0))

start()