# intro to Panda/05-scale.py
from Panda import *

# Create 2 pandas at (1,0,0) and (-1,0,0) and set their sizes
# using sliders that range 0 to 5 and init at 1
# Display the values of the sizes in text objects
# What happens when the pandas touch?
# What happens when the size is negative?

size1 = slider(min = -1, max = 5, init = 1, label = "right")
size2 = slider (min = -1, max = 5, init = 1, label = "left")
panda(position = P3 (1,0,0), size = size1)
panda(position = P3 (-1,0,0), size = size2 )

start()