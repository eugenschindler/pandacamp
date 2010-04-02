from Panda import *
panda.position = at(P3(-3,0,0))+to(3,P3(0,2,2.5))+to(P3(-2,0,0))
#initially move the panda to the right
p = panda(position = P3(time, 0, 0))
# This takes the panda, looks at the current position,
# and starts going up from this position
def goUp(p, v):
    here = p.position.now()
    p.position = here + P3(0,0,localTime)
    p.hpr = HPR (0, -pi/4, pi)
def goDown(p, v):
    here = p.position.now()
    p.position = here + P3(0,0,-localTime)
    p.hpr = HPR (0, pi/4, 0)
# On the left button press, go up
p.react(lbp, goUp)
p.react(rbp, goDown)
# Try adding a print statement to the goUp function so
# you can see where you are when you start to go up

# Why doesn't this do anything the second time you click?

# Add another reaction using the right button to move the panda right again




start()