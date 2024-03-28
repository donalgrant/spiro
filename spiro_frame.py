from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos

def on_frame(sd,skip=1,scale=1.0,oangle=pi/3,fb=0.5,fh=0.5,asym=0,orient=0,polyfunc=None,  # tcoords or pcoords
             pts=100,first=0,n=None,orient_follow=None,arc_angle=0,object=0,prot=0,vertex_order=None,
             pin_coord=None,pin_to_frame=0.0,autoscale=True,pinned_vertex=0,
             frame_intersect=False):
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
        
        if (pin_coord is None):
            fcoord = sd.xy(i)
        else:
            fcoord = pin_to_frame*sd.xy(i) + (1.0-pin_to_frame)*pin_coord
            
        T.load(polyfunc(oa,ay,fb=fbk,fh=fhk,prot=pr),ph,frame_x=fcoord[0],frame_y=fcoord[1])
        
        if not pin_coord is None:

            pv = array_val(pinned_vertex,k)
            seg_length = dist(array( [ T.xy(0), T.xy(pv) ] ))
            seg_dir = dir(array( [ T.xy(0), T.xy(pv) ] )) if seg_length > 0 else 0
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
                    frame_x=fcoord[0],frame_y=fcoord[1])
            tt += npts

        S.add(st.scale(sc).rotate(array_val(orient_angle,k)).disp(fcoord))
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

'''
F1 is used as the "frame", and F2 is the frame used as pin coordinates
variations in the parameters are done along the pin coordinates.
If the normal_intersect flag is set, then the pin-coordinate will be the
intersection point for the two normals for each frame, possibly modified by norm_off1 and norm_off2.
Note that if n1 > 1, the intersection point will only be calculated using the first coord in frame 1;
each call to on_frame is only passed a single pin-coordinate.
'''

def frame_pair(F1,F2,skip1=1,skip2=1,first1=0,first2=0,
               scale=1.0,oangle=pi/3,fb=0.0,fh=0.0,asym=0,orient=0,polyfunc=None,  # tcoords or pcoords
               pts=100,n1=1,n2=None,arc_angle=0,object=0,prot=0,vertex_order=None,
               pin_to_frame1=0.0,autoscale=True,pinned_vertex=0,show_side=None,
               normal_intersect=False,norm_off1=0.0,norm_off2=0.0,frame_only=False,intersect_tol=1.0e-3):

    S = SpiroData()
    max_n = F2.n() if n2 is None else n2
    
    for i in range(max_n):

        j2 = first2+i*array_val(skip2,i)
        p2 = F2.xy(j2)
        sk1 = array_val(skip1,i)
        j1 = array_val(first1,i)+i*sk1
        
        if normal_intersect:
            pc = intersect(F1.xy(j1),p2,F1.direction(j1)+pi/2+array_val(norm_off1,i),
                           F2.direction(j2)+pi/2+array_val(norm_off2,i),tol=intersect_tol)
        else:
            pc=p2

        if show_side is None:
            npts = array_val(pts,i)
        else:
            npts = show_side * array_val(pts,i)
        
        if pc is not None:
            if frame_only:
                S.add(on_frame(F1,skip=sk1,first=j1,n=array_val(n1,i),
                               scale=0,oangle=0,fb=0,fh=0,asym=0,orient=0,polyfunc=dcoords,
                               pts=1,arc_angle=0,object=array_val(object,i),prot=0,
                               pin_coord=pc,pin_to_frame=array_val(pin_to_frame1,i),
                               autoscale=False,pinned_vertex=0))
            else:
                S.add(on_frame(F1,skip=sk1,first=j1,n=array_val(n1,i),
                               scale=array_val(scale,i),oangle=array_val(oangle,i),
                               fb=array_val(fb,i),fh=array_val(fh,i),asym=array_val(asym,i),
                               orient=array_val(orient,i),polyfunc=polyfunc,
                               pts=npts,arc_angle=array_val(arc_angle,i),
                               object=array_val(object,i),prot=array_val(prot,i),vertex_order=vertex_order,
                               pin_coord=pc,pin_to_frame=array_val(pin_to_frame1,i),
                               autoscale=array_val(autoscale,i),pinned_vertex=array_val(pinned_vertex,i)))
    return S

def ellipses_from_coord(sd,coord=array([0,0]),offset=100,npts=500,
                        scale_major=1.0,
                        orient_offset=0.0,
                        off_major=1.0,off_minor=0.0,
                        eccen=0.8,nfigs=0,i2_start=-1,object=0):
    
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
        st.load(s,phase,object=array_val(object,i),segment=i,
                frame_x=coord[0],frame_y=coord[1]).move(oM*a,om*b).rotate(o-orient).move(x0,y0)
            
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
                                   eccen,nfigs,i2_start,object=i))
        
    return st

def ellipses_on_frame(sd,major,eccen,orient,pts,first=0,n=None,object=0):
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
        s = ecoords(array_val(eccen,i),array_val(pts,i))*array_val(major,i)
        st = SpiroData()
        st.load(s,array_val(sd.p,i),object=array_val(object,i),segment=i,
                frame_x=sd.xy(i)[0],frame_y=sd.xy(i)[1]).rotate(array_val(orient,i)).disp(sd.xy(i))
        S.add(st)
    return S

def ellipses_between_frames(s1,s2,step1,step2,
                            scale_major,orient_offset,off_major,off_minor,eccen,
                            nfigs,pts,bias=0.5,istart1=0,istart2=0,object=0):
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
        st.load(s,ph,object=array_val(object,k),segment=k,
                frame_x=c1[0],frame_y=c1[1]).move(oM*a,om*b).rotate(oo-o).disp( (1-fb)*c1 + fb*c2 )
        S.add(st)
        
        i1 += array_val(step1,k)
        i2 += array_val(step2,k)
        
    return S
