from Panda import *
# A group of photos can be displayed on a cube or a photoWheel.
# Replace some of these photos with your own.
# A cube takes exactly six photos:

c = cube("realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg", position = P3(1,1,1.5))

b = photoWheel(["realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg" ,"realpanda.jpg"], position = P3(-1, 0, 0))


# Make the cube and the wheel move so you can see all sides.
start()