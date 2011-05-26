from Panda import *
text(lbutton)
text(rbutton)
# The signals lbutton and rbutton are either True or False
# The function choose is used to select one of two values:
#   choose(test, val1, val2)
# This has the value val1 if the test is true and val2 if not.
# Use choose to create a panda which is at (0,0,0) when the
# left button is pressed and at (1,0,0) when it is not.

# Create a panda that is at either P3(0,0,0) or P3(1,1,1), depending on the left button
# Create another panda that is red unless the right button is pressed - then it's blue.
panda(position = choose(lbutton, P3(0,0,0), P3 (1,1,1)))
panda(color = choose(rbutton, red, green), position = P3(-2, 0, 0))

# Finally, create a panda that gets twice as big when both buttons are pressed.
# The "&" symbol means "and" - so lbutton & rbutton is true only when both buttons
# are pressed.

panda(position = P3(2, 0, 0), size = choose(lbutton & rbutton, 0.5, 1))


start()