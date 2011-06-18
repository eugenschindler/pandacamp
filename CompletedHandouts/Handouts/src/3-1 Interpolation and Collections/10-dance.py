# Vectors and interpolation/10-dance.py
from Panda import *
# Create a "dance" that scripts the position, HPR, and color of a model.
# Create three different interpolants, one for each.  Build the interpolants in
# 6 segments of .5 and repeat each forever.
# The position interpolant should use only "move" - start with an "at" in each
# model so each model can be at a different place.
# Put three (or more!) models in your dance.

t = time*4

start()