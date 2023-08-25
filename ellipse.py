from SpiroData import *
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array,arctan
from scipy.special import ellipe, ellipeinc

def circum(major,minor=None):
    if not minor: minor=major
    if major<=minor: return 2*pi*major
    # approximation for Circumference for an ellipse from Wikipedia
    h = (major-minor)**2/(major+minor)**2
    return pi*(major+minor)*(1 + 3*h/(10+sqrt(4-3*h)))

def _arclength(T0, T1, a, b):
    '''from John Cook consulting Blog:  https://www.johndcook.com/blog/2022/11/02/elliptic-arc-length/'''
    m = 1 - (b/a)**2
    t1 = ellipeinc(T1 - 0.5*pi, m)
    t0 = ellipeinc(T0 - 0.5*pi, m)
    return a*(t1 - t0)

def semi_minor(semi_major,eccen):  return semi_major*sqrt(1.0-eccen**2)
def ellip_T(a,b,phi):         return arctan( (a/b) * tan(phi) )

# only correct results for p0 and pf in upper right quadrant:
# 0 <= p0,pf <= pi/2
# use symmetry to get the rest

def _eurq_arc(p0,pf,a,b):
    m = 1 - (b/a)**2
    return a * (ellipeinc(ellip_T(a,b,pf)-pi/2,m) -
                ellipeinc(ellip_T(a,b,p0)-pi/2,m))

def _ellipse_arc(p0,pf,a,b):
    dphi=pf-p0
    if (dphi<0): return -1 * _ellipse_arc(pf,p0,a,b)
    nq = abs(dphi) // (pi/2)
    qr = dphi - nq*(pi/2)
    if (p0>=0):
        p0nq = p0 // (pi/2)
        p1 = p0-p0nq*(pi/2)
    else:
        p0nq = abs(p0) // (pi/2)
        p1 = p0+p0nq*(pi/2)
    p2 = p1 + qr
    return nq*circum(a,b)/4 + _eurq_arc(p1,p2,a,b)


class Ellipse:   # might consider making "spacing" part of the Wheel's data

    def __init__(self,major=3, eccen=0.5, pen=2, offset=0):
        self.a = major  # semi-major axis
        self.b = semi_minor(self.a,eccen)
        self.m = pen    # marker position
        self.o = offset # cw angle from the horizontal (diff from Wheel)
        self.c = circum(self.a,self.b)

        # arc length array -- to be interpolated
#        self.arc = np.array([ ellipse_arc(0,phi) for phi in np.linspace(0,2*pi,1000) ])

    def arc(self,p1,p2):
        return _ellipse_arc(p1,p2,self.a,self.b)

    def r(self,phi=None):
        if not phi: phi = self.o
        return self.a*self.b / sqrt((self.a*sin(phi))**2+(self.b*cos(phi))**2)

# duplicate function -- put them in a spiro_math module eventually

def rot_2D(angle):
    '''Matrix will rotate a coordinate by angle_rads cw'''
    return array([ [ cos(angle), sin(angle) ],
                   [-sin(angle), cos(angle)  ] ])

def rot_coords(angle_rads,coords):
    cc = np.empty((coords.shape[0],2))
    for i in range(cc.shape[0]):
        cc[i] = np.matmul(rot_2D(angle_rads),coords[i])

    return cc

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

    # to calculate exact value of phi for one complete loop
    # would neet to solve ellipse.arc(0,phi) for value of phi which
    # makes arc = 2*pi*RC
    
    t=np.linspace(0.0,2*pi*RC/wc*loops,int(loops/spacing))

    iv = -1 if inside else 1
    
    p = t
    
    phi_factor   = 1
    
    # work out start_guard and end_guard effects in invert and reverse situations

    p   = phi_factor   * t + offset
    rp  = np.array([ wheel.r(phi) for phi in p ])

    arc = np.array([ wheel.arc(0,phi) for phi in p ])
    theta = iv * arc / R + orient

    # -theta is the tangent slope at the point of contact
    # rotate the ellipse-based coords by this angle to get
    # figure based coordinates

#    coords = np.empty((t.shape[0],2))  # ellipse ref frame coordinates of the contact point
#    for i in range(t.shape[0]):
#        coords[i]=np.array([ [ rp[i]*sin(p[i]), rp[i]*cos(p[i]) ]  ])

#    ec = rot_coords(-1.0*theta[i],coords)
    
    r     = iv * rp

    # ignore pen position for the moment...
    
    sd.t=t
#    sd.x=x0+R*sin(theta) + iv * ec[i][0]
#    sd.y=y0+R*cos(theta) + iv * ec[i][1]
#    sd.x=x0+R*sin(theta) + iv * rp * (1 - (m/a)) * sin(p)
#    sd.y=y0+R*cos(theta) + iv * rp * (1 - (m/a)) * cos(p)

    # not right, but just looking for a place-holder...

    sd.x = x0 + (R+r) * sin(theta) + rp * (m/a) * sin(p)
    sd.y = y0 + (R+r) * cos(theta) + rp * (m/a) * cos(p)
    
    sd.p=p
    
    return sd

def roll_ellipse(x1,y1,x2,y2,ellipse,start_guard=0,end_guard=0,invert=False):
    '''roll in straight line from (x1,y1) to (x2,y2) using ellipse.
    invert keyword controls sense of wheel location:  default
    is above and/or to the right.  invert=True is the opposite.
    '''
    
    C = ellipse.c
    a = ellipse.a
    b = ellipse.m
    offset = ellipse.o
    
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
