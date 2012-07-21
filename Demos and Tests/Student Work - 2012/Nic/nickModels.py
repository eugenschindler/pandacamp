from Panda import*

def ghost(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle(fileName = "nic logo.egg", name = 'ghost',
                       localSize = 0.116412728843, 
                       localPosition = P3(  -0.32,   -0.12,   -0.41), 
                       localOrientation = HPR(   0.00,    0.00,    0.06), 
                       cRadius = 1.0, cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)
def terrain(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle(fileName = "nics real terrain.egg", name = 'terrain',
                       localSize = 0.548545095069, localPosition = P3(   0.00,    0.00,    0.04),
                       localOrientation = HPR(  -0.00,    0.00,    0.00),
                       cRadius = 1.0, cFloor = 0.0, cTop = 1.0, 
                       cType = 'cyl', **a)
                       
def bug(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle(fileName = "bug.egg", name = 'bug',
                       localSize = 0.0980678654642, 
                       localPosition = P3(   0.00,    0.00,    0.54), 
                       localOrientation = HPR(   0.00,    0.00,    0.00), 
                       cRadius = 1.0, cFloor = 0.0, cTop = 1.0, cType = 'sphere'
                       , **a)
def propeller(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle(fileName = "nics logo2.egg", name = 'propeller',
            localSize = 7.49030628891, localPosition = P3(   0.69,    0.06,    0.00),
            localOrientation = HPR(  -0.11,   -0.88,   -0.11), cRadius = 1.0, 
            cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)