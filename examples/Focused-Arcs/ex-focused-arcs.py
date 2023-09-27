import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

F.set_default_dpi(150)

S = SpiroData()

###

N=600
S.reset()
S.add(cIc(Ring(50),Wheel(8.7,10),inside=True,ppl=N))

T=SpiroData()
for first in range(6):
    for offset in range(15):
        Q=SpiroData()
        Q.add(arcs_from_multi(S,array([int(offset*3+N/3)]),100,invert=True,line_pts=400,
                              max_strings=1,first=int(N/6*first*1.3),arc_only=False)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T,cmap='jet',color_scheme='time',save=True)

###


N=600
S.reset()
S.add(cIe(Ellipse(50,0.8,0,pi/4),Wheel(6.7,10),inside=True,ppl=N))

T=SpiroData()
np.random.seed(12)
for first in range(18):
    first_point = np.random.randint(0,N)
    for offset in range(8):
        offset_array = array([int(offset*4+N/3)])
        Q=SpiroData()
        Q.add(arcs_from_multi(S,offset_array,100,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,90,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,80,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T,cmap='jet',color_scheme='t-waves',save=True)

###

N=600
S.reset()
S.add(cIe(Ellipse(50,0.8,0,pi/4),Wheel(6.7,10),inside=False,ppl=N))

T=SpiroData()
np.random.seed(16)
for first in range(8):
    first_point = np.random.randint(0,N)
    for offset in range(9):
        offset_array = array([int(offset*4+N/3)])
        Q=SpiroData()
        Q.add(arcs_from_multi(S,offset_array,100,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,90,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,80,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T,cmap='ocean',color_scheme='length',save=True)

###


N=600
S.add(cIe(Ellipse(50,0.8,0,pi/4),Wheel(6.7,10),inside=False,ppl=N))

T=SpiroData()
np.random.seed(20)
for first in range(8):
    first_point = np.random.randint(0,N)
    for offset in range(30):
        offset_array = array([int(offset*4+N/2)])
        Q=SpiroData()
        Q.add(arcs_from_multi(S,offset_array,80,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,75,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,70,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T,cmap='Blues_r',color_scheme='time',save=True)

###

S=spiro_nstar(3,50,0.25,W0)
S=S.subsample(10)
N=S.n()

T=SpiroData()
np.random.seed(20)
for first in range(12):
    first_point = np.random.randint(0,N)
    for offset in range(7):
        offset_array = array([int(offset*4+N/2)])
        Q=SpiroData()
        Q.add(arcs_from_multi(S,offset_array,100,invert=False,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,80,invert=False,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,100,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,80,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T.rotate(pi/4),cmap='Wistia',color_scheme='t-waves',save=True)

###

S=spiro_nstar(4,50,.35,W0)
S=S.subsample(10)
N=S.n()
T=SpiroData()
np.random.seed(20)
for first in range(20):
    first_point = np.random.randint(0,N)
    for offset in range(10):
        offset_array = array([int(offset*4+0.4*N)])
        Q=SpiroData()
        Q.add(arcs_from_multi(S,offset_array,100,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,80,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T,cmap='Reds',color_scheme='t-waves',save=True)

###

S=cIc(Ring(30),Wheel(3,20),loops=1,ppl=720)
N=S.n()
T=SpiroData()
np.random.seed(21)

for first in range(12):
    first_point = np.random.randint(0,N)
    for offset in range(7):
        offset_array = array([int(offset+0.4*N)])
        Q=SpiroData()
        Q.add(arcs_from_multi(S,offset_array,100,invert=False,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,80,invert=False,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,100,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,80,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.plot(T,cmap='Reds_r',color_scheme='l-waves',save=True)

###

S=cIc(Ring(30),Wheel(3,20),loops=1,ppl=720)
N=S.n()

T=SpiroData()
np.random.seed(21)
for first in range(60):
    first_point = 73*first+34
    for offset in range(7):
        offset_array = array([int(offset+N/9)])
        Q=SpiroData()
        Q.add(arcs_from_multi(S,offset_array,100,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.add(arcs_from_multi(S,offset_array,60,invert=True,line_pts=400,
                              max_strings=1,first=first_point,arc_only=True)).move(0,0).rotate(0)
        Q.t=Q.x*0+first%5
        T.add(Q)

F.set_default_cmap(cmap_from_list(['red','darkgreen']))
F.plot(T,color_scheme='l-waves',save=True)
