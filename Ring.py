import numpy as np
from numpy import pi

class Ring:

    def __init__(self,radius,origin=np.array([0,0]),orient=0):
        self.r = radius
        self.O = origin
        self.o = orient
        self.c = 2 * pi * radius

        

    
