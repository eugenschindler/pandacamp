from Panda import *
# time is something that is always going as the program runs:
f = fireish(position= P3(6,0,0))
r = bunny(position= P3(1,1,1))

def goto0(model, value):
    model.position = P3(0,0,0)  # Put the model at (0,0,0) when reacting
def fall(model, value):
    model.position = P3(0,0,-localTime/2)
def kill(model, value):
    model.size = 0
def revive(model, value):
    model.size = 1
def big(model, value):
    model.size = 2
def small(model, value):
    model.size = 1
def fire(model, value):
    model.position = P3(0,0,0)
def douse(model, value):
    model.position = P3(5,0,0)
def rise(model, value):     # Rise up from (0,0,0)
    model.position = P3(0,0,localTime/2)

p = panda()  # Make a panda
p.react(lbp, goto0)  # Tell it to go to P3(0,0,0) when the left mouse button is pressed
p.react(rbp, rise)
p.react(key("a"), fall)
p.react(key("b"), big)
f.react(key("f"),fire)
f.react(key("d"),douse)
p.react(key("s"),small)
r.react(key("t"),kill)
r.react(key("h"),revive)
# Tell it rise when the right mouse button is pressed

# What if you want to restart at 0 when you press the right button?
# Change time to localTime in rise and see what happens.

# Instead of changing the position, use time to change the heading.  How does localTime differ from time in this case?

start()