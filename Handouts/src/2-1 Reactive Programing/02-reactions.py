from Panda import *

# A reaction function is how a program responds to an event like a mouse click or the keyboard or models that collide.
# Every event function has the same parameters:

def exitModel(model, value):
    model.exit()
   
# This function tells the model to exit from the program.  The things you do inside a reaction function are different than
# the things that we normally write - you couldn't put the .exit() thing in other places in your program.

# You attach a reaction to a model by giving the triggering event and the name of the reaction function.  The def always
# comes before the .react 

# This tells the panda to exit the scene when the left mouse button is pressed (lbp).  key is another event you can use.
p = panda()
p.react(lbp, exitModel)

# Activity 1:
#  Change the reaction function to do the following:
#    a) Make the panda move
#    b) Change the color of the panda
#  Add another panda to the scene that performs the same reaction using a different event, rbp

# Another event is a mouse click on a particular model.  Use leftClick(m) to get an event when the model is clicked on by the
# left mouse button

# A function is code that can be reused.  Every function starts with def and a parameter list
# For example, this function creates a panda and makes it exit when the left button is clicked:
def exitingBunny(pos, c):
    p = bunny(position = pos, color = c)
    p.react(leftClick(p), exitModel)


# Activity 2:
# 
# Call the function above to create two bunnies that will exit when clicked.
# Add a parameter to the function to set the color of the bunny

exitingBunny(P3(-1, 0, 0), red)
exitingBunny(P3(1, 0, 0), blue)

# The timeIs event happens at a particular time.  For example, timeIs(2) happens 2 seconds after the
# program starts.  
# A reaction doesn't need to be attached to a model.  You can use "react" with out a model to
# make something happen.

# Activity 3:

# Create a reaction function which creates an exitingBunny.  

start()