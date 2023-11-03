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

hd = 0  # high-def

def_factor = (1+4*hd)

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions
data_set=0

###

ppl=1000
T = cIc(Ring(30),Wheel(5,8),loops=1,ppl=ppl,inside=True)
S = ellipses_on_frame(T,50,0.9,T.directions(),1000*def_factor)
if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,cmap='OrRd',color_scheme='cycles',alpha=0.4,save=True,fig_dim=fd)

###

ppl=3000
T = cIc(Ring(30),Wheel(5,8),loops=1,ppl=ppl,inside=True).subsample(1).inverted_radii().scale(1000)
S=ellipses_on_frame(T,50,0.9,T.directions(),1000*def_factor,n=ppl//5)
if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,cmap='ocean_r',color_scheme='phase',alpha=0.4,save=True,fig_dim=fd)

###

S=SpiroData()
ppl=3000
T = cIc(Ring(30),Wheel(5,8),loops=1,ppl=ppl,inside=False) # .subsample(1).inverted_radii().scale(1000)
for i in range(3):
    ne=ppl//5
    first=i*ppl//3
    orient=[ T.direction(j) for j in arange(first,first+ne) ]
    S.add(ellipses_on_frame(T,50,0.9,orient,500*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,cmap='Wistia_r',color_scheme='length',alpha=0.4,save=True,fig_dim=fd)

###

S=SpiroData()

ppl=3000
T = spiro_ngon(3,wheel=Wheel(10,8),loops=1,inside=True)
for i in range(1):
    ne=ppl//2
    first=i*ppl//3
    orient=[ T.direction(j) for j in arange(first,first+ne) ]
    eccen=0.9+0.1*sin(linspace(0,4*pi,ne))-0.001
    S.add(ellipses_on_frame(T,50,eccen,orient,500*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,cmap=cmap1,color_scheme='cycles',alpha=0.4,save=True,fig_dim=fd)

###

ppl=3000

S = SpiroData()
np.random.seed(966)
T = spiro_ngon(3,wheel=Wheel(10,8),loops=1,inside=True)
for i in range(6):
    ne=ppl//20+np.random.randint(100)
    first=np.random.randint(ppl)
    orient=[ T.direction(j) for j in arange(first,first+ne) ]
    eccen=0.9+0.0*sin(linspace(0,4*pi,ne))-0.001
    S.add(ellipses_on_frame(T,40,eccen,orient,500*def_factor,first=first,n=ne))


if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,color_scheme='t-waves',cmap='OrRd',alpha=0.4,save=True,fig_dim=fd)

###

S = SpiroData()
ppl=3000
seed = np.random.randint(1000)
np.random.seed(421)
T = spiro_line(wheel=Wheel(5,3),loops=1)
F.plot(T)
for i in range(1):
    ne=ppl//4
    first=np.random.randint(ppl)
    orient=[ T.direction(j) for j in arange(first,first+ne) ]
    eccen=0.8+0.0*sin(linspace(0,4*pi,ne))
    S.add(ellipses_on_frame(T,20,eccen,orient,500*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,color_scheme='time',cmap='jet',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()
np.random.seed(480)
T = spiro_nstar(6,wheel=Wheel(5,3),loops=1,fold=True).subsample(8)
ppl=T.n()
for i in range(1):
    ne=ppl//4
    first=np.random.randint(ppl)
    orient=[ T.direction(j) for j in arange(first,first+ne) ]
    eccen=0.8
    S.add(ellipses_on_frame(T,20,eccen,orient,500*def_factor,first=first,n=ne))


if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,color_scheme='l-waves',cmap='bone',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()
np.random.seed(402)
T = spiro_nstar(6,wheel=Wheel(5,3),loops=1,fold=True).subsample(8)
ppl=T.n()

for i in range(1):
    ne=ppl//3
    first=np.random.randint(ppl)
    orient=[ T.direction(j) for j in arange(first,first+ne) ]
    eccen=0.75+0.2*sin(linspace(0,4*pi,ne))
    S.add(ellipses_on_frame(T,20,eccen,orient,500*def_factor,first=first,n=ne))


if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
F.plot(S,color_scheme='l-waves',cmap='ocean',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()

T = spiro(Ring(30),wheel=Wheel(10,8),loops=1).subsample(2)
ppl=T.n()
ne=ppl-1
first=0
major =[ 2/sqrt(T.neighbor_dist(j)) for j in arange(first,first+ne) ]
orient=[ T.direction(j)+pi/2        for j in arange(first,first+ne) ]
eccen=0.75
S.add(ellipses_on_frame(T,major,eccen,orient,500*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme='cycles',cmap='OrRd',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()
T = spiro(Ring(30),wheel=Wheel(10,8),loops=1).subsample(2)
ppl=T.n()
ne=ppl-1
first=0 
major =[ 14/sqrt(T.neighbor_dist(j)) for j in arange(first,first+ne) ]
orient=[ T.direction(j)+pi/4         for j in arange(first,first+ne) ]
eccen=0.99
S.add(ellipses_on_frame(T,major,eccen,orient,1500*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme='length',cmap='copper',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()
T = spiro(Ring(30),wheel=Wheel(6,4),loops=1).subsample(2)
ppl=T.n()
ne=ppl-1
first=0 
major =[ 14/(T.neighbor_dist(j))**0.25 for j in arange(first,first+ne) ]
orient=[ T.direction(j)+pi/4         for j in arange(first,first+ne) ]
eccen=0.99
S.add(ellipses_on_frame(T,major,eccen,orient,1000*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme='length',cmap='turbo',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()
T = cIc(Ring(30),wheel=Wheel(6,4),loops=1).subsample(1)
ppl=T.n()
ne=ppl-1
first=0 
major =[ 14/(T.neighbor_dist(j))**0.25 for j in arange(first,first+ne) ]
orient=[ T.direction(j)+pi/4         for j in arange(first,first+ne) ]
eccen=0.99
S.add(ellipses_on_frame(T,major,eccen,orient,1000*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme='length',cmap='turbo',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()
T = cIc(Ring(30),wheel=Wheel(5,12),loops=1).subsample(1)
ppl=T.n()
F.plot(T)
ne=ppl-1
first=0 
major =[ 14/(T.neighbor_dist(j))**0.25 for j in arange(first,first+ne) ]
orient=[ T.direction(j)+pi/3           for j in arange(first,first+ne) ]
eccen=0.99
S.add(ellipses_on_frame(T,major,eccen,orient,1000,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1

F.plot(S,color_scheme='l-waves',cmap='tab20b',alpha=0.4,fig_dim=fd,save=True)

###

S = SpiroData()
T = cIc(Ring(30),wheel=Wheel(5,12),loops=1).subsample(1).inverted_radii().scale(500)
ppl=T.n()
F.plot(T,no_frame=False)
ne=ppl-1
first=0 
major =[ 14/(T.neighbor_dist(j))**0.25 for j in arange(first,first+ne) ]
orient=[ T.direction(j)+pi/3           for j in arange(first,first+ne) ]
eccen=0.99
S.add(ellipses_on_frame(T,major,eccen,orient,1000*def_factor,first=first,n=ne))

if hd:
    S.save(f'figure-{data_set}.pickle')
    data_set+=1
    
F.plot(S,color_scheme='cycles',cmap='copper',alpha=0.4,fig_dim=fd,save=True)
