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


###

ppl=100
e=0.3
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(12*r),Ellipse(8,e,36),inside=True,loops=3.5,ppl=ppl)
Q=arcs_on_frame(T,50,2*pi,T.neighbor_distances(),500,1,n=T.n()-1)
F.plot(Q,cmap='viridis',color_scheme='cycles',save=True)

###

Q=SpiroData()
ppl=200
e=0.3
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(12*r),Ellipse(8,e,36),inside=True,loops=3.5,ppl=ppl)
Q.add(arcs_on_frame(T,20*cos(T.t/25),pi,T.p+pi/2,500,1))
F.plot(Q,cmap='ocean',color_scheme='cycles',save=True)

###

Q=SpiroData()
ppl=200
e=0.8
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(12*r),Ellipse(8,e,36),inside=True,loops=3.5,ppl=ppl)
Q.add(arcs_on_frame(T,20*cos(T.p),T.p/10,T.t,1000,1))
F.plot(Q,cmap='autumn',color_scheme='cycles',save=True)

###

Q=SpiroData()
ppl=200
e=0.8
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(6*r),Ellipse(4,e,12),inside=True,loops=3.5,ppl=ppl)
U = eIc(Ring(14*r),Ellipse(8,e,4),inside=False,loops=3.5,ppl=ppl)
Q.add(arcs_on_frame(U,15,         pi,U.t,300,1))
Q.add(arcs_on_frame(T, 5*cos(T.p),2*pi,T.p,300,1))
F.plot(Q,cmap='Reds',color_scheme='cycles',save=True)

## (ad infinitum)

Q=arcs_on_frame(U.subsample(4),15,         pi/2,0,20,0)
W=arcs_on_frame(Q,Q.radii()/5,pi/4,Q.radii()/30,100,0)
F.plot(W,cmap='autumn',color_scheme='cycles',save=True)
