from Panda import *
import g
# A menu generates an event that contains the selection.
# The following menu generates events "One", "Two", or "Three":
m = menu(["One", "Two", "Three"], P2(-.8, .8))
# We can observe what was last picked using hold:
txt = hold("Nothing", m)
text(txt)

p = panda()
# This menu allows us to change the model p

m1 = menu(["Panda", "Glider", "Ball"], P2(-0.8, .6))


# This is a function to react to the menu:
def change(m, v):
    # This is needed to make sure that the p with the panda in it is the once
    # used in change
    global p
    p.exit()
    if v == "Panda":  # This is how you test to see which selection was clicked
        p = panda()
    elif v == "Glider":
        p = hangGlider()
    else:
        p = soccerBall()

react(m1, change)
# Add another option to this menu for the jeep.
# Make a new menu that allows you to select "spin" or "tumble".  Hold onto the
# most recently selected item with a hold and inside change set either the heading
# (for spin) or pitch (for tumble) to be localTime.  To look at the
# current value of this you'll need a .now() - this only works on signals that
# are part of an object so you need to put the hold inside "world" - as in
# world.todo = hold("Spin", m)
#

start()