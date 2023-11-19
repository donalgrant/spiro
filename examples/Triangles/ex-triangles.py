import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_ellipses import *
from spiro_arcs import *
from spiro_string import *
from spiro_triangles import *
from polygon import *
from Ring import *

F=SpiroFig()
F.text_color='white'

hd = 0  # 1 for high-def

def_factor = (1+4*hd)
save=True

F.set_default_dpi(150*(1+hd))
fd = 10*(1+2*hd) # figure dimensions

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,save=save)

###

R1=4
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/3),loops=1,inside=True,ppl=1000)
n=T1.n()//2
figure(triangles_on_frame(T1,1,scale=8,fb=0.5,fh=0.5,pts=500*def_factor,
                           oangle=pi/3,asym=0,n=n,orient=pi+T1.directions()),
       'phase','Oranges')

##

n=T1.n()//5
figure(triangles_on_frame(T1,1,scale=3,fb=0.5,fh=0.5,pts=500*def_factor,
                          oangle=pi/1.5,asym=0,n=n,orient=pi+T1.directions()),
       'cycles','hot')

##

n=T1.n()//5
figure(triangles_on_frame(T1,3,scale=3,fb=0.5,fh=0.5,pts=500*def_factor,
                          oangle=pi/8,asym=0.7,n=n,orient=pi+T1.directions()),
       'cycles',pretty_blues)

###

R1=4
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/3),loops=1,inside=True,ppl=ppl)

np.random.seed(768)
n=T1.n()*2//5
m=n//300
o=np.append(np.full(m-1,0),np.full(1,m))
first=np.random.randint(T1.n())
orient=np.empty(0)
for j in range(n//m):
    orient=np.append(orient,linspace(0,pi/9,m)+np.full(m,-pi/3-T1.direction(first+j*m)))

figure(triangles_on_frame(T1,o,scale=linspace(5,7,m),fb=0.5,fh=0.5,first=first,
                          pts=500*def_factor,oangle=pi/3,asym=0.0,n=m*(n//m),orient=orient),
       'phase',cmap1.reversed())


###

e=0.7
R1=4
ppl=2000
a =major_from_circum(2*pi*R1/6,e)
T1 = eIc(Ring(R1),wheel=Ellipse(a,e,1.3*a),loops=1,inside=True,ppl=ppl)

n=T1.n()//7
figure(triangles_on_frame(T1,5,scale=7,fb=0.5,fh=0.5,first=0,
                          pts=500*def_factor,oangle=pi/3,asym=0.3,n=n,orient=-T1.directions()),
       'phase','OrRd')

###

e=0.7
R1=4
ppl=3000
a =major_from_circum(2*pi*R1/6,e)
T1 = eIc(Ring(R1),wheel=Ellipse(a,e,1.3*a),loops=1,inside=True,ppl=ppl)

S=SpiroData()

cs = 'phase'
my_cmap = 'summer'

d=T1.directions()

np.random.seed(96)
for k in range(2):

    n=200
    first=np.random.randint(T1.n()) 
    
    S.add(triangles_on_frame(T1,1,scale=25,fb=0.5,fh=0.5,first=first,
                         pts=500*def_factor,oangle=pi/3,asym=0.0,n=n,orient=-d[first::1]))

figure(S,cs,my_cmap)

##

S=SpiroData()

cs = 'phase'
my_cmap = 'hot'

d=T1.directions()

np.random.seed(479)
for k in range(5):

    n=100 
    first=np.random.randint(T1.n())
    
    oa=pi/2
    S.add(triangles_on_frame(T1,1,scale=25,fb=0.5,fh=0.5,first=first,
                         pts=500*def_factor,oangle=oa,asym=0.4,n=n,orient=oa-d[first::1]))

figure(S,cs,my_cmap)

###

e=0.8
R1=4
ppl=3000
a =major_from_circum(2*pi*R1/6,e)
T1 = eIe(Ellipse(R1,e),wheel=Ellipse(a,e,1.3*a),loops=1,inside=True,ppl=ppl)

cs = 'y-direction'
my_cmap = 'turbo'

d=T1.directions()

np.random.seed(144)

n=400 
first=np.random.randint(T1.n()-n-1)
oa=pi/1.5
skip=1
figure(triangles_on_frame(T1,skip,scale=linspace(6,8,n),fb=0.5,fh=0.5,first=first,
                          pts=500*def_factor,oangle=oa,asym=0.4,n=n,orient=oa-d[first::skip]),
       cs,my_cmap)

###

e=0.4
R1=4
ppl=1000
a =major_from_circum(circum(R1,semi_minor(R1,e)),e)
T1 = eIe(Ellipse(R1,e),wheel=Ellipse(a/3,0.5,a/4),loops=1,inside=True,ppl=ppl)

d=T1.neighbor_distances()
orient=2*pi* (d-min(d))/(max(d)-min(d))
    
np.random.seed(814)
n=400 
first=np.random.randint(T1.n()-n-1)
oa=pi/3
skip=1
figure(triangles_on_frame(T1,skip,scale=linspace(1,1.2,n),fb=0.5,fh=0.5,first=first,
                          pts=500*def_factor,oangle=oa,asym=0.995,n=n,orient=orient[first::skip]),
       'phase','hot')

###

e=0.4
R1=4
ppl=2000
a =major_from_circum(circum(R1,semi_minor(R1,e)),e)
T1 = eIe(Ellipse(R1,e),wheel=Ellipse(a/3,0.5,a/4),loops=1,inside=True,ppl=ppl)

d=T1.directions()
orient=2*pi* (d-min(d))/(max(d)-min(d))
    
np.random.seed(580)

skip=4
n=400 
first=np.random.randint(T1.n()-skip*(n+1))
oa=pi/4
figure(triangles_on_frame(T1,skip,scale=linspace(6,7.2,n),fb=0.25,fh=0.25,first=first,
                          pts=500*def_factor,oangle=oa,asym=0.0,n=n,orient=orient[first::skip]),
       'phase','jet')

