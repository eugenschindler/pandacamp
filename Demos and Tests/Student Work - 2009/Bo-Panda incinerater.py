from Panda import *
grassScene (position=P3(0,0,0))
# The timeIs event happens at given absolute time
boom =sound("synth_beep_3.wav")# There is also a localTimeIs event
p = panda(position = P3(0,0,0))
def byebye(m, v):
    m.exit()
    boom.play()
stop=sound("evil_laugh.wav")
p.react(localTimeIs(3), byebye)
text("press s to stop the madness")
# Add a second model that exits at a different time
# Next, delete these models and respond to the lbp event by creating
# a model that moves left and exits after two seconds.
# Finally, alter this to use the current mouse position
# to set the panda direction.  Note that if you have a
# direction d that localTime*d moves you along that direction
c = alarm(start = 0, step = 2)
def trick(s,n):
    stop.play()
    # Write a function to create a new bear and send it
    # moving right across the screen.  Use "localTime"
    # to create your motion.
react(key('s'), trick)
def launch(w, x):
  p=panda(position=P3(localTime-2,0,0))
  e=panda(position=P3(localTime-2,0,-2))
  p.hpr=HPR(localTime,0,0)
  e.hpr=HPR(localTime,0,0)
  e.color=purple
  p.color=green
  p.react(localTimeIs(3), byebye)
  e.react(localTimeIs(9), byebye)
# This calls the launch every 2 seconds
fireish(position=P3(2,0,-.5))
fireish(position=P3(7,0,-2.5))
# Note that there is no particular model reacting here - you can
# have "free floating" reactions.  The object associated with this is the
# world object.
react(c,launch)
# This is a 3-D direction based on the mouse position
dir = P3(getX(mouse), 0, getY(mouse))

camera.position = P3(3.5, -15, 0)
start()