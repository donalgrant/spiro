from SpiroData import *
from SpiroGeometry import *
from numpy import array,linspace

def spiro_string(sd,subsample=100,line_pts=500):
    s = sd.subsample(subsample)
    st = SpiroData()
    for i in range(s.n()-1):
        cc = line(array([ [s.x[i],s.y[i]], [s.x[i+1],s.y[i+1]] ]),line_pts)
        sti = SpiroData()
        sti.x=cc[:,0]
        sti.y=cc[:,1]
        sti.t=linspace(0,sti.x.shape[0])
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

