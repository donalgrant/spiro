from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos


def ellipses_from_coord(sd,coord=array([0,0]),offset=100,npts=500,
                        scale_major=1.0,
                        orient_offset=0.0,
                        off_major=1.0,off_minor=0.0,
                        eccen=0.8,nfigs=0,i2_start=-1):
    
    S = SpiroData()
    if nfigs==0: nfigs = int(sd.n()/offset)
    x0=coord[0]
    y0=coord[1]
    if i2_start<0:
        initial_i2 = np.random.randint(0,sd.n())
    else:
        initial_i2 = i2_start
    if initial_i2 < 0:  initial_i2=0

    for i in range(0,nfigs):
 
        e = array_val(eccen,i)
        n = array_val(npts,i)
        o = array_val(orient_offset,i)
            
        i2=(i*offset+initial_i2) % sd.n()
        
        end_pt = array([ coord, sd.xy(i2) ])
        orient = arctan2(sd.y[i2]-y0,sd.x[i2]-x0)

        sm = array_val(scale_major,i)
        
        a = sm * dist(end_pt)/2
        b = semi_minor(a,e)
        oM = array_val(off_major,i)
        om = array_val(off_minor,i)
        
        phase = sd.p[i2]

        s = ecoords(e,n)*a
        st = SpiroData()
        st.load(s,phase).move(oM*a,om*b).rotate(o-orient).move(x0,y0)
            
        S.add(st)
        
    return S

def ellipses_from_pts(sd,n=3,offset=100,npts=500,scale_major=1.0,
                      orient_offset=0.0, off_major=1.0, off_minor=0.0,
                      eccen=0.8, nfigs=0, fixed=0):

    st = SpiroData()
    for i in range(n):
        j = np.random.randint(0,sd.n())
        i2_start=-1 if fixed==0 else j+fixed

        st.add(ellipses_from_coord(sd,array([ sd.x[j], sd.y[j] ]),offset,npts,
                                   scale_major,orient_offset,off_major,off_minor,
                                   eccen,nfigs,i2_start))
        
    return st

def ellipses_on_frame(sd,major,eccen,orient,pts,first=0,n=None):
    '''Every argument except the first may be an array:
    sd = SpiroData frame on which to draw the ellipses
    major:  semi-major axis of ellipses
    eccen:  eccentricity for each ellipse
    orient: orientation for each ellipse
    pts:    number of points to draw in the arc
    '''
    S = SpiroData()
    last = first+sd.n() if n is None else first+n
    for i in range(first,last):
        ne = array_val(pts,i)
        s = ecoords(array_val(eccen,i),array_val(pts,i))*array_val(major,i)
        st = SpiroData()
        st.load(s,array_val(sd.p,i)).rotate(array_val(orient,i)).disp(sd.xy(i))
        S.add(st)
    return S

def ellipses_between_frames(s1,s2,step1,step2,
                            scale_major,orient_offset,off_major,off_minor,eccen,
                            nfigs,pts,istart1=0,istart2=0):
    S=SpiroData()

    return S
