import numpy as np
from numpy import array, append, column_stack, abs, sqrt, arctan2, linspace

from SpiroGeometry import *
import pickle

def array_val(a,i):
    '''Generic function to extract an element of an array, with
    wrapping on the element number.  If what is passed is a scalar,
    then the scalar itself is returned.'''
    
    return a[i%len(a)] if hasattr(a,"__len__") else a

def array_or_scalar_len(a):
    return len(a) if hasattr(a,"__len__") else 1

def read_SD(filename):
    with open(filename,'rb') as f:
        U = pickle.load(f)
    return U

def rotate(x0,y0,xr,yr,angle,object=0,segment=0):
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
    sd.o = t*0+object
    sd.s = t*0+segment
    sd.fx = t*0+x0
    sd.fy = t*0+y0
        
    return sd

class SpiroData:
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = array([])  # x-coord
        self.y = array([])  # y-coord
        self.p = array([])  # wheel phase
        self.t = array([])  # overall parameterization
        self.o = array([])  # object number
        self.s = array([])  # segment number
        self.fx = array([])  # frame x-coord
        self.fy = array([])  # frame y-coord
        return self

    def add(self, sd):
        self.x = append(self.x,sd.x)
        self.y = append(self.y,sd.y)
        self.p = append(self.p,sd.p)
        self.t = append(self.t,sd.t)
        self.o = append(self.o,sd.o)
        self.s = append(self.s,sd.s)
        self.fx = append(self.fx,sd.fx)
        self.fy = append(self.fy,sd.fy)
        return self

    def set(self,x=0,y=0,p=0,t=0,o=0,s=0,fx=0,fy=0):
        self.x = array([x])
        self.y = array([y])
        self.p = array([p])
        self.t = array([t])
        self.o = array([o])
        self.s = array([s])
        self.fx = array([fx])
        self.fy = array([fy])
        return self

    def set_array(self,x,y,p,t,o,s,fx,fy):
        self.x = x
        self.y = y
        self.p = p
        self.t = t
        self.o = o
        self.s = s
        self.fx = fx
        self.fy = fy
        return self

    def load(self,xy_array,phase,time_offset=0,object=0,segment=0,frame_x=0,frame_y=0):
        s = SpiroData()
        s.x=xy_array[:,0]
        s.y=xy_array[:,1]
        s.t=linspace(time_offset,time_offset+s.x.shape[0],s.x.shape[0])
        s.p=s.t*0+phase
        s.o=np.full((s.n()),object)
        s.s=np.full((s.n()),segment)
        s.fx=np.full((s.n()),frame_x)
        s.fy=np.full((s.n()),frame_y)
        return self.add(s);
        
    def xc(self):  return self.x[-1] 
    def yc(self):  return self.y[-1] 
    def pc(self):  return self.p[-1]
    def tc(self):  return self.t[-1]
    def oc(self):  return self.o[-1]
    def sc(self):  return self.s[-1]

    def xy(self, index): return array([  self.x[index % self.n()],  self.y[index % self.n()] ])
    def fxy(self,index): return array([ self.fx[index % self.n()], self.fy[index % self.n()] ])

    def xyp(self,scale=1.0):
        cc = empty((self.n(),3))
        prange=max(self.p)-min(self.p)
        pavg=min(self.p)+prange/2.0
        for i in range(self.n()):
            cc[i]=array([self.x[i],self.y[i],scale*(self.p[i]-pavg)/prange])
        return cc

    
    def xyt(self,scale=1.0):
        cc = empty((self.n(),3))
        trange=max(self.t)-min(self.t)
        tavg=min(self.t)+trange/2.0
        for i in range(self.n()):
            cc[i]=array([self.x[i],self.y[i],scale*(self.t[i]-tavg)/trange])
        return cc

    
    def xyl(self,scale=1.0):
        cc = empty((self.n(),3))
        lrange=self.n()
        lavg=self.n()/2
        for i in range(self.n()):
            cc[i]=array([self.x[i],self.y[i],scale*cos(pi*(i-lavg)/lrange)])
            
        return cc
    
    def wrap(self,i):  return i % self.n()
    
    def direction(self,i1):
        i1 = i1 % self.n()
        i2 = (i1+1) % self.n()
        return arctan2(self.y[i2]-self.y[i1],self.x[i2]-self.x[i1])

    def fdirection(self,i1):
        i1 = i1 % self.n()
        i2 = (i1+1) % self.n()
        return arctan2(self.fy[i2]-self.fy[i1],self.fx[i2]-self.fx[i1])

    def directions(self):
        return array([ self.direction(i) for i in range(self.n()) ])

    def fdirections(self):
        return array([ self.fdirection(i) for i in range(self.n()) ])

    def chord_direction(self,i1,i2):
        i1w = self.wrap(i1)
        i2w = self.wrap(i2)
        return arctan2(self.y[i2w]-self.y[i1w],self.x[i2w]-self.x[i1w])

    def fchord_direction(self,i1,i2):
        i1w = self.wrap(i1)
        i2w = self.wrap(i2)
        return arctan2(self.fy[i2w]-self.fy[i1w],self.fx[i2w]-self.fx[i1w])

    def chord_dirs(self,offset):
        return array([ self.chord_direction(j,j+offset) for j in range(self.n()) ])

    def fchord_dirs(self,offset):
        return array([ self.fchord_direction(j,j+offset) for j in range(self.n()) ])
                       
    def polar(self,i):
        i = i % self.n()
        return arctan2(self.y[i],self.x[i])
                       
    def fpolar(self,i):
        i = i % self.n()
        return arctan2(self.fy[i],self.fx[i])
    
    def polars(self):
        return array([ self.polar(i) for i in range(self.n()) ])
    
    def fpolars(self):
        return array([ self.fpolar(i) for i in range(self.n()) ])
    
    def radius(self,i):
        return dist(array([ self.xy(i), [0,0] ]))

    def radii(self):
        return array([ self.radius(i) for i in range(self.n()) ])
    
    def fradius(self,i):
        return dist(array([ self.fxy(i), [0,0] ]))

    def fradii(self):
        return array([ self.fradius(i) for i in range(self.n()) ])
    
    def chord_dist(self,i1,i2):
        return dist(array([ self.xy(i1), self.xy(i2) ]))
    
    def fchord_dist(self,i1,i2):
        return dist(array([ self.fxy(i1), self.fxy(i2) ]))

    def chord_dists(self,offset):
        return array([ self.chord_dist(j,j+offset) for j in range(self.n()) ])

    def fchord_dists(self,offset):
        return array([ self.fchord_dist(j,j+offset) for j in range(self.n()) ])
    
    def neighbor_dist(self,i):
        return dist(array([ self.xy(i), self.xy(i+1) ]))

    def neighbor_distances(self):
        return array([ self.neighbor_dist(i) for i in range(self.n()) ])
    
    def fneighbor_dist(self,i):
        return dist(array([ self.fxy(i), self.fxy(i+1) ]))

    def fneighbor_distances(self):
        return array([ self.fneighbor_dist(i) for i in range(self.n()) ])
    
    def rotate(self,angle):
        coords = rot_coords(angle,column_stack((self.x,self.y)))
        self.x = coords[:,0]
        self.y = coords[:,1]
        return self

    def scale(self,factor):
        self.x*=factor
        self.y*=factor
        return self

    def move(self,x0,y0):
        self.x+=x0
        self.y+=y0
        return self

    def disp(self,coord): return self.move(coord[0],coord[1])

    def inverted_radii(self):
        '''return an inverted version of the current data'''
        sd = SpiroData()
        sd.p=self.p
        sd.t=self.t
        sd.o=self.o
        sd.s=self.s
        inv_r = 1/self.radii()
        pp = self.polars()
        sd.x = inv_r * cos(pp)
        sd.y = inv_r * sin(pp)
        sd.fx = self.fx
        sd.fy = self.fy
        return sd
    
    def subsample(self,n,first=0):
        '''return a subsampled version of the current data'''
        sd = SpiroData()
        sd.x=self.x[first::n]
        sd.y=self.y[first::n]
        sd.p=self.p[first::n]
        sd.t=self.t[first::n]
        sd.o=self.o[first::n]
        sd.s=self.s[first::n]
        sd.fx=self.fx[first::n]
        sd.fy=self.fy[first::n]
        return sd

    def n(self):  return self.x.shape[0]

    def select(self,condition):
        sd = SpiroData()
        j = condition
        return sd.set_array(self.x[j],self.y[j],self.p[j],
                            self.t[j],self.o[j],self.s[j],
                            self.fx[j],self.fy[j])

    def remove(self,condition):
        sd = SpiroData()
        j = np.in1d(range(self.n()),condition)
        return sd.set_array(self.x[~j],self.y[~j],self.p[~j],
                            self.t[~j],self.o[~j],self.s[~j],
                            self.fx[~j],self.fy[~j])
        
    def save(self,filename):
        with open(filename,'wb') as f:
            pickle.dump(self,f,pickle.HIGHEST_PROTOCOL)
        f.close()

def read(filename):
    with open(filename,'rb') as f:
        U = pickle.load(f)
    return U
