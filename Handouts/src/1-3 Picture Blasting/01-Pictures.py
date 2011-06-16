from Panda import *
# Rectangles and photos
# Take a photo from today's activities and place the .jpg in this folder.  Then
# bring it into Panda:

# Add a second picture to the same photo using side2 = "another.jpg"
# Set the HPR so that the photo spins.

rectangle(P3(0,0,0), P3(1,0,0), P3(0,0,1), texture = "realpanda.jpg", side2 = "westernlogo.jpg", hpr = HPR(time, 0, 0))

# Create a triangle from another photo and add it to the scene.

triangle(P3(-1,0,-1), P3(1,0,-1), P3(0,0,0), texture = "hurst.jpg",  hpr = HPR(time, 0, 0))

# What part of the photo is shown on the triangle?

start()