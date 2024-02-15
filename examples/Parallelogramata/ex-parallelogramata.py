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
from spiro_frame import *
from polygon import *
from Ring import *

parser = argparse.ArgumentParser(description="Parallelogram Examples")
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

R1=20
ppl=400
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/4),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//2
scale=15 
first=T1.n()//5 
offset = T1.n()//4
oa=pi/8
ao = 0
asym=0
S=figure(directed_pars(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                       pts=200*def_factor,asym=asym),
         'length','Reds')

###

R1=20
ppl=500
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/5),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//2
scale=30
first=T1.n()//5
offset = T1.n()//4
oa=pi/4
ao = 0 
asym=0
S=figure(directed_pars(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                       pts=200*def_factor,asym=asym),
         'length',emerald_woman)

###

R1=20
ppl=500
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/5),ppl=ppl,loops=1,inside=False)

skip=1
n=T1.n()//2
scale=30
first=T1.n()//5
offset = T1.n()//4 
oa=pi/4
ao = 0
asym=0
S=figure(directed_pars(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                       pts=200*def_factor,asym=asym),
         'length','hot')

###

R1=20
ppl=1000
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//4
scale=20
first=T1.n()//5
offset = T1.n()//3
oa=pi/4
ao = pi/6
asym=linspace(0,0.2,n)
S=figure(directed_pars(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                       pts=200*def_factor,asym=asym),
         'length','turbo')

###

R1=20
ppl=600
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()
scale=10
first=T1.n()//5
offset = T1.n()//3 
oa=pi/2
ao = linspace(0,12*pi,n) 
asym=0.3 
figure(directed_pars(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                     pts=200*def_factor,asym=asym),
       'time','hot')

###

R1=5
ppl=1500
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/6),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()
scale=[2,2.5,3]
first=T1.n()//5
offset = T1.n()//2
oa=pi/4
ao = linspace(0,-2*pi,n)
asym=-0.3
figure(directed_pars(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                     pts=200*def_factor,asym=asym),
       'cycles','Oranges')

###

R1=5
ppl=500
T1 = cIc(Ring(R1),wheel=Wheel(R1/1.5,R1),ppl=ppl,loops=2,inside=True)

skip=2
n=T1.n()//2
scale=5
first=T1.n()//5
offset = T1.n()//2
oa=pi/4
ao = [0,pi]
asym=0.
figure(directed_pars(T1,skip=skip,offset=offset,scale=scale,oangle=oa,angle_offset=ao,n=n,first=first,
                     pts=200*def_factor,asym=asym),
       'direction',pretty_blues)

###

R1=5
ppl=400
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/4),ppl=ppl,loops=1,inside=True)

skip=[6,1,1,1,1,1]
n=T1.n()
scale=5
first=0 
offset=1
oa=pi/2
ao = linspace(pi/4,3*pi,n)
asym=0.2
figure(pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0,fb=0,
                     pts=500*def_factor,asym=asym,orient_follow=None,orient=ao),
       'l-waves','turbo')

###

R1=5
ppl=1500
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/4),ppl=ppl,loops=1,inside=True)

skip=5 # [20,1,1,1,1,1,1]
n=T1.n()//skip
first=0 
offset=1
oa=pi/2 
ao = pi/4
asym = 0.5
scale=5 * (1.0-abs(asym))
figure(pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                     pts=500*def_factor,asym=asym,orient_follow=5,orient=ao),
       'l-waves','OrRd')

###

R1=5
ppl=1500
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/4),ppl=ppl,loops=1,inside=True)

skip=2 
n=T1.n()//skip
first=0 
offset=1
oa=pi/4 
ao = linspace(0,6*pi,n)
asym = [0.95 * cos(8*pi*j/n) for j in range(n)]
scale=2 * (1.0-abs(asym))
figure(pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                     pts=500*def_factor,asym=asym,orient_follow=5,orient=ao),
       'time',pretty_blues)

###

R1=5
ppl=1500
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/4),ppl=ppl,loops=1,inside=True)

skip=5
n=T1.n()//skip
first=0 
offset=1
oa=pi/2+pi/15
ao = np.random.standard_normal(n)*pi/100
asym = 0 
scale=5
figure(pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                     pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao),
       'time',pinks)
