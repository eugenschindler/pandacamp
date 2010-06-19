from Panda import *
# Sounds can be played only within reaction functions.
# You have to do two things:
#   Create a sound object - here are two examples:

quack = sound("duck.wav")
pop = sound("corkPop.wav")

# Then place sound.play() in a reaction function.


# You can use a single reaction function if you tag the buttons with the sound
# to be played.

def playit(obj, val):
    val.play()

# Create models that play different sounds when clicked

start()