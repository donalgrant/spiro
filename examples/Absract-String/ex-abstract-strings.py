import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_string import *
from polygon import *

S = SpiroData()
F = SpiroFig()

F.set_default_dpi(300)

for o in range(10): 
    S.add(spiro_cross(wheel=Wheel(2,5.5,0),orient=pi/40*o,loops=2,fold=False))

F.plot(S,cmap='turbo',color_scheme='xrand',alpha=1,save=True)


###

F.plot(string_dispersing_pairs(S,step=500,step2=500,offset=3000),
       cmap='turbo',color_scheme='length',save=True)

F.plot(string_dispersing_links(S,step0=10,step=40,offset=200),
       cmap='turbo',color_scheme='cycles',save=True)
       
F.plot(strings_from_coord(S,offset=200),
       cmap='turbo',color_scheme='l-waves',save=True)

###

F.plot(string_offset_pairs(S,step=500,offset=3000),save=True)

# should initialize the random generator here with a seed

np.random.seed(547)

for c in ['turbo','jet']:
       SS5=SpiroData()
       SS5.add(strings_from_pts(S,8,nLines=30,offset=30))
       SS5.add(strings_from_pts(S,4,nLines=30,offset=10))
       SS5.add(strings_from_pts(S,4,nLines=30,offset=50))
       F.plot(SS5,cmap=c,color_scheme='l-waves',save=True)

###
       
SS5=SpiroData()
np.random.seed(548)

SS5.add(strings_from_pts(S,8,nLines=30,offset=30))
SS5.add(strings_from_pts(S,4,nLines=30,offset=30))
SS5.add(strings_from_pts(S,4,nLines=30,offset=30))
F.plot(SS5,cmap='turbo',color_scheme='l-waves',save=True)

###

SS5=SpiroData()
np.random.seed(549)

for i in range(6):
    SS5.add(strings_from_pts(S,4,nLines=8,offset=10))
F.plot(SS5,cmap='turbo',color_scheme='l-waves',save=True)

###
np.random.seed(550)

F.plot(strings_from_pts(S,70,nLines=8,offset=100,fixed=50),
       cmap='turbo',color_scheme='l-waves',save=True)

###

np.random.seed(551)

F.plot(strings_from_pts(S,70,nLines=20,offset=30,fixed=50),
       cmap='turbo',color_scheme='l-waves',save=True)

