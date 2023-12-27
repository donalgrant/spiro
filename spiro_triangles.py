from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos

# add arc parameters and relpace line with arc call

def triangles_on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,
                       pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0):
    S = SpiroData()
    n = sd.n() if n is None else n
    i = first
    for k in range(n):
        if not orient_follow is None:
            orient_angle = -sd.chord_direction(i,i+array_val(orient_follow,k))-array_val(orient,k)
        else:
            orient_angle = -array_val(orient,k)
        T = SpiroData()  # for the triangle vertices
        T.load(tcoords(array_val(oangle,k),array_val(asym,k),array_val(fb,k),array_val(fh,k)),
               array_val(sd.p,k))
        st = SpiroData() # for the triangle sides
        tt = 0
        for j in range(T.n()):
            npts=array_val(pts,k*T.n()+j)
            st.load(arc_between_pts(array([ T.xy(j),T.xy(j+1) ]),
                                    arc_subtended=array_val(arc_angle,k*T.n()+j),npts=npts),
                                    T.p[j], time_offset=tt,object=array_val(object,k*3+j),segment=j)
            tt += npts
        S.add(st.scale(array_val(scale,k)).rotate(array_val(orient_angle,k)).disp(sd.xy(i)))
        i+=array_val(skip,k)
    return S

def directed_triangles(sd,skip=1,offset=None,scale=1.0,oangle=pi/3,
                       asym=0,angle_offset=0,pts=100,first=0,n=None,object=0):
    if n is None: n = sd.n()
    if offset is None: offset = sd.n()//3   
    return triangles_on_frame(sd,skip,scale,oangle,asym=asym,pts=pts,first=first,n=n,
                              orient_follow=offset,orient=angle_offset,object=object)

#    orient = [ sd.chord_direction(first+j,first+j+offset)+array_val(angle_offset,j) for j in range(0,n,skip) ]
#    return triangles_on_frame(sd,skip,scale,oangle,asym=asym,orient=orient,pts=pts,first=first,n=n)



def pars_on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,
                  pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0):
    S = SpiroData()
    n = sd.n() if n is None else n
    i = first
    for k in range(n):
        if not orient_follow is None:
            orient_angle = -sd.chord_direction(i,i+array_val(orient_follow,k))-array_val(orient,k)
        else:
            orient_angle = -array_val(orient,k)
        T = SpiroData()  # for the parallelogram vertices
        T.load(pcoords(array_val(oangle,k),array_val(asym,k),array_val(fb,k),array_val(fh,k)),
               array_val(sd.p,k))
        st = SpiroData() # for the parallelogram sides
        tt = 0
        for j in range(T.n()):
            np=array_val(pts,k*T.n()+j)
            st.load(arc_between_pts(array([ T.xy(j),T.xy(j+1) ]),
                                    arc_subtended=array_val(arc_angle,k*T.n()+j),npts=np),
                    T.p[j], time_offset=tt,object=array_val(object,k*4+j),segment=j)
            tt += np
        S.add(st.scale(array_val(scale,k)).rotate(orient_angle).disp(sd.xy(i)))
        i+=array_val(skip,k)
    return S

def directed_pars(sd,skip=1,offset=None,scale=1.0,oangle=pi/3,
                  asym=0,angle_offset=0,pts=100,first=0,n=None,object=0):
    if n is None: n = sd.n()
    if offset is None:  offset=sd.n()//3
    return pars_on_frame(sd,skip,scale,oangle,asym=asym,pts=pts,first=first,n=n,
                         orient_follow=offset,orient=angle_offset,object=object)


