from Panda import *

# The "&" symbol means "and" and "|" means "or"
# So (x > 2) & (y > 3) would true if x is greater than 2 and y is greater than 3
# The parenthesis are needed to make sure that it does the > before the &
p = panda()
# Give a panda the name "p"
mouseControl(p)
# Let the mouse move the panda around

# You can put the x and z coordinate of p's location into variables
# so that it's easier to refer to them
x = getX(p.position)
z = getZ(p.position)
# Set the color of the panda to be different when the x and z coordinates
# are both bigger than 0.  Or when either is bigger than 0.
# Can you make the color depend on both x and y being positive or both
# being negative?


p.color = choose(((x > 0) & (z > 0)) | ((x < 0) & (z < 0)), green, yellow)

start()