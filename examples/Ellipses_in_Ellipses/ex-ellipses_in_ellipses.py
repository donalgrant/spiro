import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from spiro_ellipse import *
from Ring import *

S = SpiroData()
F = SpiroFig()
F.text_color='white'

###

c = cmap_list()
cs = cs_list()

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",
                                         ["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",
                                         ["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",
                                         ["seagreen","teal","cornflowerblue","mediumblue","indigo"])

fig_n = 0

###

S.reset()
F = SpiroFig()
a=9.0
nc=10
bv=[0.8*a-0.03*a*i for i in range(nc)]
for i in range(nc):
    S.add(eIe(Ellipse(30,0.7,0,pi/4),
                             Ellipse(a,0.5,bv[i]),10,inside=True)).rotate(pi/30).move(0,-1)

F.plot(S,color_scheme='length',cmap=cmap3,save=True)

###

S.reset()
a=9.0
nc=20
bv=[0.8*a-0.02*a*i for i in range(nc)]
for i in range(nc):
    S.add(eIe(Ellipse(30,0.7,0,pi/2),
                             Ellipse(a,0.5,bv[i]),5,inside=True)).rotate(pi/30).move(0.5,-1)
    
F.plot(S,color_scheme='length',cmap='inferno',save=True)

###

S.reset()
a=9.0
nc=20
bv=[0.8*a-0.02*a*i for i in range(nc)]
for i in range(nc):
    S.add(eIe(Ellipse(30,0.7,0,pi/2),
                             Ellipse(a,0.5,bv[i]),5,inside=True)).rotate(pi/10).move(0.5,-1)

F.plot(S,color_scheme='length',cmap='Reds',save=True)

###

S.reset()
a=9.0
nc=10
bv=[0.8*a-0.005*a*i for i in range(nc)]
for i in range(nc):
    S.add(eIe(Ellipse(10,0.6,0,pi/2),
                             Ellipse(a,0.5,bv[i]),5,inside=True)).rotate(pi/5).move(0.5,-1)

F.plot(S,color_scheme='length',cmap='autumn',save=True)

###

S.reset()
a=9.0
nc=5
bv=[0.8*a-0.005*a*i for i in range(nc)]
for i in range(nc):
    S.add(eIe(Ellipse(11,0.6,0,pi/4,i*pi/30),
                             Ellipse(a,0.5,bv[i]),10,inside=True))

F.plot(S,color_scheme='length',cmap='summer',save=True)

###

S.reset()
a=9.0
for i in range(10):
    S.add(eIe(Ellipse(11.5,0.6,0,pi/4,i*pi/30),
                             Ellipse(a,0.5,0.8*a-0.05*a*i),5,inside=True))

F.plot(S,color_scheme='time',cmap=cmap1,save=True)

###

S.reset()
a=9.0
for i in range(10):
    S.add(eIe(Ellipse(11.5+i/40,0.6,0,pi/4,i*pi/50),
                             Ellipse(a,0.5,0.8*a-0.05*a*i),5,inside=True))

F.plot(S,color_scheme='radial',cmap=cmap2,save=True)

###

S.reset()
a=9.0
for i in range(10):
    S.add(eIe(Ellipse(12+i*0,0.6,0,pi/3,i*pi/50),
                             Ellipse(2,0.5,0.8*a-0.05*a*i),1,inside=False))

F.plot(S,color_scheme='time',cmap=cmap1,save=True)
    
###

S.reset()
a=11.0
for i in range(10):
    S.add(eIe(Ellipse(9+i*0,0.3,0,pi/3,i*pi/50),
                             Ellipse(1.5,0.3,0.8*a-0.05*a*i),1,inside=False))

F.plot(S,color_scheme='time',cmap='Reds',save=True)
