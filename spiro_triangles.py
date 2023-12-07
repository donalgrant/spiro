from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos

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
    orient = [ sd.chord_direction(first+j,first+j+offset)+array_val(angle_offset,j) for j in range(0,n,skip) ]
    return triangles_on_frame(sd,skip,scale,oangle,asym=asym,orient=orient,pts=pts,first=first,n=n)



def pars_on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,
                  pts=100,first=0,n=None,orient_follow=None):
    S = SpiroData()
    n = sd.n() if n is None else n
    i = first
    for k in range(n):
        if not orient_follow is None:
            orient_angle = sd.chord_direction(i,i+array_val(orient_follow,k))+array_val(orient,k)
        else:
            orient_angle = array_val(orient,k)
        T = SpiroData()  # for the parallelogram vertices
        T.load(pcoords(array_val(oangle,k),array_val(asym,k),array_val(fb,k),array_val(fh,k)),
               array_val(sd.p,k))
        st = SpiroData() # for the parallelogram sides
        for j in range(T.n()):
            st.load(line(array([ T.xy(j),T.xy(j+1) ]), npts=array_val(pts,k)),T.p[j],
                    time_offset=j*array_val(pts,k))
        S.add(st.scale(array_val(scale,k)).rotate(orient_angle).disp(sd.xy(i)))
        i+=array_val(skip,k)
    return S

def directed_pars(sd,skip=1,offset=None,scale=1.0,oangle=pi/3,
                  asym=0,angle_offset=0,pts=100,first=0,n=None):
    if n is None: n = sd.n()
    if offset is None:  offset=sd.n()//3
    return pars_on_frame(sd,skip,scale,oangle,asym=asym,pts=pts,first=first,n=n,
                         orient_follow=offset,orient=angle_offset)

'''
def directed_pars(sd,skip=1,offset=None,scale=1.0,oangle=pi/3,asym=0,angle_offset=0,
                  pts=100,first=0,n=None):
    if n is None: n = sd.n()
    if offset is None: offset = sd.n()//3
    orient = [ sd.chord_direction(first+j,first+j+offset)+array_val(angle_offset,j) for j in range(0,n,skip) ]
    return pars_on_frame(sd,skip,scale,oangle,asym=asym,orient=orient,pts=pts,first=first,n=n)
'''
