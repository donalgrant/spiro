from SpiroData import *
from SpiroGeometry import *
from numpy import array,linspace,fmod

def spiro_string(sd,subsample=100,line_pts=500):
    s = sd.subsample(subsample)
    st = SpiroData()
    i=0
    for i in range(s.n()-1):
        cc = line(array([ [s.x[i],s.y[i]], [s.x[i+1],s.y[i+1]] ]),line_pts)
        sti = SpiroData()
        sti.x=cc[:,0]
        sti.y=cc[:,1]
        sti.t=linspace(0,sti.x.shape[0],len(cc[:,0]))
        sti.p=sti.t*0+s.p[i]
        st.add(sti)
        
    return st

def string_offset_pairs(sd,offset=1000,step=50,line_pts=500):
    st = SpiroData()
    for i in range(0,sd.n()-offset,step):
        cc = line(array([ [sd.x[i],sd.y[i]], [sd.x[i+offset],sd.y[i+offset]] ]),line_pts)
        sti = SpiroData()
        sti.x=cc[:,0]
        sti.y=cc[:,1]
        sti.t=linspace(0,sti.x.shape[0],sti.x.shape[0])
        sti.p=sti.t*0+sd.p[i]
        st.add(sti)
        
    return st

def string_dispersing_pairs(sd,offset=1000,step=50,step2=100,line_pts=500):
    st = SpiroData()
    i1=0
    i2=i1+offset
    while i2<sd.n():
        cc = line(array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ]),line_pts)
        sti = SpiroData()
        sti.x=cc[:,0]
        sti.y=cc[:,1]
        sti.t=linspace(0,sti.x.shape[0],sti.x.shape[0])
        sti.p=sti.t*0+sd.p[i1]
        st.add(sti)
        i1+=step
        i2+=step2
        
    return st

def string_dispersing_links(sd,offset=1000,step0=50,step=1,line_pts=500):
    st = SpiroData()
    i1=0
    i2=i1+offset
    ip=step0
    while i2<sd.n():
        cc = line(array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ]),line_pts)
        sti = SpiroData()
        sti.x=cc[:,0]
        sti.y=cc[:,1]
        sti.t=linspace(0,sti.x.shape[0],sti.x.shape[0])
        sti.p=sti.t*0+sd.p[i1]
        st.add(sti)
        i1=i2
        ip+=step
        i2=i1+offset
        
    return st

def strings_from_coord(sd,coord=array([0,0]),offset=100,line_pts=500,nLines=0,i2_start=-1):
    st = SpiroData()
    if nLines==0: nLines = int(sd.n()/offset)
    x0=coord[0]
    y0=coord[1]
    if i2_start<0:
        initial_i2 = np.random.random_integers(0,sd.n()-nLines*offset)
    else:
        initial_i2 = i2_start
    if initial_i2 < 0:  initial_i2=0
    for i in range(0,nLines):
        i2=i*offset+initial_i2
        if i2>=sd.n():  break
        cc = line(array([ [x0,y0], [sd.x[i2],sd.y[i2]] ]),line_pts)
        sti = SpiroData()
        sti.x=cc[:,0]
        sti.y=cc[:,1]
        sti.t=linspace(0,sti.x.shape[0],sti.x.shape[0])
        sti.p=sti.t*0+sd.p[i2]
        st.add(sti)
        
    return st

def strings_from_pts(sd,n=3,offset=100,line_pts=500,nLines=30,fixed=0):
    st = SpiroData()
    for i in range(n):
        j = np.random.random_integers(0,sd.n())
        i2_start=-1 if fixed==0 else j+fixed
        st.add(strings_from_coord(sd,array([ sd.x[j], sd.y[j] ]),
                                  offset,line_pts,nLines,i2_start=i2_start))
        
    return st

def strings_from_multi(sd,offset_array,line_pts=500,max_strings=0):
    st = SpiroData()
    n=len(offset_array)
    i=0
    i1=0
    i2=(i1+offset_array[0]) % sd.n()
    jstring=0
    while True:
        cc = line(array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ]),line_pts)
        sti = SpiroData()
        sti.x=cc[:,0]
        sti.y=cc[:,1]
        sti.t=linspace(0,sti.x.shape[0],sti.x.shape[0])
        sti.p=sti.t*0+sd.p[i1]
        st.add(sti)
        jstring+=1
        i+=1
        i1=i2
        if (max_strings<=0) and (i1+offset_array[i%n])>=sd.n(): break
        i2 = (i2+offset_array[i%n]) % sd.n()  # wrap around if necessary
        if (max_strings>0) and (jstring>=max_strings): break
            
    return st

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


def centered_arcs(sd,arc_radius=100,arc_subtended=None,angle_offset=None,
                  arc_scale=0.1,theta_phase=False,line_pts=300,max_strings=0,first=0):
    st = SpiroData()
    i=0
    i1=first % sd.n()
    i2=(i1+1) % sd.n()
    jstring=0
    while True:
        end_pt = array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ])
        d = dist(end_pt)
        phase = sd.p[i1]
        theta = arctan2(sd.y[i2]-sd.y[i1],sd.x[i2]-sd.x[i1])
        angle_phase = theta if theta_phase else phase
        if angle_offset is None:
            offset=fmod(angle_phase+pi,2*pi)
        else:
            offset=angle_offset
        if arc_subtended is None:
            arc_subtended=2*pi*d*arc_scale

        s = arc_on_center(end_pt[0],radius=arc_radius,
                          arc_subtended=arc_subtended,angle_offset=offset,
                          npts=line_pts)
        st.load(s,phase)
        jstring+=1
        i+=1
        i1=i2
        if (max_strings<=0) and (i1+1 >= sd.n()): break
        i2 = (i2+1) % sd.n()  # wrap around if necessary
        if (max_strings>0) and (jstring>=max_strings): break
            
    return st

def rotating_arcs(sd,arc_radius=100,rotation_rate=1,arc_subtended=None,
                  arc_offset_angle=0,arc_scale=0.1,line_pts=300,max_strings=0,first=0):
    st = SpiroData()
    i=0
    i1=first % sd.n()
    i2=(i1+1) % sd.n()
    jstring=0
    while True:
        end_pt = array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ])
        d = dist(end_pt)
        phase = sd.p[i1]
        theta = arctan2(sd.y[i2]-sd.y[i1],sd.x[i2]-sd.x[i1])
        angle_offset=fmod(jstring*2*pi/sd.n()*rotation_rate+arc_offset_angle,2*pi)
        if arc_subtended is None:
            arc_subtended=2*pi*d*arc_scale
        s = arc_on_center(end_pt[0],radius=arc_radius,
                          arc_subtended=arc_subtended,angle_offset=angle_offset,
                          npts=line_pts)
        st.load(s,phase)
        jstring+=1
        i+=1
        i1=i2
        if (max_strings<=0) and (i1+1 >= sd.n()): break
        i2 = (i2+1) % sd.n()  # wrap around if necessary
        if (max_strings>0) and (jstring>=max_strings): break
            
    return st
