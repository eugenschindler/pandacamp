from Panda import *

# A reaction function is how a program responds to an event like a mouse click or the keyboard or models that collide.
# Every event function has the same parameters:

def exitTheModel(model, value):
    model.exit()
    
    
p = panda()
p.react(lbp, exitTheModel)
# Reaction functions
# One-time reactions
# Time and localtime
# Clock

start()