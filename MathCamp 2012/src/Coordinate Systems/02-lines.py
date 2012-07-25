from Panda import *

def launcher(f, deltaT):
    c = alarm(step = deltaT)
    react(c, lambda m, v: f(localTime, v))

def cyl(t, v):
    panda(position = P3C(2, t, t/6-2))

launcher(cyl, .2)

# Things to do:
#   Change the r component to t
#   Set the HPR based on t
#   Create a second stream of models
#   Change the radius based on the height - use sine

start()
