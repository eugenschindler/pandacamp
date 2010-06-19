from Panda import *
# A reaction function is a python function that looks like this:
#  def f(model, value)
#      what to do for the reaction

# The name f can be anything you want.  You can have lots of reaction functions in your program.
# We won't use the value right now but it still has to be there.

# Here are two:
def goto0(model, value):
    model.position = P3(0,0,0)  # Put the model at (0,0,0) when reacting

def goto1(model, value):
    model.position = P3(0,0,1)  # Put the model at (0,0,1)

# You can tell a model to react using .react:
p = panda()  # Make a panda
p.react(lbp, goto0)  # Tell it to go to P3(0,0,0) when the left mouse button is pressed
p.react(rbp, goto1)  # Tell it to go to P3(0,0,1) when the right mouse button is pressed
# lbp and rbp are events - these are triggered by the change from button up to down for the left and right mouse buttons.

# Change the reaction functions to change the size instead of the position
# Add a second panda that also reacts to the same mouse buttons
# Change the reactions to twirl the panda left or right depending on which button you press.
# Here are two:
def twirlright(model, value):
    model.hpr = HPR(time, 0, 0)

def twirlleft(model, value):
        model.hpr = HPR(-time, 0, 0)

start()