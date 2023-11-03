import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_ellipses import *
from spiro_arcs import *
from spiro_string import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

hd = 0  # 1 for high-def

def_factor = (1+4*hd)

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions
data_set=0

###

# a=major_from_circum(2*pi*30,0.8)
T = cIc(Ring(30),wheel=Wheel(5,7),loops=1,inside=True,ppl=3000).subsample(5)
ppl=T.n()

seed=476 # np.random.randint(0,1000)
np.random.seed(seed)

cs = 'spacing'
c = 'OrRd'

S=SpiroData()
nstarts=5
nfigs=50
for si in range(nstarts):
    i2_start = np.random.randint(T.n()//(2*nstarts))+si*T.n()//nstarts
    S.add(ellipses_from_coord(T,array([0,0]),offset=1,npts=1000*def_factor,
                              off_major=linspace(1.0,0.9,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                              eccen=linspace(0.7,0.7,nfigs),nfigs=nfigs,i2_start=i2_start))
    
F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

##

cs = 't-waves'
c = 'Wistia'

seed = 59
np.random.seed(seed)

S=SpiroData()
nstarts=3
nfigs=30
for k in range(1):
    for si in range(nstarts):
        i2_start = np.random.randint(T.n()//(2*nstarts))+si*T.n()//nstarts
        S.add(ellipses_from_coord(T,array([0,0]),offset=4,npts=1000*def_factor,
                                  off_major=linspace(1.0,0.9,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.7,0.7,nfigs),nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

##

cs = 'y-direction'
c = 'turbo'

seed = 418
np.random.seed(seed)

S=SpiroData()
nstarts=5
nfigs=20
for k in range(1):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts
        S.add(ellipses_from_coord(T,array([0,si*5]),offset=1,npts=1000*def_factor,
                                  off_major=linspace(1.0,1.3,nfigs),off_minor=linspace(0.0,0.1,nfigs),
                                  eccen=linspace(0.75,0.6,nfigs),nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

###

T = cIc(Ring(30),wheel=Wheel(5,7),loops=1,inside=False,ppl=3000).subsample(1)

cs = 'y-direction'
c = cmap1

S=SpiroData()
nstarts=9
nfigs=30
for k in range(1):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,array([0,si*5]),offset=1,npts=1000*def_factor,
                                  off_major=linspace(1.0,1.3,nfigs),off_minor=linspace(0.0,0.1,nfigs),
                                  eccen=linspace(0.75,0.6,nfigs),nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

###

T = cIc(Ring(21),wheel=Wheel(7,7),loops=1,inside=True,ppl=3000).subsample(15)

cs = 'spacing'
c = 'ocean'

S=SpiroData()
nstarts=1
nfigs=15
nk=12
for k in range(nk):
    R=0
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts
        S.add(ellipses_from_coord(T,array([R*cos(2*k*pi/nk),R*sin(2*k*pi/nk)]),offset=1,npts=1000*def_factor,
                                  orient_offset=linspace(0,0,nfigs),
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.6,0.6,nfigs),nfigs=nfigs,i2_start=T.n()//nk*k))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

##

cs = 'spacing'
c = 'Greens'

S=SpiroData()
nstarts=1
nfigs=10
nk=40
for k in range(nk):
    R=15
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts # np.random.randint(T.n()//(2*nstarts))
        S.add(ellipses_from_coord(T,array([R*sin(2*k*pi/nk),R*cos(2*k*pi/nk)]),offset=1,npts=1000*def_factor,
                                  orient_offset=linspace(0,pi/4,nfigs),
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.9,0.9,nfigs),nfigs=nfigs,i2_start=T.n()//nk*k))

        
if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

###

T = cIc(Ring(21),wheel=Wheel(14,10),loops=2,inside=True,ppl=3000).subsample(15)

cs = 'time'
c = cmap1

S=SpiroData()
nstarts=T.n()
nfigs=1
nk=1
for k in range(nk):
    R=15
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts
        S.add(ellipses_from_coord(T,array([0,0]),offset=1,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.9,0.9,nfigs),nfigs=nfigs,i2_start=i2_start))
        
if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

##

T = cIc(Ring(21),wheel=Wheel(14,10),loops=2,inside=True,ppl=3000).subsample(15)

cs = 'l-waves'

clist = [ 'xkcd:'+i for i in ['sapphire','vibrant blue','carolina blue','navy blue','azul'] ]
c = cmap_from_list(clist)

S=SpiroData()
nstarts=T.n()
nfigs=1
nk=1
for k in range(nk):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts
        S.add(ellipses_from_coord(T,array([15,15]),offset=1,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.9,0.9,nfigs),nfigs=nfigs,i2_start=i2_start))
        
if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,save=True)

###

T = cIc(Ring(20),wheel=Wheel(4,8),loops=1,inside=True,ppl=3000).subsample(1)

cs = 'cycles'
my_cmap = 'OrRd'

S=SpiroData()
nstarts=T.n()//5
nfigs=1
nk=1
for k in range(nk):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,array([0,0]),offset=1,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=pi/8,
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.9,0.9,nfigs),nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,save=True)

###

T = cIc(Ring(24),wheel=Wheel(6,6),loops=1,inside=True,ppl=3000).subsample(1)

cs = 'spacing'
my_cmap = 'OrRd'

S=SpiroData()
nstarts=T.n()//40
nfigs=5
nk=1
for k in range(nk):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,array([0,0]),offset=2,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=0,
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.9,0.9,nfigs),nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,save=True)

##

cs = 'x-direction'
my_cmap = 'turbo'

S=SpiroData()
nstarts=T.n()//10
nfigs=1
nk=1

nc=32
var = [ pi/5*sin(nc*2*pi*i/T.n()) for i in range(T.n()) ]

for k in range(nk):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,array([0,0]),offset=2,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=var[si],
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.9,0.9,nfigs),nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,save=True)

###

T = cIc(Ring(28),wheel=Wheel(4,5),loops=1,inside=True,ppl=3000).subsample(1)

cs = 'spacing'
my_cmap = 'Greens'

S=SpiroData()
nstarts=T.n()//5
nfigs=1
nk=1

nc=3
var = [ pi/9*sin(nc*2*pi*i/T.n()) for i in range(T.n()) ]

for k in range(nk):
    for si in range(nstarts):
        i2_start = si*T.n()//nstarts 
        S.add(ellipses_from_coord(T,array([0,0]),offset=2,npts=1000*def_factor,
                                  scale_major=linspace(1.0,1.0,nfigs),
                                  orient_offset=pi/4,
                                  off_major=linspace(1.0,1.0,nfigs),off_minor=linspace(0.0,0.0,nfigs),
                                  eccen=linspace(0.9,0.9,nfigs),nfigs=nfigs,i2_start=i2_start))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,save=True)
