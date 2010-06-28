from Panda import *

# There is a simpler way to do the same thing.  An "interpolant" is
# based on two functions: at and to.  at(p) means that the interpolant is
# at location p, to(t, p) indicates a journey taking time t arriving at
# p.  You can add these together using "+".  For example,
#   i = at(P3(1,2,3)) + to(2,P3(3,2,1))
# defines an interpolant starting at (1,2,3) and taking 2 units of time
# to reach (3,2,1).
# To use an interpolant, you need to say "interpolate", as in
#   panda(position = interpolate(t, i)

# How does this differ from the interpolation in the previous example?
# Add a third point to the interpolation - take 2 seconds to get there.
# What happens if you put an "at" in the middle of an interpolant?

p0 = P3(2, -1, 1)    # Be here at t = 0
p1 = P3(-2, 4, -1)   # Be here at t = 1

# Define your interpolant here
i =
t = slider(min = -1, max = 2)  # Select t
soccerBall(position = p0, size = .2, color = red)  # Mark p0
soccerBall(position = p1, size = .2, color = blue)  # Mark p1
p = panda(position = interpolate(t, i))
text(format("t: %7.3f  Panda is at: (%7.3f, %7.3f, %7.3f)", t,
          getX(p.position), getY(p.position), getZ(p.position)))



start();