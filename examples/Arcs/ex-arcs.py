import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from Ring import *

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",["seagreen","teal","cornflowerblue","mediumblue","indigo"])

###

F=SpiroFig()
F.text_color='white'

S = SpiroData()

S.add(eIe(Ellipse(15,0.7,0,pi/4),Ellipse(pi**2,0.4,10),loops=30,inside=True))

T=arcs_from_multi(S,array([1463]),7,invert=True,line_pts=300,max_strings=2000)
F.plot(T,color_scheme='t-waves',cmap='ocean',save=True)

##

T=arcs_from_multi(S,array([63,300,1000]),5,invert=True,line_pts=300,max_strings=3500)
F.plot(T,color_scheme='cycles',cmap='jet',save=True)

###

T = cIc(Ring(10),Wheel(4,3.5),loops=100,ppl=1283)
cs='t-waves'

offsets=[658]
F.plot(arcs_from_multi(T,offsets),
       cmap='Reds',color_scheme=cs,save=True)

##

offsets=[658,340,25]
F.plot(arcs_from_multi(T,offsets,30,invert=False,line_pts=500,max_strings=500),
       cmap=cmap3,color_scheme='cycles',save=True)

##

offsets=[3001]
Q=arcs_from_multi(T,offsets,30,invert=False,line_pts=500,max_strings=300)
Q.add(arcs_from_multi(T,offsets,30,invert=True,line_pts=500,max_strings=300))
F.plot(Q,cmap='turbo',color_scheme='length',save=True)

###

T = cIc(Ring(10),Wheel(4,3.5),loops=2,ppl=1283)

offsets=[301]
Q=arcs_from_multi(T,offsets,15,invert=True,line_pts=500,max_strings=300)
F.plot(Q,cmap='OrRd',color_scheme='t-waves',save=True)

###

T = cIc(Ring(8.5),Wheel(4,3.5),loops=8,ppl=300)
offsets=[43,79]
Q=arcs_from_multi(T,offsets,15,invert=True,line_pts=500,max_strings=300)
Q.add(arcs_from_multi(T,offsets,15,invert=False,line_pts=500,max_strings=300))
F.plot(Q,cmap='OrRd',color_scheme='length',save=True)

###

T = cIe(Ellipse(8.5,0.8,0,pi/5),Wheel(4,5.5),loops=3,ppl=300)
offsets=[43]
Q=arcs_from_multi(T,offsets,15,invert=True,line_pts=500,max_strings=300)
Q.add(arcs_from_multi(T,offsets,15,invert=False,line_pts=500,max_strings=300))
F.plot(Q,cmap='turbo',color_scheme='length',save=True)

###


T = cIe(Ellipse(11.5,0.8,0,-pi/5),Wheel(7,5.5),loops=3,ppl=300)
offsets=[43,86]
Q=arcs_from_multi(T,offsets,40,invert=True,line_pts=500,max_strings=300)
Q.add(arcs_from_multi(T,offsets,20,invert=False,line_pts=500,max_strings=300))
F.plot(Q,cmap='ocean',color_scheme='length',save=True)

###  (poster)

for t in [True,False]:
    
    F = SpiroFig(rows=3,cols=3)
    F.text_color='white'
    
    T = cIc(Ring(10),Wheel(4,3.5),loops=100,ppl=1283)
    
    F.plot(T,caption='Original')
    
    cs='t-waves'
    arc_radius=30
    
    F.caption(f'arc_radius={arc_radius}; invert={t}')
    
    offsets=[658]
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap='Reds',color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    offsets.append(340)
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap=cmap1,color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    offsets.append(25)
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap=cmap2,color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    offsets.append(174)
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap=cmap3,color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    offsets=[657,852]
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap='summer',color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    offsets=[658,340,25,174,1,5]
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap='autumn',color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    offsets=[657,880]
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap='jet',color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    offsets=[658,340,25,174,1,5,41,360]
    F.plot(arcs_from_multi(T,offsets,arc_radius,invert=t),
           cmap='terrain',color_scheme=cs,caption=f'{offsets}',new_fig=False)
    
    F.save_fig(f'arc-poster-{arc_radius}-{t}.png')
