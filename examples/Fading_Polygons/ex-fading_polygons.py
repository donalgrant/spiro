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

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,save=save)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,save=save,filename=filename)

###
R1=7
ppl=1000
T1 = cIc(Ring(R1),wheel=Wheel(R1/6,R1/3),ppl=ppl,loops=1,inside=True)

skip=1
n=150
oa=pi/2
ao = 0 # np.random.standard_normal(n)*pi/50
asym = 0 # [0.95 * cos(8*pi*j/n) for j in range(n)]
scale=5 # 5*d/(dmax-dmin) # * (1.0-abs(asym))

arc_angle_t=[pi/6,0,pi/6]
arc_angle_p=linspace(-pi/6,pi/6,4*n)

pts = [ 255+np.round(250*sin(2*pi*j/n)).astype(int) for j in range(3*n) ]

seeds = [23,40,655,424,196,956]
cmaps = ['jet','turbo','hot','inferno','magma','autumn']

for j in range(len(seeds)):
    
    my_cmap=cmaps[j]
    np.random.seed(seeds[j])
    offset=np.random.randint(T1.n())
    first=np.random.randint(T1.n())
    S = SpiroData()
    for i in range(3): 
        S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                                 first=first,fh=0.5,fb=0.5,
                                 pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                                 arc_angle=arc_angle_t).rotate(i*2*pi/3))

    figure(S,'length',cmaps[j])

##

skip=2
n=T1.n()//skip
oa=pi/3
ao = 0 
asym = 0.3 
scale=2 

arc_angle_t=[pi/6,0,pi/6]
arc_angle_p=[pi/8,0,pi/8,0]

pts = [ 255+np.round(250*sin(6*pi*j/n)).astype(int) for j in range(4*n) ]

my_cmap='turbo'
seed=155
np.random.seed(seed)
offset=np.random.randint(T1.n())
first=np.random.randint(T1.n())
S = pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                  first=first,fh=0.5,fb=0.5,
                  pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                  arc_angle=arc_angle_p)

figure(S,'length',my_cmap)

###

R1=7
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/6,R1/3),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//skip//5
oa=pi/3
ao = 0
asym = 0.3
scale=4 

arc_angle_p=[pi/4,pi/8,pi/4,pi/8]

pts = [ 255+np.round(250*sin(3*pi*j/n)).astype(int) for j in range(4*n) ]

my_cmap='turbo'
offset=948*2 
first=377*2 
S = pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                  first=first,fh=0.5,fb=0.5,
                  pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                  arc_angle=arc_angle_p).rotate(i*pi)

figure(S,'length','turbo')

##

skip=1
n=T1.n()//skip//5
oa=pi/3
ao = 0 
asym = 0.3
scale=4

arc_angle_p=[pi/4,pi/8,pi/4,pi/8]

pts = [ 255+np.round(250*sin(3*pi*j/n)).astype(int) for j in range(4*n) ]

my_cmap='Oranges'
seed=809
np.random.seed(seed)
offset=np.random.randint(T1.n())
first=np.random.randint(T1.n())

S = pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                  first=first,fh=0.5,fb=0.5,
                  pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                  arc_angle=arc_angle_p).rotate(i*pi)

figure(S,'length','Oranges')

###

R1=7
ppl=2000
T1 = cIc(Ring(R1),wheel=Wheel(R1/6,R1/6),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//skip//4
oa=pi/3
ao = 0 
asym = 0.3
scale=6

arc_angle_p=[pi/4,pi/8,pi/4,pi/8]

pts = [ 255+np.round(250*sin(2*pi*j/n)).astype(int) for j in range(4*n) ]

my_cmap='autumn'
seed=494
np.random.seed(seed)
offset=np.random.randint(T1.n())
first=np.random.randint(T1.n())

S = pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                  first=first,fh=0.5,fb=0.5,
                  pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                  arc_angle=arc_angle_p).rotate(i*pi)

figure(S,'cycles','autumn')

###

R1=7
ppl=1000
T1 = cIc(Ring(R1),wheel=Wheel(R1/6,R1/6),ppl=ppl,loops=1,inside=True)

skip=4
n=T1.n()//skip//5
oa=pi/3
ao = linspace(0,pi,n)
asym = 0.3

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=2*(d-dmin)/(dmax-dmin)+1.0

arc_angle_t=[pi/6,0,pi/6]
arc_angle_p=[pi/4,pi/8,pi/4,pi/8]

pts = np.round(linspace(500*def_factor,2*def_factor,3*n)).astype(int)

my_cmap='hot'
seed=143
np.random.seed(seed)
offset=np.random.randint(T1.n())
first=np.random.randint(T1.n())

S = SpiroData()
n_swoops=6
for i in range(n_swoops):
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                      first=first+i*T1.n()//n_swoops,fh=0.5,fb=0.5,
                      pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                      arc_angle=arc_angle_t))

figure(S,'phase',pretty_blues)

###

e=0.7
R=7
ppl=1000
a=circum(R1,semi_minor(R1,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

skip=2
n=T1.n()//skip
oa=pi/3
ao = linspace(0,pi,n)
asym = 0.3

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=0*(d-dmin)/(dmax-dmin)+4.0

arc_angle_t=[-pi/6,0,-pi/6]

pts = [ 255+np.round(250*sin(6*pi*j/n)).astype(int) for j in range(3*n) ]

for (seed,cs,c) in zip([271,704,516],['time','cycles','time'],['hot',pretty_blues,emerald_woman]):
    np.random.seed(seed)
    offset=np.random.randint(T1.n())
    first=np.random.randint(T1.n())

    S = triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                           first=first,fh=0.5,fb=0.5,
                           pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                           arc_angle=arc_angle_t)

    figure(S,cs,c)
