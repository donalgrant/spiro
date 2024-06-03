import numpy as np
from numpy import array, append, column_stack, abs, sqrt, arctan2, linspace

from SpiroGeometry import *
import pickle

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
        self.v = array([])   # flag:  1 if valid, 0 if invalid
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
        self.v = append(self.v,sd.v)
        return self

    # use add_invalid to maintain correspondence of points to a source, even if some points are undefined/invalid
    def add_invalid(self, sd):
        self.x = append(self.x,sd.x)
        self.y = append(self.y,sd.y)
        self.p = append(self.p,sd.p)
        self.t = append(self.t,sd.t)
        self.o = append(self.o,sd.o)
        self.s = append(self.s,sd.s)
        self.fx = append(self.fx,sd.fx)
        self.fy = append(self.fy,sd.fy)
        self.v = append(self.v,sd.v*0)   # mark all points as invalid
        return self

    def set(self,x=0,y=0,p=0,t=0,o=0,s=0,fx=0,fy=0,v=1):
        self.x = array([x])
        self.y = array([y])
        self.p = array([p])
        self.t = array([t])
        self.o = array([o])
        self.s = array([s])
        self.fx = array([fx])
        self.fy = array([fy])
        self.v = array([v])
        return self

    def set_array(self,x,y,p=None,t=None,o=None,s=None,fx=None,fy=None,v=None):
        self.x = x
        self.y = y
        self.p = self.x*0                 if p  is None else p
        self.t = linspace(0,1,x.shape[0]) if t  is None else t
        self.o = self.x*0                 if o  is None else o
        self.s = self.x*0                 if s  is None else s
        self.fx = self.x                  if fx is None else fx
        self.fy = self.y                  if fy is None else fy
        self.v = self.x*0+1               if v  is None else v
        return self

    def load(self,xy_array,phase=0.0,time_offset=0,object=0,segment=0,frame_x=0,frame_y=0):
        s = SpiroData()
        s.x=xy_array[:,0]
        s.y=xy_array[:,1]
        s.t=linspace(time_offset,time_offset+s.x.shape[0],s.x.shape[0])
        s.p=s.t*0+phase
        s.o=np.full((s.n()),object)
        s.s=np.full((s.n()),segment)
        s.fx=np.full((s.n()),frame_x)
        s.fy=np.full((s.n()),frame_y)
        s.v= np.full((s.n()),1)
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
        i1 = (i1-1+self.n()) % self.n()
        i2 = (i1+1) % self.n()
        return arctan2(self.y[i2]-self.y[i1],self.x[i2]-self.x[i1])

    def fdirection(self,i1):
        i1 = (i1-1+self.n()) % self.n()
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

    def direction_to_coord(self,i,coord):
        iw = self.wrap(i)
        return arctan2(coord[1]-self.y[iw],coord[0]-self.x[iw])

    def direction_to_frame(self,i):
        return self.direction_to_coord(i,self.fxy(i))

    def directions_to_frame(self):
        return array([ self.direction_to_frame(i) for i in range(self.n()) ])
    
    def frame_offset_dir(self,i):
        return self.direction_to_frame(i)-self.fdirection(i)

    def dirs_off_frame(self):
        return array([ self.frame_offset_dir(i) for i in range(self.n()) ])
    
    def dist_to_coord(self,i,coord):
        iw = self.wrap(i)
        return dist(array([ self.xy(i), coord ]))

    def dist_to_frame(self,i):
        return self.dist_to_coord(i,self.fxy(i))

    def dists_to_frame(self):
        return array([ self.dist_to_frame(i) for i in range(self.n()) ])

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

    def lengths(self):
        return append([0],path_length(self.x,self.y))
    
    def flengths(self):
        return append([0],path_length(self.fx,self.fy))

    def frac_paths(self):
        return self.lengths()/self.max_path()
    
    def rotate(self,angle):
        coords = rot_coords(angle,column_stack((self.x,self.y)))
        self.x = coords[:,0]
        self.y = coords[:,1]
        return self

    def scale(self,factor):
        self.x*=factor
        self.y*=factor
        self.fx*=factor
        self.fy*=factor
        return self

    def move(self,x0,y0):
        self.x+=x0
        self.y+=y0
        self.fx+=x0
        self.fy+=y0
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
        sd.v = self.v
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
        sd.v =self.v[first::n]
        return sd

    def n(self):  return self.x.shape[0]

    def select(self,condition):
        sd = SpiroData()
        j = condition
        return sd.set_array(self.x[j],self.y[j],self.p[j],
                            self.t[j],self.o[j],self.s[j],
                            self.fx[j],self.fy[j],self.v[j])

    def remove(self,condition):
        sd = SpiroData()
        j = np.in1d(range(self.n()),condition)
        return sd.set_array(self.x[~j],self.y[~j],self.p[~j],
                            self.t[~j],self.o[~j],self.s[~j],
                            self.fx[~j],self.fy[~j],self.v[~j])

    def valid(self):
        sd = self.copy()
        sd = sd.select(sd.v==1)
        return sd
    
    def valid_in_box(self,lbox):
        sd = self.valid()
        sd = sd.select(-lbox<=sd.x)
        sd = sd.select(sd.x<=lbox)
        sd = sd.select(-lbox<=sd.y)
        sd = sd.select(sd.y<=lbox)
        return sd

    def valid_in_radius(self,r):
        sd = self.valid()
        sd = sd.select(sqrt(sd.x**2+sd.y**2)<=r)
        return sd

    def non_zero_intervals(self):
        dr = path_diffs(self.x,self.y)
        return np.where(dr>1.0e-6)
        
    def max_path(self):
        j = self.non_zero_intervals()
        x = self.x[j]
        y = self.y[j]
        dist = path_length(x,y)
        return dist[-1]
    
    def resample(self,interp_dists):
        j = self.non_zero_intervals()
        dist=np.append([0],path_length(self.x[j],self.y[j]))
        bx= make_interp_spline(dist,self.x[j])
        by= make_interp_spline(dist,self.y[j])
        bp= make_interp_spline(dist,self.p[j])
        bt= make_interp_spline(dist,self.t[j])
        bo= make_interp_spline(dist,self.o[j])
        bs= make_interp_spline(dist,self.s[j])
        bfx=make_interp_spline(dist,self.fx[j])
        bfy=make_interp_spline(dist,self.fy[j])
        sd = SpiroData()
        sd.x=bx(interp_dists)
        sd.y=by(interp_dists)
        sd.p=bp(interp_dists)
        sd.t=bt(interp_dists)
        sd.o=bo(interp_dists)
        sd.s=bs(interp_dists)
        sd.fx=bfx(interp_dists)
        sd.fy=bfy(interp_dists)
        sd.v=sd.x*0+1
        return sd

    def oversample(self,factor):
        return self.resample(self.max_path()*frame_sampling(int(factor*self.n()),1.0,'constant'))
    
    def copy(self):
        sd = SpiroData()
        sd.x= np.copy(self.x)
        sd.y= np.copy(self.y)
        sd.p= np.copy(self.p)
        sd.t= np.copy(self.t)
        sd.o= np.copy(self.o)
        sd.s= np.copy(self.s)
        sd.fx=np.copy(self.fx)
        sd.fy=np.copy(self.fy)
        sd.v =np.copy(self.v)
        return sd

    def copy_n(self,n_copies):
        sd = SpiroData()
        for j in range(n_copies):
            sd.add(self)
        return sd
    
    def save(self,filename):
        with open(filename,'wb') as f:
            pickle.dump(self,f,pickle.HIGHEST_PROTOCOL)
        f.close()

def read(filename):
    with open(filename,'rb') as f:
        U = pickle.load(f)
    return U
