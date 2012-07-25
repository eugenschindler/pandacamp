from Panda import *

# Use the .x and .y components of each tile to customize the behavior

pieces = blastPicture("mathcamp.jpg", 5, 5)

for p in pieces:
    # Use a trajectory that depends on the grid location of each tile.
    # The .x and .y fields contain an integer between 0 and the number of tiles-1
    # Use a path that makes the tile go off screen and adjust the wait time in the move
    p.position = itime(at(p.location) + move((p.x+5*p.y)/5.0, P3(0,0,0)) + to(1, P3(20,0,0)))
    # Activities:
    #   Try different ways of combining p.x and p.y
    #   Use modulus, as in x % y, to group tiles.
    #   Customize other features of the tile
start()