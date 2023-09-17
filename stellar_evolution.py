from SpiroData import *
from SpiroDraw import *
from spiro import *
from Wheel import *
from Ring import *
from polygon import *
from numpy import linspace,pi

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",["seagreen","teal","cornflowerblue","mediumblue","indigo"])

S=SpiroData()
F = SpiroFig(rows=4,cols=3)
F.text_color='black'

inside=False
outside=True
n=6
l=18
np=3
r2=0.6
r1=25
ir=-5
a=4
m=4
dx=2
dy=0

F.plot(spiro_nstar(n,r1=r1,r2=r2,wheel=W0,inside=t),caption='Star Frame')

S.reset()
for i in range(np):
    S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=W0,inside=t).rotate(ir*pi/40*i))
F.plot(S,caption='... with rotations',new_fig=False)

S.reset()
for i in range(np):
    S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=W0,inside=t).rotate(ir*pi/40*i).move(i*dx,i*dy))
F.plot(S,caption='... and translations',new_fig=False)

S.reset()
if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a,m),loops=l,inside=True))
if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a,m),loops=l,inside=False))
F.plot(S,caption=f'{l} loops',new_fig=False)

S.reset()
for i in range(np):
    if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a,m),loops=l,inside=True).rotate(ir*pi/40*i))
    if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a,m),loops=l,inside=False).rotate(ir*pi/40*i))
F.plot(S,caption='... with rotations',new_fig=False)

S.reset()
for i in range(np):
    if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a,m),loops=l,inside=True).rotate(ir*pi/40*i).move(i*dx,i*dy))
    if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a,m),loops=l,inside=False).rotate(ir*pi/40*i).move(i*dx,i*dy))
F.plot(S,caption='... and translations',new_fig=False)

S.reset()
if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),loops=l,inside=True))
if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),loops=l,inside=False))
F.plot(S,caption='alter radius and pen',new_fig=False)

S.reset()
for i in range(np):
    if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),loops=l,inside=True).rotate(ir*pi/40*i))
    if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),loops=l,inside=False).rotate(ir*pi/40*i))
F.plot(S,caption='... with rotations',new_fig=False)

S.reset()
for i in range(np):
    if inside:   S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10), 
                                   loops=l,inside=True).rotate(ir*pi/40*i).move(i*dx,i*dy))
    if outside:  S.add(spiro_nstar(n,r1=r1,r2=r2,wheel=Wheel(a-i/30,m+i/10),
                                   loops=l,inside=False).rotate(ir*pi/40*i).move(i*dx,i*dy))
F.plot(S,caption='... and translations',new_fig=False)
    
### colors

F.plot(S,caption='t-waves/RedOrangePink',color_scheme='t-waves',cmap=cmap1,new_fig=False)
F.plot(S,caption='t-waves/ocean',color_scheme='t-waves',cmap='ocean',new_fig=False)
F.plot(S,caption='t-waves/jet',color_scheme='t-waves',cmap='jet',new_fig=False)

F.caption('Stellar Evolution')

F = SpiroFig()
F.text_color='black'
for c in ['jet','ocean','Reds']:  # [cmap1,cmap2,cmap3,'summer','autumn','jet','terrain','Reds','ocean']:
    for cs in ['time','t-waves','length','l-waves','cycles','radial','s-ripples']:
        F.plot(S,color_scheme=cs,cmap=c,save=False,caption=f'{cs}/{c}',
               new_fig=True) # if c==cmap1 else False)
