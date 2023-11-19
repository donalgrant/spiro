from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos

'''
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

'''
# add arc parameters and relpace line with arc call
def triangles_on_frame(sd,offset=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,
                       pts=100,first=0,n=None):
    S = SpiroData()
    n = sd.n() if n is None else n
    i = first
    for k in range(n):
        T = SpiroData()  # for the triangle vertices
        T.load(tcoords(array_val(oangle,k),array_val(asym,k),array_val(fb,k),array_val(fh,k)),
               array_val(sd.p,k))
        st = SpiroData() # for the triangle sides
        for j in range(T.n()):
            st.load(line(array([ T.xy(j),T.xy(j+1) ]), npts=array_val(pts,k)),T.p[j],
                    time_offset=0 if j==0 else array_val(pts,k))
        S.add(st.scale(array_val(scale,k)).rotate(array_val(orient,k)).disp(sd.xy(i)))
        i+=array_val(offset,k)
    return S

def directed_triangles(sd,skip=1,offset=None,scale=1.0,oangle=pi/3,asym=0,angle_offset=0,
                       pts=100,first=0,n=None):

    if n is None: n = sd.n()
    if offset is None: offset = sd.n()//3
    orient = [ sd.chord_direction(first+j,first+j+offset)+angle_offset for j in range(0,n,skip) ]
    return triangles_on_frame(sd,skip,scale,oangle,asym=asym,orient=orient,pts=pts,first=first,n=n)

'''
def ellipses_between_frames(s1,s2,step1,step2,
                            scale_major,orient_offset,off_major,off_minor,eccen,
                            nfigs,pts,bias=0.5,istart1=0,istart2=0):
    S=SpiroData()

    i1 = istart1
    i2 = istart2

    for k in range(nfigs):
        sm = array_val(scale_major,k)
        oo = array_val(orient_offset,k)
        oM = array_val(off_major,k)
        om = array_val(off_minor,k)
        e  = array_val(eccen,k)
        np = array_val(pts,k)
        fb = array_val(bias,k)

        ph = (1-fb)*array_val(s1.p,k)+fb*array_val(s2.p,k)

        c1 = s1.xy(i1)
        c2 = s2.xy(i2)
        ep = array([ c1, c2 ])
        
        o = dir(ep)
        if sm < 0:
            a = -sm
        else:
            a = sm * dist(ep) / 2
        b = semi_minor(a,e)
        
        s = ecoords(e,np)*a
        st = SpiroData()
        st.load(s,ph).move(oM*a,om*b).rotate(oo-o).disp( (1-fb)*c1 + fb*c2 )
        S.add(st)
        
        i1 += array_val(step1,k)
        i2 += array_val(step2,k)
        
    return S
'''
