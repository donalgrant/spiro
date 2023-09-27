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

###

Q1=centered_arcs(cIc(Ring(30),Wheel(5,10),inside=True,loops=1,ppl=300),
                 10,arc_subtended=pi/5,theta_phase=False,line_pts=200)
Q2=centered_arcs(cIc(Ring(30),Wheel(5,10),inside=False,loops=1,ppl=400),
                 10,arc_subtended=pi/3,theta_phase=False,line_pts=200)
Q3=centered_arcs(cIc(Ring(9),Wheel(1.5,0),inside=True,loops=1,ppl=200),
                 6,arc_subtended=pi/4,theta_phase=False,line_pts=200)
F.plot(Q1,cmap='Purples',color_scheme='time')
F.plot(Q2,cmap='Oranges',color_scheme='time',new_fig=False)
F.plot(Q3,cmap='Reds',color_scheme='time',new_fig=False)
F.save_fig()

###

Q2=centered_arcs(cIc(Ring(30),Wheel(5,10),inside=True,loops=10,ppl=300),
                 10,arc_subtended=pi/3,theta_phase=True,line_pts=200)
F.plot(Q2,cmap='Oranges',color_scheme='time',save=True)

###

S = cIc(Ring(30),Wheel(20,4),inside=True,loops=2,ppl=200)
Q=rotating_arcs(S,20,arc_subtended=pi/8,rotation_rate=8,arc_offset_angle=pi/2)
F.plot(Q,cmap='autumn',color_scheme='radial',save=True)



