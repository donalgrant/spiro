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

    return sd.set_array(x0+r*sin(p),y0+r*cos(p),p,t,object,segment,x0,y0,1)


class SpiroData:
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        return self.set_array(array([]),array([]))

#  x: x-coord
#  y: y-coord
#  p: wheel phase
#  t: overall parameterization
#  o: object number
#  s: segment number
#  fx: frame x-coord
#  fy: frame y-coord
#  v: flag:  1 if valid, 0 if invalid

    def update_coords(self, x, y):
        self.x=x
        self.y=y
        if (x.shape[0]!=y.shape[0]):
            print(f'***>ERROR:  Length mismatch -- x{x.shape[0]}!=y{y.shape[0]}')
        return self

    def add(self, sd, valid=True):
        sdv = sd.v if valid else sd.v*0
        return self.set_array(append(self.x,sd.x),append(self.y,sd.y),append(self.p,sd.p),  append(self.t,sd.t),
                              append(self.o,sd.o),append(self.s,sd.s),append(self.fx,sd.fx),append(self.fy,sd.fy),
                              append(self.v,sdv))

    # use add_invalid to maintain correspondence of points to a source, even if some points are undefined/invalid
    def add_invalid(self, sd):
        return self.add(sd,False)

    def set_array(self,x,y,p=None,t=None,o=None,s=None,fx=None,fy=None,v=None):
        return self.update_coords(x,y).set_phases(p).set_tcoords(t).set_objects(o).set_segments(s).set_fcoords(fx,fy).set_valid(v)

    def set_phases(self,p=None):
        if p is None: self.p=np.full(self.n(),0.0)
        else:         self.p=p if is_array(p) else np.full((self.n()),p)
        return self

    def set_tcoords(self,t=None):
        if t is None: self.t=linspace(0.0,1.0,self.n())
        else:         self.t=t if is_array(t) else np.full((self.n()),t)
        return self

    def set_fcoords(self,fx=None,fy=None):
        if fx is None: self.fx=np.full(self.n(),0.0)
        else:          self.fx=fx if is_array(fx) else np.full((self.n()),fx)
        if fy is None: self.fy=np.full(self.n(),0.0)
        else:          self.fy=fy if is_array(fy) else np.full((self.n()),fy)
        return self

    def set_objects(self,o=None):
        if o is None: self.o=np.full(self.n(),0)
        else:         self.o=o if is_array(o) else np.full((self.n()),o)
        return self

    def set_segments(self,s=None):
        if s is None: self.s=np.full(self.n(),0)
        else:         self.s=s if is_array(s) else np.full((self.n()),s)
        return self

    def set_valid(self,v=None):
        if v is None: self.v=np.full(self.n(),1)
        else:         self.v=v if is_array(v) else np.full((self.n()),v)
        return self
    
    def load(self,xy_array,phase=0.0,time_offset=0,object=0,segment=0,frame_x=0,frame_y=0,v=1):
        s = SpiroData()
        n = xy_array.shape[0]
        s.set_array(xy_array[:,0],xy_array[:,1],phase,linspace(time_offset,time_offset+n,n),
                    object,segment,frame_x,frame_y,v)
        return self.add(s);
        
    def xc(self):  return self.x[-1] 
    def yc(self):  return self.y[-1] 
    def pc(self):  return self.p[-1]
    def tc(self):  return self.t[-1]
    def oc(self):  return self.o[-1]
    def sc(self):  return self.s[-1]

    def xy(self, index): return array([  self.x[index % self.n()],  self.y[index % self.n()] ])
    def fxy(self,index): return array([ self.fx[index % self.n()], self.fy[index % self.n()] ])

    def xys(self,scale=1.0):
        cc = empty((self.n(),3))
        srange=max(self.s)-min(self.s)
        savg=min(self.s)+srange/2.0
        for i in range(self.n()):
            cc[i]=array([self.x[i],self.y[i],scale*(self.s[i]-savg)/srange])
        return cc

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
    
    def xyf(self,scale=1.0):
        cc = empty((self.n(),3))
        frange=max(self.dists_to_frame())-min(self.dists_to_frame())
        favg=min(self.dists_to_frame())+frange/2.0
        for i in range(self.n()):
            cc[i]=array([self.x[i],self.y[i],scale*(self.dist_to_frame(i)-favg)/frange])
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
        return self.update_coords(coords[:,0],coords[:,1])

    def scale(self,factor):
        return self.update_coords(self.x*factor,self.y*factor).set_fcoords(self.fx*factor,self.fy*factor)

    def move(self,x0,y0):
        return self.update_coords(self.x+x0,self.y+y0).set_fcoords(self.fx+x0,self.fy+y0)

    def disp(self,coord): return self.move(coord[0],coord[1])

    def inverted_radii(self):
        '''return an inverted version of the current data'''
        inv_r = 1/self.radii()  # need to trap 1/0 here
        pp = self.polars()
        x = inv_r * cos(pp)
        y = inv_r * sin(pp)
        sd = self.copy()
        return sd.update_coords(x,y)
    
    def subsample(self,n,first=0):
        '''return a subsampled version of the current data'''
        return self.select(slice(first,self.n(),n))

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

    # need to find a way to add a "closed curve" mod here
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
        return sd.set_array(bx(interp_dists),by(interp_dists),bp(interp_dists),bt(interp_dists),
                            bo(interp_dists),bs(interp_dists),bfx(interp_dists),bfy(interp_dists))

    def oversample(self,factor):
        sd = self.resample(self.max_path()*frame_sampling(int(factor*self.n()),1.0,'constant'))
        return sd # .add(self.select(slice(0,1)))
    
    def copy(self):
        sd = SpiroData()
        return sd.set_array(np.copy(self.x),np.copy(self.y), np.copy(self.p), np.copy(self.t),np.copy(self.o),
                            np.copy(self.s),np.copy(self.fx),np.copy(self.fy),np.copy(self.v))

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
