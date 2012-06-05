# intro to Panda/03-rotatingpanda.py

# Experiment with the HPR of this panda.  Create a second panda at P3(1, 0, 0) with a different HPR.
# Use HPR to create a HPR object.

from Panda import *
phpr = sliderHPR(label = "panda")
panda(hpr = phpr)
text(phpr)




start()