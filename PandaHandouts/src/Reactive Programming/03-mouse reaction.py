from Panda import *
# Objects can react to events like mouse button presses.

# localTime is like time except it starts back at 0 when a reaction occurs
x = P3(localTime-4, 2, sin(time))
# The panda will move right because of localTime
p = panda(position = x, color = color(.4*sin(time)+.4, .4, .4),size = sin(time-1))
# This is a reaction function - this ALWAYS has two parameters: the model that
# is reacting and the value that this model "hears" and reacts to.
# The mouse button doesn't say anything interesting so we'll ignore v in
# this function.  This causes the movement to "start over"
def reset(p, v):
    p.position = x
# This is how you make a model watch for a reaction
p.react(lbp, reset)


# Try the following:
#   Change the reaction to also change the hpr
#   Try using "react1" instead of "react".  What's
#     the difference?
#   Add a second reaction that sends the panda left
#   Trigger this by rbp (the right mouse button)


start()