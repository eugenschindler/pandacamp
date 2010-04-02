from Panda import *

# How do you interpolate between two points?
# If the panda is at p0 at t = 0 and p1 at t = 1,
# what equation would make it move from p0 to p1 smoothly?
# What if you want to make it arrive at p1 when t = 2 instead of 1?

p0 = HPR(2, -1, 1)    # Be here at t = 0
p1 = HPR(-2, 4, -1)   # Be here at t = 1
p2 = HPR(-2, 10, 9)
t = time  # Select t
s = slider(min = -1, max = 3)
i = at(p0)+ to (1, p1)+ at (p0) + to (1.25, p2)

p = panda(position = interpolate(t, at(p0) + to (1,p1)+ to (1,p2)))  # Fill this in
text(format("t: %7.3f  Panda is at: (%7.3f, %7.3f, %7.3f)", t,
          getX(p.position), getY(p.position), getZ(p.position)))

start()
