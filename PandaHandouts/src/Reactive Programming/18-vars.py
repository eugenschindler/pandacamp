from Panda import *
# A var is a value that can be accessed in reactive code and changed in
# non-reactive code using the .set, .add, and other methods.

# This is how you make a button on the screen
b = button("Hit me", P2(-0.8, .6))
# This is a value that you can access from reaction code
v = var(0)  # 0 is the initial value
# This is a reaction that will add 1 to v
def bump(w, x):
   v.add(1)
# When the button clicks, bump up v
react(b, bump)
# Show the value of v
text(v)
# Add a reaction to lbp that subtracts 2 from v
# Use v.sub to do this
# Add another button that multiplies v by 2
# Add a clock that adds 1 to v every second
# Use v set the heading of a model

start()