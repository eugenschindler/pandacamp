from Panda import *
# The reactions created by .react are always there
# What if you want to not use a reaction again?
# Use react1 to just do a reaction once.


p = panda()

def r1(p, v):
    p.position = P3(0,0,1)
    p.react1(lbp, r2)

def r2(p, v):
    p.position = P3(0,0,2)
    p.react1(lbp, r3)

def r3(p, v):
    p.position = P3(2,0,1)
    p.react1(lbp, r1)

p.react1(lbp, r1)

# Add another reaction function and create another place for the panda to go after
# Have these reactions change something besides the position of the panda

start()