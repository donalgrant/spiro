from SpiroData import *
from SpiroGeometry import *
from Ellipse import *
import numpy as np
from numpy import array,linspace,fmod,arange,sin,cos


def ellipses_from_coord(sd,coord=array([0,0]),offset=100,npts=500,
                        off_major=-1.0,off_minor=0.0,
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
            
        i2=(i*offset+initial_i2) % sd.n()
        
        end_pt = array([ coord, sd.xy(i2) ])
        orient = arctan2(sd.y[i2]-y0,sd.x[i2]-x0)
        
        a = dist(end_pt)/2
        b = semi_minor(a,e)
        oM = array_val(off_major,i)
        om = array_val(off_minor,i)
        
        phase = sd.p[i2]

        s = ecoords(e,n)*a
        st = SpiroData()
        st.load(s,phase).move(oM*a,om*b).rotate(orient).move(x0,y0)
            
        S.add(st)
        
    return S

'''
def ellipses_from_pts(sd,n=3,offset=100,npts=500,arc_radius=30,
                  invert=False,nLines=30,fixed=0,arc_only=True,arc_always=True):
    st = SpiroData()
    for i in range(n):
        j = np.random.randint(0,sd.n())
        i2_start=-1 if fixed==0 else j+fixed

        st.add(ellipses_from_coord(sd,array([ sd.x[j], sd.y[j] ]),offset,npts,arc_radius,
                               invert=invert,nLines=nLines,arc_only=arc_only,arc_always=arc_always,
                               i2_start=i2_start))
        
    return st



def ellipses_from_multi(sd,offset_array,arc_radius=100,invert=False,
                    line_pts=300,max_strings=0,first=0,arc_only=True,arc_always=True):
    st = SpiroData()
    n=len(offset_array)
    i=0
    i1=first % sd.n()
    i2=(i1+offset_array[0]) % sd.n()
    jstring=0
    while True:
        end_pt = array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ])

        d = dist(end_pt)

        phase = sd.p[i1]
        
        if d <= 2*arc_radius:
            st.load(arc(end_pt,arc_radius,invert=invert,npts=line_pts),phase)
        else:
            if arc_always:
                st.load(arc(end_pt,d/2,invert=invert,npts=line_pts),phase)
            elif not arc_only:
                st.load(line(end_pt,line_pts),phase)
            else:
                pass

        jstring+=1
        i+=1
        i1=i2
        if (max_strings<=0) and (i1+offset_array[i%n])>=sd.n(): break
        i2 = (i2+offset_array[i%n]) % sd.n()  # wrap around if necessary
        if (max_strings>0) and (jstring>=max_strings): break
            
    return st
'''

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

'''


def centered_ellipses(sd,arc_radius=100,arc_subtended=None,angle_offset=None,
                  arc_scale=0.1,theta_phase=False,line_pts=300):
    d = sd.neighbor_distances()
    angle_phase = sd.directions() if theta_phase else sd.p
    arc_subtended = 2*pi * d * arc_scale if arc_subtended is None else arc_subtended
    offset = fmod(angle_phase+pi,2*pi) if angle_offset is None else angle_offset
    return ellipses_on_frame(sd,arc_radius,arc_subtended,offset,line_pts,0)

def rotating_ellipses(sd,arc_radius=100,rotation_rate=1,arc_subtended=None,
                  arc_offset_angle=0,arc_scale=0.1,line_pts=300):
    d = sd.neighbor_distances()
    arc_subtended = 2*pi * d * arc_scale if arc_subtended is None else arc_subtended
    offset=fmod(arange(sd.n())*2*pi/sd.n()*rotation_rate+arc_offset_angle,2*pi)
    return ellipses_on_frame(sd,arc_radius,arc_subtended,offset,line_pts,0)

def ribbon(sd,width,arc_subtended=pi/4,twists=0,twist_start=0,pts=300,trim=False):
    radius = width/arc_subtended
    n = sd.n()-1 if trim else sd.n()
    offsets = linspace(twist_start,twist_start+2*pi*twists,sd.n())
    return ellipses_on_frame(sd,radius,arc_subtended,pi-sd.directions()+offsets,pts,0,n=n)
    # sd.directions() may have one more element than necessary if trim, but
    # the extra element will be ignored.

'''
