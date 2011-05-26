# only turn to blackand turn to white works needs to be fleshed out more as of Jan 25 2011 - michael Reed

from Panda import *
# If all you need to do with an event is remember the most recent one, there
# is a simpler way to deal with the event than using react.
# hold is a function that remembers the last thing it is told.
# You give hold an initial value and an event stream - the resulting signal
# will start with the initial value and change to whatever values that the
# event stream gives it.

# The events all need to send a value - a key event can just add this to
# the key function.  With the mouse events, you can use "tag" to tag an event
# with a value.  In fact, key(a, b) and tag(b, key(a)) are the same.

#Information on buttons
text("Press 1 to change the Background Black")
text("Press 2 to change the Background Blue")
text("Press 3 to change the Background Red")
text("Press 4 to change the Background Green")
text("Press left mouse button to change the Background Dark Blue")


sp = panda(position = P3(0,0,0))
# This time change the background color instead of the model

# Add the other events to the following
events = key('1', black)+ key('2', blue)
# There is another version of tag that changes the tag every time the event
# happens.  tags([darkblue, darkred], lbp) would deliver a different color
# each time the mouse is pressed.  Change one of the events to use tags (you
# can use this with key too)
world.color = hold(white, events)

start()