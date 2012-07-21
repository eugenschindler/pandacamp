from Panda import *
# You can add more photos to your nametag by placing some geometric solids in your animation

# You can put an arbitrary number of photos in a wheel, 6 photos on a cube, or 4 on a tetrahedron

a = photoWheel(["nic.jpg", "nic2.jpg", "hurst.jpg" , "nic3.jpg", "camplogo.jpg", "hurst.jpg"])

a.hpr = HPR(((time*2)/(cos(time)))/5, (sin(time/cos(time))*cos(sin(cos(time)*time)))/5, (cos(time*sin(time/cos(time*sin(time)))))/5)


c = cube("nic.jpg", "nic2.jpg", "nic3.jpg", "nic.jpg", "nic2.jpg", "nic3.jpg")
c.position = P3(-2, 0, 0)
c.hpr=HPR(time*2,0,time)



#tetra(t1, t2, t3, t4)


    
start()