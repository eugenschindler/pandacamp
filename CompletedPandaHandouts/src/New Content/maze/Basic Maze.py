# Basic Maze.py
from Panda import *

# make the racetrack
Racetrack("maze2.txt")

camera.position = P3(15, 15, 200)
camera.hpr = HPR(0, -pi/2, 0)

start()
