from Panda import *
# Sounds can be played only within reaction functions.
# You have to do two things:
#   Create a sound object - here are two examples:

quack = sound("duck.wav")
pop = sound("corkPop.wav")

# Then place sound.play() in a reaction function.

# Create a soundboard with three buttons, each attached to sounds.

# You can use a single reaction function if you tag the buttons with the sound
# to be played.

def playit(obj, val):
    val.play()
# Put the buttons here

# Use "react" to connect the buttons with the sounds.
start()