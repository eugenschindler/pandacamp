from Panda import *
# Photos can be displayed on a cube or a photoWheel.
# A cube takes exactly six photos:

cube("realpanda.jpg", "realpanda.jpg", "realpanda.jpg", "realpanda.jpg", "realpanda.jpg", "realpanda.jpg", hpr = HPR(time, time*1.2, time*1.5))

# Give the wheel an interesting trajectory and add some of your own pictures to it.
# Note that the picture need to be grouped in [] unlike the cube.

# photoWheel([],position = P3(),hpr = HPR())

start()