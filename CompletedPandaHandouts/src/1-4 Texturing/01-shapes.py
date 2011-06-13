from Panda import *
# Photos can be displayed on a cube or a photoWheel.
# A cube takes exactly six photos:

c = cube("realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg", position = P3(1,1,1.5), hpr = HPR(time*1.2, time, 0))

# Give the wheel an interesting trajectory and add some of your own pictures to it.
# Note that the picture need to be grouped in [] unlike the cube.

b = photoWheel(["realpanda.jpg","realpanda.jpg","realpanda.jpg","realpanda.jpg" ,"realpanda.jpg"], hpr = HPR(time, time*1.2, 0), position = P3(-1, 0, 0))

start()