import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_string import *
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


