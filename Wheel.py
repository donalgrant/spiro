from numpy import pi

class Wheel: 

    def __init__(self,radius=3.0, pen=2.0, offset=0):
        self.r = radius # radius of the wheel
        self.m = pen    # marker position
        self.o = offset # cw angle from the vertical
        self.c = 2*pi*self.r  # circumference

    def arc(self,phi): return self.c * phi / (2*pi)
