from SpiroData import *
from SpiroGeometry import *
from numpy import array,linspace,fmod

def spiro_string(sd,line_pts=500):
    return strings_from_multi(sd,[1],line_pts=line_pts)

def string_offset_pairs(sd,offset=1000,step=50,line_pts=500,object=0):
    st = SpiroData()
    for i in range(0,sd.n()-offset,step):
        st.load(line(array([ [sd.x[i],sd.y[i]], [sd.x[i+offset],sd.y[i+offset]] ]),line_pts),
                sd.p[i],object=array_val(object,i),segment=i,
                frame_x=sd.x[i],frame_y=sd.y[i])
        
    return st

def string_dispersing_pairs(sd,offset=1000,step=50,step2=100,line_pts=500,object=0):
    st = SpiroData()
    i1=0
    i2=i1+offset
    while i2<sd.n():
        st.load(line(array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ]),line_pts),
                sd.p[i1],object=array_val(object,i1//step),segment=i1//step,
                frame_x=sd.x[i1],frame_y=sd.y[i1])
        i1+=step
        i2+=step2
        
    return st

def string_dispersing_links(sd,offset=1000,step0=50,step=1,line_pts=500,object=0):
    st = SpiroData()
    i1=0
    i2=i1+offset
    ip=step0
    while i2<sd.n():
        st.load(line(array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ]),line_pts),
                sd.p[i1],object=array_val(object,ip//step),segment=ip//step,
                frame_x=sd.x[i1],frame_y=sd.y[i1])
        i1=i2
        ip+=step
        i2=i1+offset
        
    return st

def strings_from_coord(sd,coord=array([0,0]),offset=100,line_pts=500,nLines=0,i2_start=-1,object=0):
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
        st.load(line(array([ [x0,y0], [sd.x[i2],sd.y[i2]] ]),line_pts),
                sd.p[i2],object=array_val(object,i),segment=i,
                frame_x=x0,frame_y=y0)
        
    return st

def closed_paths(sd,offsets,skip=1,first=0,n=0,line_pts=500,object=0):
    st = SpiroData()
    if n==0:  n = sd.n()//3  # number of closed paths to do
    i1=first % sd.n()        # offset to first closed path starting point
    seg_count=0
    j=0                      # counter for number of closed paths
    while True:
        i0=i1
        for o in offsets:
            st.load(line(array([ sd.xy(i1), sd.xy(i1+o) ]),line_pts),
                    sd.p[i1%sd.n()], object=array_val(object,j), segment=seg_count,
                    frame_x=sd.xy(i1)[0],frame_y=sd.xy(i1)[1])
            seg_count+=1
            i1 += o

        # now close the loop
        st.load(line(array([ sd.xy(i1),sd.xy(i0) ]),line_pts),
                sd.p[i1%sd.n()], object=array_val(object,j), segment=seg_count,
                frame_x=sd.xy(i1)[0],frame_y=sd.xy(i1)[1])
        seg_count+=1
        j+=1
        
        if (n<=0) and (i0+skip)>=sd.n(): break
        i1 = (i0 + skip) % sd.n()
        if (n>0)  and (j>=n): break

    return st

def strings_from_pts(sd,n=3,offset=100,line_pts=500,nLines=30,fixed=0):
    st = SpiroData()
    for i in range(n):
        j = np.random.random_integers(0,sd.n())
        i2_start=-1 if fixed==0 else j+fixed
        st.add(strings_from_coord(sd,array([ sd.x[j], sd.y[j] ]),
                                  offset,line_pts,nLines,i2_start=i2_start,object=i))
        
    return st

def strings_from_multi(sd,offset_array,line_pts=500,max_strings=0,first=0,object=0):
    st = SpiroData()
    n=len(offset_array)
    i=0
    i1=first % sd.n()
    i2=(i1+offset_array[0]) % sd.n()
    jstring=0
    while True:
        st.load(line(array([ [sd.x[i1],sd.y[i1]], [sd.x[i2],sd.y[i2]] ]),line_pts),
                sd.p[i1], object=array_val(object,jstring), segment=jstring,
                frame_x=sd.x[i1],frame_y=sd.y[i1])
        jstring+=1
        i+=1
        i1=i2
        if (max_strings<=0) and (i1+offset_array[i%n])>=sd.n(): break
        i2 = (i2+offset_array[i%n]) % sd.n()  # wrap around if necessary
        if (max_strings>0) and (jstring>=max_strings): break
            
    return st

