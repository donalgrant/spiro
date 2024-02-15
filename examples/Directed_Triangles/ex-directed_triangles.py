import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_ellipses import *
from spiro_arcs import *
from spiro_string import *
from spiro_frame import *
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
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/3),loops=1,inside=True,ppl=ppl)

np.random.seed(606)

skip=1
n=400 
f=0.5

first=np.random.randint(T1.n()-skip*(n+1))
offset = T1.n()//3
orient = [ T1.chord_direction(first+j,first+j+offset) for j in range(0,n,skip) ]
oa=pi/4

figure(triangles_on_frame(T1,skip,scale=[5,7,9],fb=f,fh=f,first=first,
                          pts=500*def_factor,oangle=oa,asym=0.0,n=n,orient=orient),
       'y-direction','OrRd')

##

np.random.seed(44)

skip=1
n=400 
f=0.5

first=np.random.randint(T1.n()-skip*(n+1))
offset = np.random.randint(T1.n())
orient = [ T1.chord_direction(first+j,first+j+offset) for j in range(0,n,skip) ]
oa=pi/4

figure(triangles_on_frame(T1,skip,scale=[3,4,5],fb=f,fh=f,first=first,
                          pts=500*def_factor,oangle=oa,asym=0.0,n=n,orient=orient),
       'spacing','Reds')

##

np.random.seed(370)

skip=1
n=400 
f=0.5

first=np.random.randint(T1.n()-skip*(n+1))
offset = np.random.randint(T1.n())
orient = [ T1.chord_direction(first+j,first+j+offset) for j in range(0,n,skip) ]
oa=pi/4

figure(triangles_on_frame(T1,skip,scale=[3,4,5],fb=f,fh=f,first=first,
                          pts=500*def_factor,oangle=oa,asym=0.0,n=n,orient=orient),
       'cycles','turbo')

###

R1=4
ppl=500
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/6),loops=1,inside=True,ppl=ppl)

np.random.seed(384)

skip=1
n=150 
f=0.5

first=np.random.randint(T1.n()-skip*(n+1))
offset = np.random.randint(T1.n())
orient = [ T1.chord_direction(first+j,first+j+offset) for j in range(0,n,skip) ]
oa=pi/4
figure(triangles_on_frame(T1,skip,scale=[3],fb=f,fh=f,first=first,
                          pts=500*def_factor,oangle=oa,asym=0.0,n=n,orient=orient),
       'length','Oranges')

##

figure(directed_triangles(T1,1,first=2,offset=424,scale=3,oangle=pi/6,n=150,pts=500*def_factor),
       'length',cmap1)

##

figure(directed_triangles(T1,1,first=217,offset=438,scale=3,oangle=pi/6,n=150,pts=500*def_factor),
       'length','OrRd')

##

figure(directed_triangles(T1,1,first=276,offset=42,scale=3,oangle=pi/6,n=150,pts=500*def_factor),
       'length','Wistia')

##

figure(directed_triangles(T1,1,first=59,offset=380,scale=3,oangle=pi/6,n=150,pts=500*def_factor),
       'length','autumn')

##

figure(directed_triangles(T1,1,first=236,offset=386,scale=linspace(3,4,150),oangle=pi/6,n=150,pts=500*def_factor),
       'length','Reds')

##

figure(directed_triangles(T1,1,first=256,offset=321,scale=linspace(3,4,150),oangle=pi/6,n=150,pts=500*def_factor),
       'length',pretty_blues)

###

R1=4
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/6),loops=1,inside=True,ppl=500)

figure(directed_triangles(T1,1,first=143,offset=148,scale=linspace(3,4,150),oangle=pi/6,n=150,pts=500*def_factor),
       'length','Reds')

##

figure(directed_triangles(T1,1,first=232,offset=81,scale=linspace(3,4,150),oangle=pi/6,n=150,pts=500*def_factor),
       'length','Reds')

##

figure(directed_triangles(T1,1,first=305,offset=28,scale=linspace(3,4,150),
                          oangle=linspace(pi/1.5,pi/16,150),n=150,pts=500*def_factor),
       'length',pretty_blues)

##

R1=4
T1 = cIc(Ring(R1),wheel=Wheel(R1/7,R1),loops=1,inside=True,ppl=2500)

figure(directed_triangles(T1,1,first=1492,offset=2496,scale=5,
                          oangle=pi/4,n=150,pts=500*def_factor),
       'length','Reds')

###

R1=4
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/3),ppl=ppl,inside=True)

figure(directed_triangles(T1,1,first=66,offset=354,scale=7,
                          oangle=pi/6,n=150,pts=500*def_factor),
       'length','Reds')

##

figure(directed_triangles(T1,1,first=148,offset=268,scale=11,
                          oangle=pi/6,n=150,pts=500*def_factor),
       'length','Oranges')

##

s = T1.neighbor_distances()
scale = 5 * (max(s)-min(s))/(s-min(s)+0.1)

figure(directed_triangles(T1,1,first=143,offset=148,scale=scale,
                          oangle=pi/16,n=150,pts=500*def_factor),
       'length','ocean')

###

R1=4
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/3),ppl=500,inside=True)

s = T1.neighbor_distances()
scale = 5 * (max(s)-min(s))/(s-min(s)+0.1)

figure(directed_triangles(T1,1,first=142,offset=102,scale=scale,
                          oangle=pi/16,n=150,pts=500*def_factor),
       'length','OrRd')
