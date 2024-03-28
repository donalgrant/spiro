import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from spiro_arcs import *
from spiro_string import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

hd = 0  # 1 for high-def

def_factor = (1+4*hd)
save=True

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions
data_set=0

###

e=0.4
a=major_from_circum(2*pi*4,e)*7
T = cIe(Ellipse(a,e,0,pi/4),wheel=Wheel(4,18),loops=1,inside=True,ppl=1000).subsample(1)

cs = 'spacing'

S=SpiroData()
nstarts=5
nfigs=15

pts = array([ [45,0], [0,45], [-45,-45] ])

for k in range(pts.shape[0]):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,pts[k],offset=2,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(1.0,1.0,nfigs),
                                  off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=0.9,
                                  nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap='pretty_blues',alpha=0.4,fig_dim=fd,save=save)

###

T = cIe(Ellipse(a,e,0,pi/4),wheel=Wheel(4,18),loops=1,inside=False,ppl=1000).subsample(1)

cs = 'spacing'
my_cmap = 'Oranges'

S=SpiroData()
nstarts=8
nfigs=25

pts = array([ [5,0], [0,5], [-5,-5], [0,20] ])

for k in range(pts.shape[0]):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,pts[k],offset=1,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(1.0,1.0,nfigs),
                                  off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=0.9,
                                  nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

###

T = cIe(Ellipse(a,e,0,pi/4),wheel=Wheel(4,18),loops=1,inside=False,ppl=1000).subsample(1)

cs = 'length'
my_cmap = 'autumn'

S=SpiroData()
nstarts=6
nfigs=20

pts = array([ [-20,0], [50,0], [15,35], [15,-35] ])

for k in range(pts.shape[0]):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,pts[k],offset=2,npts=1000*def_factor,
                                  scale_major=linspace(0.4,0.6,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(0.6,0.9,nfigs),
                                  off_minor=linspace(0.3,0.3,nfigs),
                                  eccen=0.9,
                                  nfigs=nfigs,i2_start=i2_start))


if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

###

T = cIe(Ellipse(a,e,0,pi/4),wheel=Wheel(4,12),loops=1,inside=True,ppl=1000).subsample(1)

cs = 'cycles'
my_cmap = 'autumn'

S=SpiroData()
nstarts=1
offset=4
nfigs=T.n()//offset

pts = array([ [30,0], [0,15], [0,-15] ])

for k in range(pts.shape[0]):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,pts[k],offset=offset,npts=1000*def_factor,
                                  scale_major=linspace(0.5+k/10,1.0+k/5,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(0.6,0.9,nfigs),
                                  off_minor=linspace(0.6,0.6,nfigs),
                                  eccen=0.9,
                                  nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

###
e=0.4
a=major_from_circum(2*pi*4,e)*3
T = cIe(Ellipse(a,e,0,pi/4),wheel=Wheel(4,12),loops=1,inside=True,ppl=1000).subsample(1)

cs = 'cycles'
my_cmap = 'autumn'

S=SpiroData()
nstarts=1 # T.n()//20
offset=4
nfigs=T.n()//offset

pts = array([ [-10,3], [2,-10], [8,8] ])

for k in range(pts.shape[0]):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,pts[k],offset=offset,npts=1000*def_factor,
                                  scale_major=linspace(0.5,1.0,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(0.6,0.9,nfigs),
                                  off_minor=linspace(0.6,0.6,nfigs),
                                  eccen=0.9, # var[si],
                                  nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

###  Start pinning *on* the frame

e=0.4
a=major_from_circum(2*pi*4,e)*5
T = cIe(Ellipse(a,e,0,pi/4),wheel=Wheel(4,4),loops=1,inside=True,ppl=1000).subsample(1)

cs = 'x-direction'
my_cmap = 'OrRd'

S=SpiroData()

nPoints=1
offset=2
nfigs=T.n()//offset//2

np.random.seed(1)

S.add(ellipses_from_pts(T,nPoints,offset=offset,npts=1000*def_factor,
                        scale_major=linspace(0.3,0.7,3),
                        orient_offset=linspace(0,pi/4,1),
                        off_major=linspace(0.8,1.2,nfigs),
                        off_minor=0.5,
                        eccen=0.95,
                        nfigs=nfigs,
                        fixed=0
                       ))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

##

cs = 'time'
my_cmap = 'hsv'

S=SpiroData()

nPoints=1
offset=1
nfigs=T.n()//offset//2

np.random.seed(581)

S.add(ellipses_from_pts(T,nPoints,offset=offset,npts=1000*def_factor,
                        scale_major=linspace(0.3,0.7,3),
                        orient_offset=linspace(0,pi/4,1),
                        off_major=linspace(0.8,1.2,nfigs),
                        off_minor=0.5,
                        eccen=0.95,
                        nfigs=nfigs,
                        fixed=0
                       ))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

###

e=0.4
a=major_from_circum(2*pi*4,e)*5
T = cIe(Ellipse(a,e,0,pi/4),wheel=Wheel(4,4),loops=1,inside=True,ppl=2000)

cs = 'y-direction'
my_cmap = cmap1

S=SpiroData()

nPoints=1
offset=1
nfigs=T.n()//offset//3

np.random.seed(829)

S.add(ellipses_from_pts(T,nPoints,offset=offset,npts=1000*def_factor,
                        scale_major=linspace(0.3,0.7,7),
                        orient_offset=linspace(0,pi/4,1),
                        off_major=linspace(0.8,1.2,nfigs),
                        off_minor=0.5,
                        eccen=0.95,
                        nfigs=nfigs,
                        fixed=T.n()//2
                       ))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

##

cs = 'cycles'
my_cmap = 'autumn'

S=SpiroData()

nPoints=2
offset=2
nfigs=T.n()//offset//3

seed = np.random.randint(1000)
np.random.seed(444)
print(seed)

S.add(ellipses_from_pts(T,nPoints,offset=offset,npts=1000*def_factor,
                        scale_major=linspace(0.8,0.7,1),
                        orient_offset=linspace(0,pi/4,1),
                        off_major=linspace(0.8,1.2,nfigs),
                        off_minor=0.5,
                        eccen=0.95,
                        nfigs=nfigs,
                        fixed=T.n()//2
                       ))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)

##

cs = 'spacing'
my_cmap = 'autumn'

S=SpiroData()

nPoints=2
offset=1
nfigs=T.n()//(offset*nPoints*3)

np.random.seed(761)

S.add(ellipses_from_pts(T,nPoints,offset=offset,npts=1000*def_factor,
                        scale_major=linspace(0.5,0.7,1),
                        orient_offset=linspace(0,pi/4,2),
                        off_major=linspace(0.8,1.2,nfigs),
                        off_minor=0.5,
                        eccen=0.95,
                        nfigs=nfigs,
                        fixed=0
                       ))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,save=save)
