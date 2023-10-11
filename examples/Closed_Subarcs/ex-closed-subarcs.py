import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from spiro_string import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

F.set_default_dpi(150)

###

T = spiro_cross(wheel=Wheel(1,4)).rotate(pi/4).subsample(5)
N=T.n()
cs = 'length'
c = cmap1

S=SpiroData()

np.random.seed(288)
first=np.random.randint(0,N//2)
first_plot=True
for k in range(2):
    S.add(closed_subarcs(T,[N//2-1,N//2-1,N//2-1],[pi,pi,pi/4,pi/4],
                         invert=True,skip=1,first=first+k*N//3,n=55))

F.plot(S,cmap=c,color_scheme=cs,save=True)

##

cs = 'length'
c = 'Reds'

S=SpiroData()

np.random.seed(901)
first=np.random.randint(0,N//2)

for k in range(2):
    S.add(closed_subarcs(T,[N//2-1,N//2-1,N//2-1],[pi/4,pi/3,pi/3],invert=True,skip=1,first=first+k*N//4,n=55))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'time'
c = 'ocean'

S=SpiroData()
np.random.seed(774)
first=np.random.randint(0,N//2)
for k in range(2):
    S.add(closed_subarcs(T,[N//2-1,N//3-1,N//4-1],[pi,pi/3,pi/3],invert=True,skip=1,first=first+k*N//4,n=55))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'length'
c = 'Wistia'

S=SpiroData()
np.random.seed(156)
first=np.random.randint(0,N//2)
for k in range(2):
    S.add(closed_subarcs(T,[N//4-1 for i in range(5)],pi,invert=True,skip=1,first=first+k*N//4,n=55))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'cycles'
c = 'ocean'

S=SpiroData()

np.random.seed(239)
first=np.random.randint(0,N//2)

for k in range(2):
    S.add(closed_subarcs(T,[N//4-3 for i in range(15)],pi,invert=True,skip=1,first=first+k*N//4,n=15))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'length'
c = 'OrRd'

S=SpiroData()

np.random.seed(745)
first=np.random.randint(0,N//2)

for k in range(3):
    S.add(closed_subarcs(T,[N//8-3 for i in range(25)],pi,invert=True,skip=1,first=first+k*N//4,n=8))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'length'
c = 'OrRd'

S=SpiroData()

np.random.seed(946)
first=np.random.randint(0,N//2)

for k in range(4):
    S.add(closed_subarcs(T,[N//8-3 for i in range(20)],pi/(k+1),invert=True,skip=1,first=first+k*N//4,n=20))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

###

T = spiro_eq_triangle(wheel=Wheel(6,6),loops=1).subsample(3)
N=T.n()

cs = 'length'
c = 'OrRd'

S=SpiroData()

np.random.seed(874)
first=np.random.randint(0,N//2)

for k in range(1):
    S.add(closed_subarcs(T,[N//4-1,N//3-1],pi/2,invert=True,skip=2,first=first+k*N//4,n=50))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'length'
c = 'Wistia'

S=SpiroData()

np.random.seed(252)
first=np.random.randint(0,N//2)

for k in range(1):
    S.add(closed_subarcs(T,[N//4-1,N//3-1],pi/2,invert=True,skip=1,first=first+k*N//4,n=80))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'length'
c = 'jet'

S=SpiroData()

np.random.seed(399)
first=np.random.randint(0,N//2)

for k in range(1):
    S.add(closed_subarcs(T,[N//5-1,N//3-1],pi,invert=True,skip=1,first=first+k*N//4,n=200))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'length'
c = 'jet'

S=SpiroData()

np.random.seed(609)
first=np.random.randint(0,N//2)

for k in range(3):
    S.add(closed_subarcs(T,[N//5-1,N//3-1],pi,invert=True,skip=1,first=first+k*N//4,n=100))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

cs = 'length'
c = 'ocean'

S=SpiroData()

np.random.seed(188)
first=np.random.randint(0,N//2)

for k in range(5):
    S.add(closed_subarcs(T,[N//6,N//5,N//4],pi/1.5,invert=True,skip=1,first=first+k*N//5,n=60))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

###

T = spiro_eq_triangle(wheel=Wheel(6,6),loops=1).subsample(3)
N=T.n()

cs = 'phase'
c = 'OrRd'

S=SpiroData()

np.random.seed(578)
first=np.random.randint(0,N//2)

for k in range(1):
    S.add(closed_subarcs(T,[N//5,N//5,N//5,N//5,N//5],pi/1.5,invert=True,skip=1,
                         first=first+k*N//5,n=250,interp_phase=True))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

###

T = spiro_cross(wheel=Wheel(2,1),loops=1,inside=True).subsample(3)    
N=T.n()

cs = 'phase'
c = 'ocean'

S=SpiroData()

np.random.seed(528)
first=np.random.randint(0,N//2)

for k in range(2):
    S.add(closed_subarcs(T,[N//5,N//5],pi/3,invert=True,skip=8,first=first+k*N//2,n=150,interp_phase=True))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)

##

T = spiro_cross(wheel=Wheel(2,1),loops=1,inside=True).subsample(3)
N=T.n()

cs = 'phase'
c = 'ocean'

S=SpiroData()

np.random.seed(475)
first=np.random.randint(0,N//2)

for k in range(2):
    S.add(closed_subarcs(T.rotate(-pi/8),[N//5,N//5],pi/3,invert=True,
                         skip=8,first=first+k*N//2,n=100,interp_phase=True))
    
F.plot(S.rotate(-pi/2),cmap=c,color_scheme=cs,alpha=0.4,save=True)

###

T = spiro_cross(wheel=Wheel(2,1),loops=1,inside=True).subsample(3)    
N=T.n()

cs = 'phase'
c = 'turbo'

S=SpiroData()

np.random.seed(706)
first=np.random.randint(0,N//2)

for k in range(3):
    S.add(closed_subarcs(T.rotate(-pi/8),[N//5,N//5],pi/3,invert=True,
                         skip=6,first=first+k*N//3,n=100,interp_phase=True))
    
F.plot(S,cmap=c,color_scheme=cs,alpha=0.4,save=True)
