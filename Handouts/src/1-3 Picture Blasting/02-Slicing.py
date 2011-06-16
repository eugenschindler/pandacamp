from Panda import *

# slicePlice is used to break a picture into many slice by columns and rows.
# There two parts to a sliced pictures the full picture and the pieces. Each can
# be moved seperatly.

(center, pieces) = slicePicture( "realpanda.jpg", columns = 10,  size = 2)

# First try making the Picture spin.

center.hpr = HPR(time,0,0)

# A for loop can be used move each piece in all the pieces of the picture.

for piece in pieces:
    
# Next move each piece in the pieces. Move a piece by using(time*piece.x) to
# spread the pieces out. Piece.x keeps treck of whick column that a piece is in.

    piece.position = P3((time*piece.x*.2),0,0)

# Try this: change the columns to rows in the slicePicture and move them
# downward using piece.y

start()