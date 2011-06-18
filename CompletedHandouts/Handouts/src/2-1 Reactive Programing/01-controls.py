from Panda import *

# You have already used one reactive value: time.  This is a number that starts at 0 and keeps going up.
# Here are some more:
#  mouse - this is a 2-D point, where the x and y coordinate are between -1 and 1.  0,0 is at the center.  You use getX and getY to access
#          individual coordinates
#  lbutton, rbutton: these are boolean (true / false) values from the mouse buttons.  You can use this in a "choose", for example
#                    choose(lbutton, 0, 1) which is 0 when the button is pressed and 1 when not pressed.

p = panda()
grassScene()

# Activity 1:
# Use each of these to move the panda in some way.  You can set either the position or the hpr or even the color
p.position = P3(time, 0, 0)   # Example: use the time to move the panda right


# Activity 2. 
# Events are things like key presses or mouse clicks.  Use "hold" to remember the most recent event value.  Give a key event a value
# such as key('a', 2) - this produces the value 2 when a is pressed.  You can use + to combine events.
# To put a value on lbp or rbp, use "tag", as in tag(lbp, red) to have each left button press generate the value "red".
# Use hold to remember the most recent event - you have to give it an initial value and an event.
# For example, this sets the size of the panda using "b" and "l"

p.size = hold(1, key('l', .5) + key('b', 1.5))

# Use the left and right mouse button to set the color of the panda and the keyboard to select its position.


# Activity 3. Build a position controller using hold and the arrow keys to set the velocity of the panda.  Use integral to turn the velocity into
# the position of the panda.  The keys are named "arrow_right", "arrow_up", "arrow_down", and "arrow_left".

# Mention how to get the panda to face the direction of travel?



start()