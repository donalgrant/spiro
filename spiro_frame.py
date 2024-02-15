from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos

def on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,polyfunc=None,  # tcoords or pcoords
                       pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0,prot=0,vertex_order=None):
    '''polyfunc is a function providing vertex coordinates to draw on the frame.  It has five
    parameters: two shape parameters (e.g., opening angle and asymmetry),
                two offset parameters to specify the distance from the frame to draw the object, and
                a "pre-rotation" angle, the angle about which to rotate the figure before applying the offset'''
    
    S = SpiroData()
    n = sd.n() if n is None else n
    i = first
    for k in range(n):
        if not orient_follow is None:
            orient_angle = -sd.chord_direction(i,i+array_val(orient_follow,k))-array_val(orient,k)
        else:
            orient_angle = -array_val(orient,k)
        T = SpiroData()  # for the triangle vertices
        oa = array_val(oangle,k)
        ay = array_val(asym,k)
        fbk = array_val(fb,k)
        fhk = array_val(fh, k)
        pr = array_val(prot,k)
        ph = array_val(sd.p,i)
        T.load(polyfunc(oa,ay,fb=fbk,fh=fhk,prot=pr),ph,frame_x=sd.xy(i)[0],frame_y=sd.xy(i)[1])
        st = SpiroData() # for the connections between vertices
        tt = 0
        nv=T.n()
        if not vertex_order is None:
            T=T.select(vertex_order)
            nv=T.n()-1
        for j in range(nv):
            npts=array_val(pts,k*T.n()+j)
            st.load(arc_between_pts(array([ T.xy(j),T.xy(j+1) ]),
                                    arc_subtended=array_val(arc_angle,k*T.n()+j),npts=npts),
                    T.p[j], time_offset=tt,object=array_val(object,k),segment=j,
                    frame_x=sd.xy(i)[0],frame_y=sd.xy(i)[1])
            tt += npts
        S.add(st.scale(array_val(scale,k)).rotate(array_val(orient_angle,k)).disp(sd.xy(i)))
        i+=array_val(skip,k)
    return S

def triangles_on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,
                       pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0,prot=0):
    return on_frame(sd,skip=skip,scale=scale,oangle=oangle,fb=fb,fh=fh,asym=asym,orient=orient,
                    pts=pts,first=first,n=n,orient_follow=orient_follow,arc_angle=arc_angle,
                    object=object,prot=prot,polyfunc=tcoords)

def pars_on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,
                       pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0,prot=0):
    return on_frame(sd,skip=skip,scale=scale,oangle=oangle,fb=fb,fh=fh,asym=asym,orient=orient,
                    pts=pts,first=first,n=n,orient_follow=orient_follow,arc_angle=arc_angle,
                    object=object,prot=prot,polyfunc=pcoords)

def directed_triangles(sd,skip=1,offset=None,scale=1.0,oangle=pi/3,
                       asym=0,angle_offset=0,pts=100,first=0,n=None,object=0):
    if n is None: n = sd.n()
    if offset is None: offset = sd.n()//3   
    return triangles_on_frame(sd,skip,scale,oangle,asym=asym,pts=pts,first=first,n=n,
                              orient_follow=offset,orient=angle_offset,object=object)

def directed_pars(sd,skip=1,offset=None,scale=1.0,oangle=pi/3,
                  asym=0,angle_offset=0,pts=100,first=0,n=None,object=0):
    if n is None: n = sd.n()
    if offset is None:  offset=sd.n()//3
    return pars_on_frame(sd,skip,scale,oangle,asym=asym,pts=pts,first=first,n=n,
                         orient_follow=offset,orient=angle_offset,object=object)


