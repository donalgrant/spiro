import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from spiro_string import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

F.set_default_dpi(150)

###

ppl=100
wheel_r=13
T = cIc(Ring(30),Wheel(wheel_r,wheel_r),inside=True,
                     loops=11.0,ppl=ppl).rotate(pi/4)
cs = 'length'
c = 'turbo'
arc_radius = [25 + i**2 for i in range(3)]

S=SpiroData()
Q=SpiroData()
seed = 331
np.random.seed(seed)
for i in range(20):
    j = np.random.randint(0,T.n())
    i2 = j + np.random.randint(6,15)
    U=arcs_from_coord(T,T.xy(j),arc_radius=arc_radius,invert=True,npts=600,
                      offset=np.random.randint(3,7),i2_start=i2,nLines=4)
    Q.add(U)
    S.add(connected_bubbles(U.subsample(30)))
    
F.plot(Q,cmap=c,color_scheme=cs,caption=f'{c}/{cs} ({seed})',alpha=0.1)
F.plot(S,cmap=c,color_scheme=cs,new_fig=False,alpha=0.2)

F.save_fig()

###

ppl=1283
ss=850
T = spiro_string(cIc(Ring(10),Wheel(4,3.5),loops=50,ppl=ppl).subsample(ss))
cs = 'length'
c = 'Reds'
S=SpiroData()
Q=SpiroData()
U=T.subsample(2)
Q.add(U)
S.add(connected_bubbles(U.subsample(30)))
        
F.plot(Q,cmap=c,color_scheme=cs,caption=f'{c}/{cs} ({seed})',alpha=0.3)
F.plot(S,cmap=c,color_scheme=cs,new_fig=False,alpha=0.2)

F.save_fig()

##

cs = 'length'
c = 'jet'
S=SpiroData()
Q=SpiroData()
U=T.subsample(1).rotate(pi)
Q.add(U)
S.add(connected_bubbles(U.subsample(97)))
        
F.plot(Q,cmap=c,color_scheme=cs,caption=f'{c}/{cs} ({seed})',alpha=0.3)
F.plot(S,cmap=c,color_scheme=cs,new_fig=False,alpha=0.4)

F.save_fig()

###

cs = 'l-waves'
c = 'OrRd'
S=SpiroData()
Q=SpiroData()
ppl=1000
for i in range(4):
    T=cIe(Ellipse(30,0.6),Wheel(8,8.5),loops=3.5,inside=True,ppl=ppl).rotate(pi/16*i).move(5,3)
    Q.add(T)
    for ss in [5,13,26]:
        S.add(connected_bubbles(T.subsample(ss)))
        
F.plot(Q,cmap=c,color_scheme=cs,alpha=0.3)
F.plot(S,cmap=c,color_scheme=cs,new_fig=False,alpha=0.2)

F.save_fig()
