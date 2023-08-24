from SpiroData import *
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array

def circum(major,minor=None):
    if not minor: minor=major
    if major<=minor: return 2*pi*major
    # approximation for Circumference for an ellipse from Wikipedia
    h = (major-minor)**2/(major+minor)**2
    return pi*(major+minor)*(1 + 3*h/(10+sqrt(4-3*h)))
    
class Ellipse:   # might consider making "spacing" part of the Wheel's data

    def __init__(self,major=3, eccen=0.5, pen=2, offset=0):
        self.a = major  # semi-major axis
        self.b = self.a * sqrt(1.0 - eccen**2)  # semi-minor axis
        self.m = pen    # marker position
        self.o = offset # cw angle from the horizontal (diff from Wheel)
        self.c = circum(self.a,self.b)

    def r(self,phi=None):
        if not phi: phi = self.o
        return self.a*self.b / sqrt((self.a*sin(phi))**2+(self.b*cos(phi))**2)


def elliptical_arc(x0=0,y0=0,orient=0,R=10.0,wheel=Ellipse(3,0.5,2,0),
                   loops=1,spacing=pi/4000,inside=True):  
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    Direction of motion can be reversed by setting reverse=True
    '''

    sd = SpiroData()

    a = wheel.a
    b = wheel.b
    m = wheel.m
    offset = wheel.o

    wc = wheel.c
    RC = circum(R)
    
    t=np.linspace(0.0,2*pi*RC/wc*loops,int(loops/spacing))

    iv = -1 if inside else 1
    
    p = t
    
    phi_factor   = 1
    
    # work out start_guard and end_guard effects in invert and reverse situations

    p   = phi_factor   * t + offset
    rp  = np.array([ wheel.r(phi) for phi in p ])
    
    theta = iv * rp / R * t + orient
    r     = R + iv * rp
    
    sd.t=t
    sd.x=x0+r*sin(theta) + (m/a)*rp*sin(p)
    sd.y=y0+r*cos(theta) + (m/a)*rp*cos(p)
    sd.p=p
    
    return sd

def roll_ellipse(x1,y1,x2,y2,ellipse,start_guard=0,end_guard=0,invert=False):
    '''roll in straight line from (x1,y1) to (x2,y2) using ellipse.
    invert keyword controls sense of wheel location:  default
    is above and/or to the right.  invert=True is the opposite.
    '''
    
    C = ellipse.c
    b = wheel.m
    offset = wheel.o
    
    R=sqrt((x2-x1)**2+(y2-y1)**2) - (start_guard+end_guard)  # roll distance
    A=arctan2(y2-y1,x2-x1)                                   # roll angle
    t=np.linspace(0,2*pi*R/C,1000)                           # angle through which the wheel rolls
    
    iv = -1 if invert else 1

    phi_factor = 1
    time_factor = iv * a

    if invert:
        phi_factor  *= -1
        time_factor *= -1
        
    # do we have to swap to end_guard on inversion?

    xs = x1 - iv * a * sin(A) + start_guard * cos(A)
    ys = y1 + iv * a * cos(A) + start_guard * sin(A)

    p = phi_factor * t + offset
    
    sd = SpiroData()
    
    sd.x = xs + time_factor * t * cos(A) + b * sin(p)
    sd.y = ys + time_factor * t * sin(A) + b * cos(p) 
    sd.p = p
    sd.t = t
    
    return sd
