from SpiroData import *
from SpiroGeometry import *
from numpy import array,linspace,fmod,arange

def arcs_from_multi(sd,offset_array,arc_radius=100,invert=False,
                    line_pts=300,max_strings=0,first=0,arc_only=True,arc_always=True):
    st = SpiroData()
    n=len(offset_array)
    i=0
    i1=first % sd.n()
    i2=(i1+offset_array[0]) % sd.n()
    jstring=0
    while True:
        end_pt = array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ])

        
        sti = SpiroData()

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

def arcs_on_frame(sd,radius,subtended,offset,pts,centers):
    '''Every argument may be an array:
    sd = SpiroData frame on which to draw the arcs
    radius:     radius of curvature for each arc
    subtended:  angular extent of arc (0 <= subtended <= 2*pi)
    offset:     start orientation for arc (0 <= offset <= 2*pi)
    pts:        number of points to draw in the arc
    centers:    fraction of radius towards curvature origin to center the arc:
    (0 for arc going through frame point, 1 for curvature origin at frame point)
    '''
    st = SpiroData()
    for i in range(sd.n()):
        s = arc_on_center(sd.xy(i),array_val(radius,i),array_val(subtended,i),
                          array_val(offset,i),array_val(pts,i),array_val(centers,i))
        st.load(s,sd.p[i])
    return st
        
def centered_arcs(sd,arc_radius=100,arc_subtended=None,angle_offset=None,
                  arc_scale=0.1,theta_phase=False,line_pts=300):
    d = sd.neighbor_distances()
    angle_phase = sd.directions() if theta_phase else sd.p
    arc_subtended = 2*pi * d * arc_scale if arc_subtended is None else arc_subtended
    offset = fmod(angle_phase+pi,2*pi) if angle_offset is None else angle_offset
    return arcs_on_frame(sd,arc_radius,arc_subtended,offset,line_pts,0)

def rotating_arcs(sd,arc_radius=100,rotation_rate=1,arc_subtended=None,
                  arc_offset_angle=0,arc_scale=0.1,line_pts=300):
    d = sd.neighbor_distances()
    arc_subtended = 2*pi * d * arc_scale if arc_subtended is None else arc_subtended
    offset=fmod(arange(sd.n())*2*pi/sd.n()*rotation_rate+arc_offset_angle,2*pi)
    return arcs_on_frame(sd,arc_radius,arc_subtended,offset,line_pts,0)

