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

T=cIc(Ring(30),Wheel(6,10.5),loops=1,inside=True,ppl=1000)
N=T.n()
S=closed_paths(T,[N//3,N//4,N//5],first=0,skip=1,n=N)

F.plot(S,cmap='OrRd',color_scheme='time',alpha=0.2,save=True)

##

S=closed_paths(T,[N//3,N//4,N//10],first=0,skip=1,n=N//3)
F.plot(S,cmap='OrRd',color_scheme='time',alpha=0.2,save=True)

##

S=closed_paths(T,[N//3,N//4],first=0,skip=3,n=N//17)
F.plot(S,cmap='Wistia',color_scheme='time',alpha=0.5,save=True)

##

S=closed_paths(T,[N//3,N//17],first=0,skip=3,n=N//17)
F.plot(S,cmap='Reds',color_scheme='time',alpha=0.5,save=True)

##

S=closed_paths(T,arange(N//24,N//21,1),first=0,skip=3,n=N//7)
F.plot(S,cmap=cmap3,color_scheme='length',alpha=0.5,save=True)

##

S=closed_paths(T,[N//3],first=0,skip=3,n=N//7)
F.plot(S,cmap=cmap2,color_scheme='length',alpha=0.5,save=True)

##

alpha=1.0
cmap=['Reds','Blues','Greens','Purples']
first_plot=True
np.random.seed(320)
first=np.random.randint(0,N,4)
for i in range(4):
    S=closed_paths(T,[N//3,N//4],first=first[i],skip=3,n=20)
    F.plot(S,cmap=cmap[i],color_scheme='length',alpha=alpha,
           new_fig = True if first_plot else False)
    first_plot=False

F.save_fig()

##

first_plot=True
np.random.seed(918)
first=np.random.randint(0,N,4)
for i in range(4):
    S=closed_arcs(T,[N//3,N//4],50,invert=True,first=first[i],skip=3,n=20)
    F.plot(S,cmap=cmap[i],color_scheme='length',alpha=alpha,
           new_fig = True if first_plot else False)
    first_plot=False

F.save_fig()

##

first_plot=True
np.random.seed(889)
first=np.random.randint(0,N,4)
for i in range(4):
    S=closed_arcs(T,[N//3,N//4],50,invert=False,first=first[i],skip=3,n=20)
    F.plot(S,cmap=cmap[i],color_scheme='length',alpha=alpha,
           new_fig = True if first_plot else False)
    first_plot=False

F.save_fig()

##

first_plot=True
np.random.seed(740)
first=np.random.randint(0,N,4)
for i in range(4):
    S=closed_arcs(T,[N//3,N//4],50,invert=[True,False],first=first[i],skip=3,n=20)
    F.plot(S,cmap=cmap[i],color_scheme='length',alpha=alpha,
           new_fig = True if first_plot else False)
    first_plot=False

F.save_fig()

##

cmap=['Wistia','Reds','ocean','jet']
first_plot=True
np.random.seed(332)
first=np.random.randint(0,N,4)
for i in range(4):
    S=closed_arcs(T,[N//3,N//4,N//5],50,invert=[True,False],first=first[i],skip=3,n=20)
    F.plot(S,cmap=cmap[i],color_scheme='length',alpha=alpha,
           new_fig = True if first_plot else False)
    first_plot=False

F.save_fig()

##

cmap=['Wistia','Reds','autumn','jet']
first_plot=True
np.random.seed(917)
first=np.random.randint(0,N,4)
for i in range(4):
    S=closed_arcs(T,[N//3],50,invert=[True,False],first=first[i],skip=3,n=50)
    F.plot(S,cmap=cmap[i],color_scheme='length',alpha=alpha,
           new_fig = True if first_plot else False)
    first_plot=False

F.save_fig()

###

ppl=1000
e=0.5
wheel_r=5
eps=0.5
rf=1
r=major_from_circum(2*pi*wheel_r*rf,e)
T = cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*0.8),inside=True,loops=2.0,ppl=ppl).rotate(pi/4)
    
N=T.n()

cs = 'length'
c = [cmap1,'Reds','Wistia']
o = 31
r=60
S=SpiroData()
seed = np.random.randint(0,1000)
np.random.seed(191)
for k in range(3):
    S=closed_arcs(T,[N//3,N//4],linspace(50,90,8),invert=True,skip=4+2*k,first=np.random.randint(0,N//2),n=30)
    F.plot(S,cmap=c[k],color_scheme='time',new_fig=True if k==0 else False,alpha=0.5)

F.save_fig()

###

ppl=1000
e=0.5
wheel_r=5
eps=0.5
rf=1
r=major_from_circum(2*pi*wheel_r*rf,e)
T = cIe(Ellipse(r*(1+eps),e),Wheel(wheel_r,wheel_r*0.8),inside=False,loops=2.0,ppl=ppl).rotate(pi/4)
    
N=T.n()

cs = 'cycles'
c = 'jet'

np.random.seed(177)
first_plot=True
for k in range(3):
    first=np.random.randint(0,N//2)
    S=closed_arcs(T,[N//3,N//4],linspace(50,80,4),invert=True,skip=3+k,first=first,n=40)
    F.plot(S,cmap=c,color_scheme=cs,new_fig=True if first_plot else False,alpha=0.5)
    first_plot=False
    S=closed_arcs(T,[N//3,N//4],linspace(50,80,4),invert=False,skip=3+k,first=first,n=40)
    F.plot(S,cmap=c,color_scheme=cs,new_fig=False,alpha=0.5)

F.save_fig()

##

cs = 'length'
c = 'jet'

S=SpiroData()

np.random.seed(284)
first_plot=True
for k in range(12):
    first=np.random.randint(0,N//2)
    S.add(closed_arcs(T,[N//3,N//4],linspace(50,80,6),invert=True,skip=2,first=first,n=20))
    
F.plot(S,cmap=c,color_scheme=cs)

###

T = spiro_cross(wheel=Wheel(1,4)).rotate(pi/4).subsample(5)
N=T.n()

cs = 'length'
c = 'jet'

S=SpiroData()
np.random.seed(229)
first_plot=True
for k in range(5):
    first=np.random.randint(0,N//2)
    S.add(closed_arcs(T,[N//3,N//4],linspace(50,80,6),invert=True,skip=1,first=first,n=50))
    
F.plot(S,cmap=c,color_scheme=cs,save=True)

##

cs = 'cycles'
c = 'ocean'

S=SpiroData()
np.random.seed(501)
first_plot=True
for k in range(5):
    first=np.random.randint(0,N//2)
    S.add(closed_arcs(T,[N//3,N//4],linspace(50,80,6),invert=True,skip=1,first=first,n=50))
    
F.plot(S,cmap=c,color_scheme=cs,save=True)

##

cs = 'cycles'
c = 'autumn'

S=SpiroData()
np.random.seed(642)
first_plot=True
for k in range(5):
    first=np.random.randint(0,N//2)
    S.add(closed_arcs(T,[N//3,N//4],30,invert=True,skip=1,first=first,n=50))

F.plot(S,cmap=c,color_scheme=cs,save=True)

##

cs = 'length'
c = 'autumn'

S=SpiroData()
np.random.seed(805)
first_plot=True
for k in range(10):
    first=np.random.randint(0,N//2)
    S.add(closed_arcs(T,[N//3,N//4],30,invert=True,skip=1,first=first,n=20))

F.plot(S,cmap=c,color_scheme=cs,save=True)
