from Panda import *
sphere(size=-100,texture="skymap.jpg",hpr=HPR(time/20,0,0))


def volcano(m, v):
    for l in range(10):
        hpr = HPR(randomRange(0,2*pi), randomRange(-pi/2, -pi/8),0)
        v=HPRtoP3(hpr)*3
        m=randomChoice((panda,bunny,jeep,girl,r2d2,ralph,gorilla,tails,sonic,truck,ford,jeep,testModel,fireish))
        p = m(size = .2)
        launch(p, P3(0,0,1), v)
        p.when(getZ(p.position) < -2, exitScene)

def f(t):
        return P3C(t/20,-t*3,t/10)-P3(0,0,2)
def g (t):
        return P3C(t/20,t*3,t/10)
    
    
def l (m,v):
    r2d2(position = f(localTime),size=.5,hpr=HPR(localTime,0,0))
    panda(position = g(localTime),size=.32,hpr=HPR(localTime,0,0))
    
c = alarm(step = .2)
react(c, l)
camera.position=P3(0,-time/2-5,0)
start()


