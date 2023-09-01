import numpy as np
from numpy import array, append, column_stack
from SpiroGeometry import *

class SpiroData:
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = array([])
        self.y = array([])
        self.p = array([])
        self.t = array([])   # parameterize the drawing data (not sure if this is needed yet)

    def add(self, sd):
        self.x = append(self.x,sd.x)
        self.y = append(self.y,sd.y)
        self.p = append(self.p,sd.p)
        self.t = append(self.t,sd.t)

    def set(self,x=0,y=0,p=0,t=0,m=1):
        self.x = array([x])
        self.y = array([y])
        self.p = array([p])
        self.t = array([t])

    def set_array(self,x,y,p,t):
        self.x = x
        self.y = y
        self.p = p
        self.t = t
    
    def xc(self):  return self.x[-1] 
    def yc(self):  return self.y[-1] 
    def pc(self):  return self.p[-1]
    def tc(self):  return self.t[-1]
    
    def rotate(self,angle):
        coords = rot_coords(angle,column_stack((self.x,self.y)))
        self.x = coords[:,0]
        self.y = coords[:,1]
        
    def subsample(self,n):
        '''return a subsampled version of the current data'''
        sd = SpiroData()
        sd.x=self.x[::n]
        sd.y=self.y[::n]
        sd.p=self.p[::n]
        sd.t=self.t[::n]
        return sd

    def n(self):  return self.x.shape[0]
