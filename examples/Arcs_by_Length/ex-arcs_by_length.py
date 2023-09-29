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

ppl=300
c=circum(4,0.3)/(2*pi)
T = eIc(Ring(2*c),Ellipse(4,0.3,7),inside=False,loops=3.015,ppl=ppl)
Q=arcs_on_frame(T,(T.radii()**2)/16,pi/4,T.directions()-pi/2,300,0,n=T.n()-1)
F.plot(Q,cmap='autumn',color_scheme='x+y',save=True)

##

Q=arcs_on_frame(T,1000/T.radii(),pi/40,T.directions()-pi/4,300,0,n=T.n()-1)
F.plot(Q,cmap='tab20b',color_scheme='length',save=True)

###

ppl=200
e=0.7
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(4*r),Ellipse(4,e,7),inside=True,loops=3.5,ppl=ppl)
Q=arcs_on_frame(T,1000/T.radii(),pi/40,T.directions()-pi/8,300,0,n=T.n()-1)
F.plot(Q,cmap='RdBu',color_scheme='cycles',save=True)

##

Q=arcs_on_frame(T,100*sin(2*pi*T.radii()/5),pi/4,T.directions(),300,0,n=T.n()-1)
F.plot(Q,cmap='RdBu',color_scheme='cycles',save=True)

###

ppl=500
e=0.3
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(12*r),Ellipse(8,e,36),inside=True,loops=3.5,ppl=ppl)
Q = arcs_on_frame(T,max(T.y/2)+T.y/2,pi/6,T.directions()*0+pi/4,300,0,n=T.n()-1)
F.plot(Q,cmap='tab20b',color_scheme='time',save=True)

##

Q=arcs_on_frame(T,T.directions()*60/pi,pi/6,T.directions()+pi/2,300,0,n=T.n()-1)
F.plot(Q,cmap='Blues',color_scheme='time',save=True)

###

ppl=250
e=0.3
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(12*r),Ellipse(8,e,36),inside=True,loops=3.5,ppl=ppl)
Q=arcs_on_frame(T,T.directions()*10,pi/2,T.directions(),300,0.8)
F.plot(Q,cmap='Wistia',color_scheme='time',save=True)

##

Q=arcs_on_frame(T,T.t,pi/2,T.directions(),300,0)
F.plot(Q,cmap='ocean',color_scheme='time',save=True)

##

Q=arcs_on_frame(T,T.neighbor_distances()*20,pi/6,T.radii()/max(T.radii())*2*pi,300,0.3,n=T.n()-1)
F.plot(Q,cmap='ocean',color_scheme='time',save=True)

###

ppl=500
e=0.3
r=circum(4,semi_minor(4,e))/(2*pi)
T = eIc(Ring(12*r),Ellipse(8,e,36),inside=True,loops=3.5,ppl=ppl)
Q=arcs_on_frame(T,T.neighbor_distances()*20,pi/6,T.neighbor_distances()*15,300,0.3,n=T.n()-1)
F.plot(Q,cmap='hot',color_scheme='time',save=True)
