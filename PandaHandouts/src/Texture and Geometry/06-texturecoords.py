from Panda import *
# When you create a triangle or rectangle, you can choose which points in texture space each vertex goes with
# In texture space, the lower left corner is P2(0,0) and the upper right is P2(1,1).
# For a triangle, the texture points are P2(0,0), P2(1,0), and P2(0, 1).  You can alter
# these by keyword parameters .  Change the texP3 coordinate below and see what happens.
# Note - you can't use a slider!  Geometry can't change as the program runs.

triangle(P3(-2, 0, 0), P3(-1, 0, 0), P3(-2, 0, 1), texture = "realpanda.jpg", texP3 = P2(0, 1))

# Here are four points in space.  Build a tetrahedron from these by make four different colored
# trianges with every combination of p1, p2, p3, p4.  Glue these together with reparentTo and then spin the
# parent triangle.
p1 = P3(-1, 0, -1)
p2 = P3(1, 0, -1)
p3 = P3(-1, 0, 1)
p4 = P3(1,0, 1)

m = triangle(p1, p2, p3, texture = "realpanda.jpg")
n = triangle(p3, p4, p2, texture = "realpanda.jpg")  # Set texP1, texP2, and texP3 to get the rest of the photo
                                                     # move the second triangle to see the photo pull apart

start()