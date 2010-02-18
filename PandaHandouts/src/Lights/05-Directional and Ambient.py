from Panda import *

#Static models and behaviors
camera.position = P3(0, 0, 7)
camera.hpr = HPR(0, 0, 0)
d = discoHall(position = P3(0, 50, 0), hpr = HPR(pi/2, 0, 0))

# This puts the panda on the stage

p = panda(position = P3(0, 60, 3), hpr = HPR(time, 0, 0), size = 3)


#control RGB of point light
sdc1 = slider(max = 1, min = 0, label="DL Red")
sdc2 = slider(max = 1, min = 0, label="DL Green")
sdc3 = slider(max = 1, min = 0, label="DL Blue")

#control RGB of ambient light
sac1 = slider(max = 1, min = 0, label="AL Red")
sac2 = slider(max = 1, min = 0, label="AL Green")
sac3 = slider(max = 1, min = 0, label="AL Blue")

dlh = slider(max = 360, min = 0, label="DL heading")
dlp = slider(max = 360, min = 0, label="DL pitch")


#an ambient light source
al = ambientlight(color = color(sac1, sac2, sac3))


dl = directionallight(color = color(sdc1,sdc2,sdc3), hpr = HPR(dlh,dlp,0) )

# The disco is completely white - without directional light it's invisible!
# Note how the directional light works - surfaces that face the same way
# get identical illumination.

# Add a moving point light - you can see where it is by looking at the disco ball.

start()

