from Panda import *

# The signals lbutton and rbutton are either True or False
panda(position =choose(lbutton, P3(0, 6, -2), P3 (-2, -2, -2)))
panda(color =choose(rbutton, red, green))

text(lbutton)
text(rbutton)
# You can make the messages easier to read using format:
# Try format("Right: %s", rbutton) in the Text

# The function choose is used to select one of two values:
#   choose(test, val1, val2)
# This has the value val1 if the test is true and val2 if not.
# Use choose to create a panda which is at (0,0,0) when the
# left button is pressed and at (1,0,0) when it is not.

# The symbol "&" stands for "and" in the signal world.
# Create a panda that moves when both buttons are pressed

# The symbol "|" stands for "or" in the signal world.
# Create a panda tha moves when either button is pressed

# The symbol "~" stands for "not"
# Create a panda that moves when the left but not the
# right button is pressed.

# Finally, create a panda that is at (0, 0, 0) unless the
# left button is pressed.  When the left button is pressed
# it is at (time, 0, 0)

start()