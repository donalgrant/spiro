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

ppl=200
e=0.5
wheel_r=5
eps=0.5
rf=4
r=major_from_circum(2*pi*wheel_r*rf,e)
T = cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*0.8),inside=True,loops=1.0,ppl=ppl).rotate(pi/4)

S=SpiroData()
cs = 't-waves'
c = 'Reds_r'
o = 6
r=60
seed = np.random.randint(0,1000)
np.random.seed(seed)
for i in range(8):
    theta = np.random.uniform(2*pi)
    r = np.random.uniform(10,20)
    x = r*cos(theta)
    y = r*sin(theta)
    for r in [60]:
        S.add(arcs_from_coord(T,[x,y],arc_radius=r,invert=True,offset=o))
        
F.plot(S,cmap=c,color_scheme=cs,caption=f'{c}/{cs} ({seed})',save=True)

##

S=SpiroData()
cs = 'time'
c = 'autumn_r'
o = 20
r=60
seed = np.random.randint(0,1000)
np.random.seed(seed)
for i in range(8):
    theta = np.random.uniform(2*pi)
    r = np.random.uniform(10,20)
    x = r*cos(theta)
    y = r*sin(theta)
    for r in [30,40,90]:
        S.add(arcs_from_coord(T,[x,y],arc_radius=r,invert=True,offset=o))
        
F.plot(S,cmap=c,color_scheme=cs,caption=f'{c}/{cs} ({seed})',save=True)

###

ppl=1000
e=0.5
wheel_r=5
eps=0.5
rf=4
r=major_from_circum(2*pi*wheel_r*rf,e)
T = cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*0.8),inside=True,loops=1.0,ppl=ppl).rotate(pi/4)

S=SpiroData()
cs = 'time'
c = 'autumn_r'
o = 8
r=60
seed = 571
np.random.seed(seed)
for i in range(1):
    S.add(arcs_from_pts(T,20,arc_radius=linspace(50,90,4),invert=True,offset=o,nLines=10))
        
F.plot(S,cmap=c,color_scheme=cs,save=True)

##

o = 20
r=60
S=SpiroData()
seed=856
np.random.seed(seed)
S.add(arcs_from_pts(T,100,arc_radius=linspace(50,90,8),invert=True,offset=o,nLines=1))

F.plot(S,cmap='turbo',color_scheme='time',save=True)

##

cs = 'time'
c = cmap1
o = 31
r=60
S=SpiroData()
seed = 591
np.random.seed(seed)
S.add(arcs_from_pts(T,2,arc_radius=linspace(50,90,8),invert=True,offset=o,nLines=30))

F.plot(S,cmap=cmap1,color_scheme='time',save=True)

###

ppl=1000
e=0.5
wheel_r=5
eps=0.5
rf=4
r=major_from_circum(2*pi*wheel_r*rf,e)
T = spiro_string(cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*0.8),inside=True,
                     loops=10.0,ppl=ppl).rotate(pi/4).subsample(377),line_pts=30)
S=SpiroData()
cs = 'time'
c = 'jet'
o = 3
r=10
seed = 969
np.random.seed(seed)
S.add(arcs_from_pts(T,20,arc_radius=linspace(50,90,4),invert=True,offset=o,nLines=5))

F.plot(S,cmap='jet',color_scheme='time',save=True)

###

ppl=1000
e=0.5
wheel_r=5
eps=0.5
rf=4
r=major_from_circum(2*pi*wheel_r*rf,e)
T = spiro_string(cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*0.8),inside=False,
                     loops=1.0,ppl=ppl).rotate(pi/4).subsample(71),line_pts=30)
cs = 'time'
c = 'ocean'
o = 3
S=SpiroData()
seed = 464
np.random.seed(seed)
S.add(arcs_from_pts(T,20,arc_radius=linspace(40,100,3),invert=True,offset=o,nLines=5))
        
F.plot(S,cmap=c,color_scheme=cs,save=True)

###

ppl=100
wheel_r=13
T = cIc(Ring(30),Wheel(wheel_r,wheel_r),inside=True,
                     loops=11.0,ppl=ppl).rotate(pi/4)
S=SpiroData()
cs = 'time'
c = 'OrRd'
arc_radius = [25 + i**2 for i in range(5)]
seed = 837
np.random.seed(seed)
for i in range(20):
    j = np.random.randint(0,T.n())
    i2 = j + np.random.randint(6,15)
    S.add(arcs_from_coord(T,T.xy(j),arc_radius=arc_radius,invert=True,
                          offset=np.random.randint(3,7),i2_start=i2,nLines=2))
        
F.plot(S,cmap=c,color_scheme=cs,save=True)

##

cs = 'length'
c = 'turbo'
arc_radius = [25 + i**2 for i in range(3)]
seed = 564
S=SpiroData()
Q=SpiroData()
np.random.seed(seed)
for i in range(20):
    j = np.random.randint(0,T.n())
    i2 = j + np.random.randint(6,15)
    U=arcs_from_coord(T,T.xy(j),arc_radius=arc_radius,invert=True,npts=600,
                      offset=np.random.randint(3,7),i2_start=i2,nLines=4)
    Q.add(U)
    S.add(ribbon(U.subsample(3),2,arc_subtended=pi/16,pts=10,trim=True))
        
F.plot(S,cmap=c,color_scheme=cs,caption=f'{c}/{cs} ({seed})',alpha=0.1)
F.plot(Q,cmap=c,color_scheme=cs,new_fig=False)
F.save_fig()
