import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from polygon import *

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",["seagreen","teal","cornflowerblue","mediumblue","indigo"])

S = SpiroData()
F = SpiroFig()

###

F.plot(spiro_nstar(6,r2=0.6,wheel=Wheel(3,3),
                   loops=10,fold=False,inside=True),
       color_scheme='time',cmap='Purples')
F.plot(spiro_nstar(6,r2=0.6,wheel=Wheel(5,4),
                   loops=10,inside=False,fold=False),
       color_scheme='time',cmap='autumn',new_fig=False)

F.save_fig()

###

F.plot(spiro_nstar(12,r2=0.5,wheel=Wheel(3.6,3),
                   loops=10,fold=False,inside=True),
       color_scheme='time',cmap='Purples')
F.plot(spiro_nstar(6,r2=0.5,wheel=Wheel(7,6),
                   loops=20,inside=False,fold=False,orient=pi/6),
       color_scheme='time',cmap='autumn',new_fig=False)

F.save_fig()

###

F.plot(spiro_nstar(4,r2=0.3,wheel=Wheel(3.2,3),
                   loops=10,fold=True,inside=True),
       color_scheme='time',cmap='Purples')
F.plot(spiro_nstar(8,r2=0.6,wheel=Wheel(5,4),
                   loops=10,inside=False,fold=False),
       color_scheme='time',cmap='autumn',new_fig=False)

F.save_fig()

### Stellar Evolution Poster

S=SpiroData()
G = SpiroFig(rows=4,cols=3)
G.text_color='white'

G.plot(spiro_nstar(4,wheel=W0),caption='Star Frame')

S.reset()
for i in range(20):
    S.add(spiro_nstar(4,wheel=W0).rotate(pi/40*i))
G.plot(S,caption='... with rotations',new_fig=False)

S.reset()
for i in range(20):
    S.add(spiro_nstar(4,wheel=W0).rotate(pi/40*i).move(i/4,-i/3))
G.plot(S,caption='... and translations',new_fig=False)

G.plot(spiro_nstar(4,wheel=Wheel(5,5),loops=2),caption='two loops',new_fig=False)

S.reset()
for i in range(20):
    S.add(spiro_nstar(4,wheel=Wheel(5,5),loops=2).rotate(pi/40*i))
G.plot(S,caption='... with rotations',new_fig=False)

S.reset()
for i in range(20):
    S.add(spiro_nstar(4,wheel=Wheel(5,5),loops=2).rotate(pi/40*i).move(i/4,-i/3))
G.plot(S,caption='... and translations',new_fig=False)

G.plot(spiro_nstar(4,wheel=Wheel(5-i/30,5+i/10),loops=2),caption='alter radius and pen',new_fig=False)

S.reset()
for i in range(20):
    S.add(spiro_nstar(4,wheel=Wheel(5-i/30,5+i/10),loops=2).rotate(pi/40*i))
G.plot(S,caption='... with rotations',new_fig=False)

S.reset()
for i in range(20):
    S.add(spiro_nstar(4,wheel=Wheel(5-i/30,5+i/10),loops=2).rotate(pi/40*i).move(i/4,-i/3))
G.plot(S,caption='... and translations',new_fig=False)
    
### colors

G.plot(S,caption='t-waves/RedOrangePink',color_scheme='t-waves',cmap=cmap1,new_fig=False)
G.plot(S,caption='t-waves/ocean',color_scheme='t-waves',cmap='ocean',new_fig=False)
G.plot(S,caption='t-waves/jet',color_scheme='t-waves',cmap='jet',new_fig=False)

G.caption('Stellar Evolution')

G.save_fig('Stellar-Evolution.png')

F.plot(S,color_scheme='t-waves',cmap='ocean',save=True)

###

t=True
n=4
l=3
np=10
S.reset()
for i in range(np):
    S.add(spiro_nstar(n,wheel=Wheel(5-i/30,5+i/10),
                      loops=l,inside=t).rotate(pi/40*i).move(i/4,-i/3))
F.plot(S,cmap='ocean',color_scheme='length',save=True)

###

t=True
n=3
l=3
np=10
S.reset()
for i in range(np):
    S.add(spiro_nstar(n,wheel=Wheel(5-i/30,5+i/10),
                      loops=l,inside=t).rotate(pi/40*i).move(i/4,-i/3))
F.plot(S,cmap=cmap1,color_scheme='radial',save=True)

###


S.reset()

t=True
n=3
l=2
np=15
r2=0.25
r1=40

for i in range(np):
    S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(5-i/30,5+i/10),loops=l,inside=t).rotate(pi/40*i).move(i/4,-i/3))
F.plot(S,cmap='Reds',color_scheme='length',save=True)

###


S.reset()
t=True
n=6
l=3
np=10
r2=0.5
r1=40
for i in range(np):
    S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(5-i/30,5+i/10),loops=l,inside=t).rotate(pi/40*i).move(i/4,-i/3))

F.plot(S,cmap=cmap2,color_scheme='t-waves',save=True)

###

S.reset()

t=True
n=5
l=3
np=8
r2=0.5
r1=25
ir=-1
a=5
m=5
dx=0
dy=0

for i in range(np):
    S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                      loops=l,inside=True).rotate(ir*pi/40*i).move(i*dx,i*dy))
    S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                      loops=l,inside=False).rotate(ir*pi/40*i).move(i*dx,i*dy))

F.plot(S,cmap='ocean',color_scheme='cycles',save=True)

###

S.reset()
inside=True
outside=False
n=5
l=18
np=5
r2=0.5
r1=25
ir=-1
a=7
m=5
dx=0
dy=0

for i in range(np):
    if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                                   loops=l,inside=True).rotate(ir*pi/40*i).move(i*dx,i*dy))
    if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                                   loops=l,inside=False).rotate(ir*pi/40*i).move(i*dx,i*dy))

F.plot(S,cmap='ocean',color_scheme='radial',save=True)

###

S.reset()

inside=True
outside=False
n=6
l=18
np=5
r2=0.6
r1=25
ir=-1
a=8
m=5
dx=0
dy=0

for i in range(np):
    if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                                   loops=l,inside=True).rotate(ir*pi/40*i).move(i*dx,i*dy))
    if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                                   loops=l,inside=False).rotate(ir*pi/40*i).move(i*dx,i*dy))
F.plot(S,cmap='jet',color_scheme='cycles',save=True)

###

S.reset()

inside=True
outside=False
n=6
l=18
np=3
r2=0.6
r1=25
ir=-1
a=6
m=4
dx=0
dy=0

for i in range(np):
    if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10), fold=True,
                                   loops=l,inside=True).rotate(ir*pi/40*i).move(i*dx,i*dy))
    if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                                   loops=l,inside=False).rotate(ir*pi/40*i).move(i*dx,i*dy))
F.plot(S,cmap='Reds',color_scheme='cycles',save=True)
