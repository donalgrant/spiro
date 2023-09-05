import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array,arctan,arctan2
from scipy.special import ellipe, ellipeinc
from scipy import optimize

def circum(major,minor=None):
    if not minor: minor=major
    if major<=minor: return 2*pi*major
    # approximation for Circumference for an ellipse from Wikipedia
    h = (major-minor)**2/(major+minor)**2
    return pi*(major+minor)*(1 + 3*h/(10+sqrt(4-3*h)))

def major_from_circum(c,eccen=0.0):
    if (eccen==0):  return c / (2*pi)
    def f(x):  return circum(x,semi_minor(x,eccen))-c
    bracket=array([ c/(2.1*pi),c/3.9 ])  # circle vs. line for brackets, with space
    sol = optimize.root_scalar(f,bracket=bracket,method='brentq')
    return sol.root
    
from math import fmod
def pfmod(a,b):
    '''a mod b, but requiring the result to be between 0 and <b if a<0'''
    if a>=0:  return fmod(a,b)
    q = fmod(a,b)+b
    if q>=b:  q-=b
    return q
    
def _arclength(T0, T1, a, b):
    '''from John Cook consulting Blog:
    https://www.johndcook.com/blog/2022/11/02/elliptic-arc-length/
    '''
    m = 1 - (b/a)**2
    t1 = ellipeinc(T1 - 0.5*pi, m)
    t0 = ellipeinc(T0 - 0.5*pi, m)
    return a*(t1 - t0)

def semi_minor(semi_major,eccen): return semi_major*sqrt(1.0-eccen**2)
def ellip_T(a,b,phi): return arctan2( (a/b) * sin(phi), cos(phi) )

# only correct results for p0 and pf in upper right quadrant:
# 0 <= p0,pf < pi/2
# use symmetry to get the rest

def _eurq_arc(p0,pf,a,b):
    m = 1 - (b/a)**2
    return a * (ellipeinc(ellip_T(a,b,pf)-pi/2,m) -
                ellipeinc(ellip_T(a,b,p0)-pi/2,m))

def _ellipse_arc(p0,pf,a,b):
    quad=pi/2
    dphi=pf-p0
    if (dphi<0): return -1 * _ellipse_arc(pf,p0,a,b)  # now dphi guaranteed >=0
    
    p0r = pfmod(p0,quad)  # p0r should now be between 0 and quad
    pfr = pfmod(pf,quad)  # pfr should now be between 0 and quad

    nq = (dphi-pfr-(quad-p0r)) / quad  # should be an integer

    '''
    # two sanity checks
    if abs(nq-round(nq)) > 1.0e-6:
        print('nq not integer: ',nq)
        print('  from p0, pf, p0r, pfr = ',p0*180/pi,pf*180/pi,p0r*180/pi,pfr*180/pi)

    if (abs(dphi-(nq*quad+pfr+quad-p0r))>1.0e-6):
        print('dphi does not add up: ',dphi*180/pi,(nq*quad+pfr+quad-p0r)*180/pi)
        print('  from nq, p0, pf, p0r, pfr = ',nq,p0*180/pi,pf*180/pi,p0r*180/pi,pfr*180/pi)
    '''
    
    return nq*circum(a,b)/4 + _eurq_arc(0,pfr,a,b) + _eurq_arc(0,quad-p0r,a,b)

class Ellipse:   # might consider making "spacing" part of the Wheel's data

    def __init__(self,major=3, eccen=0.5, pen=2, offset=0, pen_offset=0, origin=np.array([0,0])):
        self.a = major  # semi-major axis
        self.e = eccen  # eccentricity
        self.b = semi_minor(self.a,eccen)
        self.m = pen         # marker position
        self.po = pen_offset # cw angle between semi-major axis and radial to pen
        self.o = offset      # semi-major axis cw angle from the vertical (diff from Wheel)
        self.c = circum(self.a,self.b)
        self.O = origin

        # arc length array -- to be interpolated
#        self.arc = np.array([ ellipse_arc(0,phi) for phi in np.linspace(0,2*pi,1000) ])

    def arc(self,p1,p2):
        return _ellipse_arc(p1,p2,self.a,self.b)

    def r(self,phi=None):
        if not phi: phi = self.o
        return self.a*self.b / sqrt((self.a*sin(phi))**2+(self.b*cos(phi))**2)

    def phi_at_arc(self,arc,p0=0):
        def f(x): return self.arc(p0,x)-arc
        nc = arc // self.c
        guard=0.5 # fraction of circumference to go beyond expected bounds
        bracket = [ (nc-guard)*2*pi+p0 , (nc+1+guard)*2*pi+p0 ]
        if f(bracket[0]) * f(bracket[1]) > 0:
            print('bracket issue with arc=',arc,'; p0=',p0,' nc=',nc,'; ',bracket)
            print(f(bracket[0]),f(bracket[1]))
        sol = optimize.root_scalar(f,bracket=bracket,method='brentq')
#        sol = optimize.root_scalar(f,x0=bracket[0],x1=bracket[1],method='secant')
        return sol.root

    def normal_at_phi(self,phi):   # returns the slope at coordinate phi
        angle = phi  # or ellip_T(self.a,self.b,phi) ?
        ab2 = self.a**2-self.b**2
        denom = self.a**2 - ab2*cos(angle)**2
        numer = ab2*sin(angle)*cos(angle)
        if abs(denom) < 1.0e-8:
            return phi+pi if numer<0 else phi    # not sure about the sign here
        return phi + arctan2(numer,denom)
        
