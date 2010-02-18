from Panda import *
<<<<<<< .mine

=======
>>>>>>> .r159
# Place a green floor under the panda at (0,0,0)
# Use a slider to move the camera up and down
# Set the world background color to blue (thats world.color)
# Remember that you only need to tell rectangle 3 points - it computes
# the fourth one.

panda = (position = P3(0,0,0))

<<<<<<< .mine
h = slider(min = -1, max = 1)
camera.position = P3(0, -5, h)
rectangle (P3(-2,3,1/2), P3(-2,-5,1/2), P3(2,3,1/2),blue)
=======
h = slider(min = -1, max = 1)
camera.position = P3(0, -5, h)
>>>>>>> .r159

re = slider(min = 0 ,max = 1, label = "red")
gr = slider(min = 0 ,max = 1, label = "green")
bl = slider(min = 0 ,max = 1, label = "blue")

text(format("Red: %5.3f  Green: %5.3f  Blue: %5.3f", re, gr, bl))

world.color = color(re,gr,bl)
# Use rectangle here
# set the background color here
start()