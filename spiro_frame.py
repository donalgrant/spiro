from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos

def on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,polyfunc=None,  # tcoords or pcoords
             pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0,prot=0,vertex_order=None,
             pin_coord=None,pin_to_frame=False,autoscale=True,pinned_vertex=0):
    '''
    polyfunc is a function providing vertex coordinates to draw on the frame.  It has five
    parameters: two shape parameters (e.g., opening angle and asymmetry),
                two offset parameters to specify the distance from the frame to draw the object, and
                a "pre-rotation" angle, the angle about which to rotate the figure before applying the offset
    if pin_coord is specified, then the origin of each object is that coordinate, with scale and orientation
    corresponding to the points on the frame.  (orient_follow is ignored in this case.)
    If pinned_vertex is set to an index other than zero, then the size of the segment between
    vertex 0 and the pinned_vertex will be used for the scaling of the figure.
    '''
    
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
        sc = array_val(scale,k)
        fx = sd.xy(i)[0]
        fy = sd.xy(i)[1]
        T.load(polyfunc(oa,ay,fb=fbk,fh=fhk,prot=pr),ph,frame_x=fx,frame_y=fy)
        
        if not pin_coord is None:
            
            seg_length = dist(array( [ T.xy(0), T.xy(pinned_vertex) ] ))
            seg_dir = dir(array( [ T.xy(0), T.xy(pinned_vertex) ] )) if seg_length > 0 else 0
            pc_dir = sd.direction_to_coord(i,pin_coord)
            orient_angle = -pc_dir if pin_to_frame else pi-pc_dir
            orient_angle += seg_dir
            orient_angle -= array_val(orient,k)
            if autoscale:
                sc *= sd.dist_to_coord(i,pin_coord)
                if seg_length > 0:
                    sc /= seg_length
                
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
                    frame_x=fx,frame_y=fy)
            tt += npts

        if (pin_coord is None) or pin_to_frame:
            loc_coord = sd.xy(i)
        else:
            loc_coord = pin_coord

        S.add(st.scale(sc).rotate(array_val(orient_angle,k)).disp(loc_coord))
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

def crosses_on_frame(sd,asym=0,top_ratio=1.0,bottom_ratio=1.0,skip=1,scale=1,orient=0,
                     pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0,prot=0):
    '''draw a set of four rectangles arranged in the shape of a cross:
       asym gives the rectangular ratio for the cross-pieces (left and right are equal)
       top_ratio is the size of top rectangle relative to cross-piece
       bottom_ratio is the size of the bottom rectangle relative to cross-piece
    '''

    oa=pi/2

    n = sd.n() if n is None else n

    tbr = ((1+asym)/(1-asym))

    # to calculate length of arrays, use n divided by the average of the skip array (if an array), rounding down

    skip_n = skip if np.isscalar(skip) else np.average(skip)
    range_n = int(n/skip_n)
    
    tt = array( [array_val(tbr,j)*array_val(top_ratio,   j) for j in range(range_n)] )
    bb = array( [array_val(tbr,j)*array_val(bottom_ratio,j) for j in range(range_n)] )

    st = array( [array_val(scale,j)*array_val(top_ratio,   j) for j in range(range_n)] )
    sb = array( [array_val(scale,j)*array_val(bottom_ratio,j) for j in range(range_n)] )
    
    tta = (tt-1)/(tt+1)
    bba = (bb-1)/(bb+1)

    S=SpiroData()

    p=np.zeros(0,dtype=int)
    for j in range(range_n):
        nj=array_val(pts,j)
        ttj = array_val(tt,j)
        p=np.append(p,array( [int(nj*ttj),int(nj/ttj),int(nj*ttj),0] ))
    
    S.add(on_frame(sd,scale=st,oangle=oa,first=first,n=n,skip=skip,fh=-1,fb=-1,
                   asym=tta,orient_follow=orient_follow,orient=orient,polyfunc=pcoords,
                   arc_angle=arc_angle,pts=p,object=object,prot=-pi/2))

    p=np.zeros(0,dtype=int)
    for j in range(range_n):
        nj=array_val(pts,j)
        tbj = array_val(tbr,j)
        p=np.append(p,array( [int(nj*tbj),int(nj/tbj),int(nj*tbj),0] ))
        
    S.add(on_frame(sd,scale=scale,oangle=oa,first=first,n=n,skip=skip,fh=-1,fb=0,
                   asym=asym,orient_follow=orient_follow,orient=orient,polyfunc=pcoords,
                   arc_angle=arc_angle,pts=p,object=object,prot=pi))

    p=np.zeros(0,dtype=int)
    for j in range(range_n):
        nj=array_val(pts,j)
        bbj = array_val(bb,j)
        p=np.append(p,array( [int(nj*bbj),int(nj/bbj),int(nj*bbj),0] ))

    S.add(on_frame(sd,scale=sb,oangle=oa,first=first,n=n,skip=skip,fh=0,fb=0,
                   asym=bba,orient_follow=orient_follow,orient=orient,polyfunc=pcoords,
                   arc_angle=arc_angle,pts=p,object=object,prot=pi/2))

    p=np.zeros(0,dtype=int)
    for j in range(range_n):
        nj=array_val(pts,j)
        tbj = array_val(tbr,j)
        p=np.append(p,array( [int(nj*tbj),int(nj/tbj),int(nj*tbj),0] ))

    S.add(on_frame(sd,scale=scale,oangle=oa,first=first,n=n,skip=skip,fh=0,fb=-1,
                   asym=asym,orient_follow=orient_follow,orient=orient,polyfunc=pcoords,
                   arc_angle=arc_angle,pts=p,object=object,prot=0))

    return S
