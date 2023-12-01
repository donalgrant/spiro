import sys
sys.path.append('../..')
import argparse

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

parser = argparse.ArgumentParser(description="replot stored pickle file")
parser.add_argument("--full_res", help="use high-definition mode", action="store_true")
args = parser.parse_args()


F=SpiroFig()
F.text_color='white'

if args.full_res:
    hd = 1
else:
    hd = 0

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
T1 = SpiroData()
for t in linspace(0,2*pi/7,4):
    T1.add(spiro_nstar(7,r1=R1,wheel=Wheel(R1/20,R1/40),loops=1,inside=True).subsample(20).rotate(t).move(t,0))

skip=1
n=T1.n()
s = T1.neighbor_distances()
scale=1
first=0
offset = T1.n()//3
oa=pi/4
asym=0 
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,n=n,first=first,
                          pts=50*def_factor,asym=asym),
       'time','bone')

###

R1=2
T1 = spiro_nstar(7,r1=R1,wheel=Wheel(R1/20,R1/40),loops=1,inside=True).subsample(20)

clist = [ 'xkcd:'+i for i in ['dark gold','gold','dark gold','muddy green','dark gold'] ]
gold = cmap_from_list(clist,'gold')

skip=1
n=T1.n()
s = T1.neighbor_distances()
scale=1
first=0
offset = T1.n()//3
oa=pi/4
asym=0 
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,n=n,first=first,
                          pts=100*def_factor,asym=asym),
       'time',gold)

###

R1=20
T1=spiro_nstar(7,r1=R1,r2=0.4,wheel=Wheel(R1/8,R1/8),loops=3,inside=False).subsample(20)

skip=1
n=T1.n()
s = T1.neighbor_distances()
scale=10
first=0
offset = T1.n()//3
oa=pi/4
asym=0 
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,n=n,first=first,
                          pts=100*def_factor,asym=asym),
       'direction','hot')

###


R1=20
T1=spiro_nstar(7,r1=R1,r2=0.4,wheel=Wheel(R1/8,R1/8),loops=1,inside=False).subsample(15)

skip=1
n=T1.n()//3
s = T1.neighbor_distances()
scale=15
first=107
offset = T1.n()//3
oa=pi/4
asym=0.8 
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,n=n,first=first,
                          pts=100*def_factor,asym=asym),
       'x-direction','OrRd')

##

skip=1
n=T1.n()//3
s = T1.neighbor_distances()
scale=15
first=389
offset = T1.n()//6
oa=pi/40
asym=0.
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,n=n,first=first,
                          pts=300*def_factor,asym=asym),
       'phase','turbo')

###

R1=20
ppl=500
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/1),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()
s = T1.neighbor_distances()
scale=linspace(10,20,n) # .4*(max(s)-min(s))/(s-min(s)+0.1)
first=0 # np.random.randint(T1.n()-skip*(n+1))
offset = T1.n()//6 # T1.n()//8 # np.random.randint(T1.n())
oa=linspace(pi/8,pi/2,n)
asym=linspace(0.0,0.7,n)
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,n=n,first=first,
                          pts=300*def_factor,asym=asym),
       'cycles',cmap1)

##

R1=20
ppl=1000
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/1),ppl=ppl,loops=1,inside=False)

skip=1
n=T1.n()-1
s = T1.neighbor_distances()
scale=30 # .4*(max(s)-min(s))/(s-min(s)+0.1)
first=0 # np.random.randint(T1.n()-skip*(n+1))
offset = T1.n()//10 # T1.n()//8 # np.random.randint(T1.n())
oa=pi/3
asym=0
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,n=n,first=first,
                          pts=200*def_factor,asym=asym),
       'direction','ocean')

###

R1=20
ppl=400
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/3.2),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()
s = T1.neighbor_distances()
scale=15 # linspace(5,15,n) # .4*(max(s)-min(s))/(s-min(s)+0.1)
first=0 # np.random.randint(T1.n()-skip*(n+1))
offset = T1.n()//8 # np.random.randint(T1.n())
oa=pi/3 
ao = np.random.standard_normal(n)*pi/60+linspace(0,pi/6,n)
asym=0
figure(directed_triangles(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                          pts=200*def_factor,asym=asym),
       'time','Reds')
