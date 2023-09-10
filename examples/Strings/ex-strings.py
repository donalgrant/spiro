import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *

###

F=SpiroFig(rows=3,cols=3)
F.text_color='white'
T = spiro_arc(loops=50)
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
S = spiro(R=20,wheel=Wheel(1.7,17.8,0),loops=10,orient=0,inside=t,spacing=0.0005)
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
S = spiro(R=20,wheel=Wheel(8,12,0),loops=10,orient=0,inside=t,spacing=0.0005)
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
S = spiro(R=20,wheel=Wheel(8.2,5.8,0),loops=10,orient=0,inside=t,spacing=0.001)
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
S = spiro(R=20,wheel=Wheel(8.2,5.8,0),loops=10,orient=0,inside=t,spacing=0.001)
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
