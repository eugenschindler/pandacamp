from Panda import *

# This demonstrates blasting the pieces of a picture using interpolation (itime)
# to move fragments from place to place

# This breaks a photo into a 5 x 5 grid
pieces = blastPicture("mathcamp.jpg", 5, 5)
# This sets each piece in motion
for p in pieces:
    # Start at a random place in the centered unit cube and move to assemble the picture in 3 seconds

    p.position = itime(at(P3(random11(), random11(), random11())) + to(3, p.location))

# Things to do:
#   Try a different grid size instead of 5x5.  More than 1000 is probably laggy
#   Make the starting location in a larger cube
#   Try different starting locations - above or left, random or constant
#   Try randomizing the wait
#   Start at a multiple of the location

# Functions you can use:
#  random01()  - a random number between 0 and 1
#  random11()  - a random number between -1 and 1
#  randomRange(low, high) - a random number in a given range
#  randomInt(max) - a random integer between 0 and max-1

start()