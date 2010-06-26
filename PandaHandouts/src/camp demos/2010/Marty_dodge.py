from Panda import *
# A reaction function is a python function that looks like this:
#  def f(model, value)
#      what to do for the reaction
p = tails()  # Make a panda
camera.hpr = HPR(0,4.68,0)

camera.position = P3(0,0,50)
def bounce(m, v):
    p.v = -p.v.now()  # v is the velocity



def forward(p, v):
    dir = P3()
    position = p.position.now()+ dir
    
    
p.react(key('w'), forward)


def left(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr)+ localTime, 0, 0)
p.react(key('a'), left)

def right(p, v):
    hpr = p.hpr.now()
    p.hpr = HPR(getH(hpr)+ -localTime, 0, 0)
p.react(key('d'), right)


#p.position = P3(time, 0, 0)
#p.v = 1
#p.when((getX(p.position) > 3) | (getX(p.position) < -3), bounce)

  

start()