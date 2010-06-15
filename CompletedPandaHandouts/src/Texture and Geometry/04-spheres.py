from Panda import *
# Sphere have a lot of predifined textures.  Create a scene with:
#  A sphere with the camplogo on it - make the sphere turn
#  Another sphere with a planet on it - also make this one turn
#  A large sphere with a sky texture of some sort.  You have to make it's size
#   negative to put the texture inside the sphere.  The size should be big enough to encompass the camera and all
#   scene objects - something like -100.
#  

sphere(hpr = HPR(time,0,0), texture = "camplogo.jpg", size = 1.5, position = P3(-1.2, 0, 0))

sphere(hpr = HPR(time*2,0,0), texture = "earthmap.jpg", size = 1, position = P3(1.2, 0, 0))

sphere(hpr = HPR(time/3,0,0), texture = "redcloud.png", size = -200)

camera.hpr = sliderHPR(label = "camera")

start()