
#  This is a wrapper for all user-visible functions

#  It also contains "start" and "begin" which initialize the FRP system and
#  start Panda
import g
import direct.directbase.DirectStart          # start panda
import os, sys
from direct.showbase import DirectObject      # for event handling
from direct.actor import Actor                # allow use of actor
from direct.gui.DirectGui import *            # 2D GUI elements
from World import *
from Time import *
from Color import *
from Models import *
from Handle import *
from Numerics import *
from Slider import *
from Text import *
from Signal import time
from FRP import *
# from Switch import *
from Light import *
from Sound import *
from Button import *
from Menu import *
from PEffect import *
from DynamicGeometry import *
from DynamicTerrain import *
from Interp import *
from TextBox import *
from PoseAndScriptFiles import *
from Utils import *


# Call this at the end to fire up Panda

def start():
    print "Starting..."
    # Initialize the system.  This is called from "begin" and needs to traverse
    # every active signal in the system.
    icontext = 0
    g.models.append(world)  # This doesn't happen during initialization
    g.models.append(camera)
    for m in g.models:
        m.checkSignals(icontext)
        m.d.switches = m.d.newswitches # Add in switchers generated at initialization
    taskMgr.add(stepTask, 'PandaClock')
    run()
