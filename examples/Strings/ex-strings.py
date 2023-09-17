import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from Ring import *

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",["seagreen","teal","cornflowerblue","mediumblue","indigo"])

###

F=SpiroFig(rows=3,cols=3)
F.text_color='white'
T = cIc(Ring(10),Wheel(4,3.5),loops=50,ppl=1283)
for cs in ['time']:
    F.plot(T,color_scheme='length',cmap='Reds',caption='Original Figure')
    for ss in [250,300,350,400,500,600,700,850]:
        F.plot(spiro_string(T,subsample=ss),color_scheme=cs,cmap='OrRd',
               new_fig=False,caption=f'Subsample {ss}')

F.save_fig('fig1.png')

###

F = SpiroFig(rows=5,cols=5)
F.text_color='white'
t=False
S = spiro(Ring(20),wheel=Wheel(1.7,17.8,0),loops=10,inside=t,ppl=2000)
F.plot(S,caption='Original',smooth=True,color_scheme='Blue',cmap='ocean')
for st in [20,40,80,160]:
    for s in [200,400,800,1600,3200,6400]:
        SO = string_offset_pairs(S,offset=s,step=st)
        F.plot(SO,caption=f'Offset {s} Step {st}',new_fig=False,color_scheme='length',cmap='ocean')

F.save_fig('fig2.png')

###

F = SpiroFig(rows=5,cols=5)
F.text_color='white'
t=True
S = spiro(Ring(20),wheel=Wheel(8,12,0),loops=10,inside=t,ppl=2000)
F.plot(S,caption='Original',smooth=True,color_scheme='red')
for st in [25,40,85,155]:
    for s in [150,200,300,400,600,955]:
        SO = string_offset_pairs(S,offset=s,step=st)
        F.plot(SO,caption=f'Offset {s} Step {st}',new_fig=False,color_scheme='t-waves',cmap='Reds')

F.save_fig('fig3.png')

###

F = SpiroFig(rows=3,cols=3)
F.text_color='white'
t=True
S = spiro(Ring(20),wheel=Wheel(8.2,5.8,0),loops=10,inside=t)
F.plot(S,caption='Original',smooth=True,color_scheme='tan')

for st in [25,40,85,155]:
    for s in [300,955]:
        SO = string_offset_pairs(S,offset=s,step=st)
        F.plot(SO,caption=f'Offset {s} Step {st}',new_fig=False,color_scheme='cycles',cmap='copper')

F.save_fig('fig4.png')

###

F = SpiroFig(rows=3,cols=3)

F.text_color='white'
t=True
fs=10
S = spiro(Ring(20),wheel=Wheel(8.2,5.8,0),loops=10,inside=t)
F.plot(S,caption='Original',smooth=False,color_scheme='length',cmap='jet',fontsize=fs)
s=15
st=55
cs='length'
c='jet'
s=93
F.plot(spiro_string(S,subsample=s),caption=f'Subsample {s}',                  
       new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)
s=213
st=33
F.plot(string_offset_pairs(S,offset=s,step=st),caption=f'Offset {s} Step {st}',
       new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)
s=60
st=15
F.plot(string_dispersing_pairs(S,offset=s,step=st,step2=2*st),
       caption=f'Disp Pairs: Off {s}, steps {st},{st*2}',
       new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)
s=80
st=10
st0=1
F.plot(string_dispersing_links(S,offset=s,step0=st0,step=st),
       caption=f'Disp Links: Off {s}, steps {st0},{st}',
       new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)
s=30
T=strings_from_coord(S,coord=array([0,3]),offset=s,nLines=50,i2_start=5)
T.add(strings_from_coord(S,coord=array([3,-2]),offset=s,nLines=50,i2_start=150))
T.add(strings_from_coord(S,coord=array([-2,1]),offset=s,nLines=50,i2_start=700))
F.plot(T,caption=f'from in Coords:  Off {s}',new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)

R=23
theta=2*pi/3
s=50
crd=array([ [R*cos(theta),R*sin(theta)],
            [R*1.3*cos(theta*2),R*sin(theta*2)],
            [R*cos(theta*2.6),R*1.5*sin(theta*2.6)] ])
T=strings_from_coord(S,coord=crd[0],offset=s,nLines=50,i2_start=5)
T.add(strings_from_coord(S,coord=crd[1],offset=s,nLines=50,i2_start=150))
T.add(strings_from_coord(S,coord=crd[2],offset=s,nLines=50,i2_start=700))
F.plot(T,caption=f'from out Coords:  Off {s}',new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)

n=3
s=31
F.plot(strings_from_pts(S,n,offset=s,fixed=400),
       caption=f'from {n} pts:  Off {s}',new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)

n=8
s=20
F.plot(strings_from_pts(S,n,offset=s,nLines=10),
       caption=f'from {n} pts:  Off {s}',new_fig=False,color_scheme=cs,cmap=c,fontsize=fs)

F.save_fig('fig5.png')

###

F = SpiroFig(rows=3,cols=3)
F.text_color='white'

T = cIc(Ring(10),Wheel(4,3.5),loops=100,ppl=1283)

F.plot(T,caption='Original')

cs='t-waves'

offsets=[658]
F.plot(strings_from_multi(T,offsets),cmap='Reds',color_scheme=cs,caption=f'{offsets}',new_fig=False)

offsets.append(340)
F.plot(strings_from_multi(T,offsets),cmap=cmap1,color_scheme=cs,caption=f'{offsets}',new_fig=False)

offsets.append(25)
F.plot(strings_from_multi(T,offsets),cmap=cmap2,color_scheme=cs,caption=f'{offsets}',new_fig=False)

offsets.append(174)
F.plot(strings_from_multi(T,offsets),cmap=cmap3,color_scheme=cs,caption=f'{offsets}',new_fig=False)

offsets=[657,852]
F.plot(strings_from_multi(T,offsets),cmap='summer',color_scheme=cs,caption=f'{offsets}',new_fig=False)

offsets=[658,340,25,174,1,5]
F.plot(strings_from_multi(T,offsets),cmap='autumn',color_scheme=cs,caption=f'{offsets}',new_fig=False)

offsets=[657,880]
F.plot(strings_from_multi(T,offsets),cmap='jet',color_scheme=cs,caption=f'{offsets}',new_fig=False)

offsets=[658,340,25,174,1,5,41,360]
F.plot(strings_from_multi(T,offsets),cmap='terrain',color_scheme=cs,caption=f'{offsets}',new_fig=False)

F.save_fig('fig6.png')
