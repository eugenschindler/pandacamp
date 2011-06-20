from Panda import *

# slicePlice is used to break a picture into many slice by columns and rows.
# There two parts to a sliced pictures the full picture and the pieces. Each can
# be moved seperatly.

(picture, pieces) = slicePicture( "realpanda.jpg", columns = 10,  size = 2)

# First try making the Picture spin.



# A for loop can be used move each piece in all the pieces of the picture.

for piece in pieces:
    piece.position = integral(P3(random01(), 0, 0))
    
# Next move each piece in the pieces. Move a piece by using(time*piece.x) to
# spread the pieces out. Piece.x keeps treck of whick column that a piece is in.

    

# Try this: change the columns to rows in the slicePicture and move them
# downward using piece.y.
# Finally use a random number to change the velocity.

start()