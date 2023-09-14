import numpy as np
from numpy import array, append, column_stack, abs, sqrt, arctan2, linspace

from SpiroGeometry import *
import pickle


def read_SD(filename):
    with open(filename,'rb') as f:
        U = pickle.load(f)
    return U

def rotate(x0,y0,xr,yr,angle):
    '''rotate the coordinate (xr,yr) about the
    origin (x0,y0) by angle
    '''
    t=linspace(0.0,abs(angle),int(500*abs(angle)/pi))
    r=sqrt((xr-x0)**2+(yr-y0)**2)
    phi=arctan2(xr-x0,yr-y0)

    p = t
    
    if (angle<0):
        p *= -1

    p += phi
    
    sd = SpiroData()
    
    sd.x = x0+r*sin(p)
    sd.y = y0+r*cos(p)
    sd.p = p
    sd.t = t
        
    return sd

class SpiroData:
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = array([])
        self.y = array([])
        self.p = array([])
        self.t = array([])   # parameterize the drawing data (not sure if this is needed yet)
        return self

    def add(self, sd):
        self.x = append(self.x,sd.x)
        self.y = append(self.y,sd.y)
        self.p = append(self.p,sd.p)
        self.t = append(self.t,sd.t)
        return self

    def set(self,x=0,y=0,p=0,t=0,m=1):
        self.x = array([x])
        self.y = array([y])
        self.p = array([p])
        self.t = array([t])
        return self

    def set_array(self,x,y,p,t):
        self.x = x
        self.y = y
        self.p = p
        self.t = t
        return self
    
    def xc(self):  return self.x[-1] 
    def yc(self):  return self.y[-1] 
    def pc(self):  return self.p[-1]
    def tc(self):  return self.t[-1]
    
    def rotate(self,angle):
        coords = rot_coords(angle,column_stack((self.x,self.y)))
        self.x = coords[:,0]
        self.y = coords[:,1]
        return self

    def move(self,x0,y0):
        self.x+=x0
        self.y+=y0
        return self
        
    def subsample(self,n):
        '''return a subsampled version of the current data'''
        sd = SpiroData()
        sd.x=self.x[::n]
        sd.y=self.y[::n]
        sd.p=self.p[::n]
        sd.t=self.t[::n]
        return sd

    def n(self):  return self.x.shape[0]

    def save(self,filename):
        with open(filename,'wb') as f:
            pickle.dump(self,f,pickle.HIGHEST_PROTOCOL)
        f.close()

    def read(filename):
        with open(filename,'rb') as f:
            U = pickle.load(f)
        return U
