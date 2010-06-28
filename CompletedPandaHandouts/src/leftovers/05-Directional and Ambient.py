from Panda import *

#Static models and behaviors
camera.position = P3(0, 0, 7)
camera.hpr = HPR(0, 0, 0)
d = discoHall(position = P3(0, 50, 0), hpr = HPR(pi/2, 0, 0))

# This puts the panda on the stage

p = panda(position = P3(0, 60, 3), hpr = HPR(time, 0, 0), size = 3)


#control RGB of point light
PLColor = sliderColor(label="PL")

#control RGB of ambient light
ALColor = sliderColor(label="AL")

dlh = slider(max = 20, min = 0, label="DL heading")
dlp = slider(max = 20, min = 0, label="DL pitch")


#an ambient light source
al = ambientlight(color = ALColor)


dl = directionallight(color = PLColor, hpr = HPR(dlh,dlp,0) )

# The disco is completely white - without directional light it's invisible!
# Note how the directional light works - surfaces that face the same way
# get identical illumination.

# Add a moving point light - you can see where it is by looking at the disco ball.

start()

