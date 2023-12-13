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

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,save=save)

###
R1=7
ppl=500
T1 = cIc(Ring(R1),wheel=Wheel(R1/3,R1/3),ppl=ppl,loops=1,inside=True)

skip=2
n=T1.n()//skip
first=0 
offset=1
oa=pi/3
ao = 0
asym = 0.6 
scale=2

arc_angle=pi/4

offset=T1.n()//3
figure(triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                          pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                          arc_angle=[arc_angle,-arc_angle,arc_angle]),
       'time',pinks)

figure(triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                          pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                          arc_angle=[arc_angle,-arc_angle,arc_angle]),
       'time',pretty_blues)

##

skip=2
n=T1.n()//skip
first=0
offset=1
oa=pi/4
ao = 0 # np.random.standard_normal(n)*pi/50
asym = 0. # [0.95 * cos(8*pi*j/n) for j in range(n)]
scale=2 # * (1.0-abs(asym))

arc_angle=pi/4

offset=T1.n()//2
figure(triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0,fb=0.5,
                          pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                          arc_angle=[arc_angle,arc_angle,arc_angle]),
       'cycles',pale_pink)

###

R1=7
ppl=1000
T1 = cIc(Ring(R1),wheel=Wheel(R1/6,R1/3),ppl=ppl,loops=1,inside=True)

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=1
n=T1.n()//skip//12
first=T1.n()//3
offset=1
oa=pi/4
ao = 0
asym = 0.
scale=5*d/(dmax-dmin)

arc_angle=pi/2

S=SpiroData()

for i in range(3):
    offset=T1.n()//3
    first=i*T1.n()//3
    S.add(pars_on_frame(T1,skip=skip,scale=scale[::skip],oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                        pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                        arc_angle=arc_angle))

figure(S,'time','copper')

##

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=1
n=T1.n()//skip//12
first=T1.n()//3
offset=1
oa=pi/4
ao = 0 # np.random.standard_normal(n)*pi/50
asym = 0. # [0.95 * cos(8*pi*j/n) for j in range(n)]
scale=15*d/(dmax-dmin) # * (1.0-abs(asym))

arc_angle=pi/2

S=SpiroData()

for i in range(3):
    offset=T1.n()//3
    first=i*T1.n()//3
    S.add(triangles_on_frame(T1,skip=skip,scale=scale[::skip],oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                            pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                            arc_angle=arc_angle))

figure(S,'phase','ocean')

##

seed=751 
np.random.seed(seed)

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=2
n=60
oa=pi/4
ao = 0 
asym = -0.3
scale=5*d/(dmax-dmin)

arc_angle=pi/8

S=SpiroData()

for i in range(3):
    offset=np.random.randint(T1.n())
    first=np.random.randint(T1.n())
    S.add(pars_on_frame(T1,skip=skip,scale=scale[::skip],oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                            pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                            arc_angle=arc_angle))
    S.add(pars_on_frame(T1,skip=skip,scale=scale[::skip]*1.2,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                            pts=500*def_factor,asym=asym,orient_follow=offset+1,orient=ao,
                            arc_angle=arc_angle))

figure(S,'time','Oranges')

##

seed=609 # np.random.randint(1000)
np.random.seed(seed)

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=2
n=200
oa=pi/4
ao = 0
asym = -0.3
scale=5*d/(dmax-dmin) # * (1.0-abs(asym))

arc_angle=linspace(0,pi/6,3*n)

offset=np.random.randint(T1.n())
first=np.random.randint(T1.n())

S=SpiroData()

S.add(triangles_on_frame(T1,skip=skip,scale=scale[::skip],oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                         pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                         arc_angle=arc_angle))

figure(S,'length','turbo')

##

seed=220 
np.random.seed(seed)

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=1
n=150
oa=pi/4
ao = 0
asym = 0
scale=5*d/(dmax-dmin) # * (1.0-abs(asym))

arc_angle=linspace(-pi/6,pi/6,3*n)

S = SpiroData()

for j in range(1):
    offset=np.random.randint(T1.n())
    first=np.random.randint(T1.n())
    for i in range(3): 
        S.add(triangles_on_frame(T1,skip=skip,scale=scale[::skip]*(1+i*3/10),oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                                pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                                arc_angle=arc_angle))

figure(S,'spacing','hot')

##

seed=655
np.random.seed(seed)

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=1
n=150
oa=pi/4
ao = 0
asym = 0
scale=5*d/(dmax-dmin) # * (1.0-abs(asym))

arc_angle=linspace(-pi/6,pi/6,3*n)

S = SpiroData()

for j in range(1):
    offset=np.random.randint(T1.n())
    first=np.random.randint(T1.n())
    for i in range(3): 
        S.add(triangles_on_frame(T1,skip=skip,scale=scale[::skip]*(1+i*2/10),oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                                pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                                arc_angle=arc_angle).rotate(i*pi/6))

figure(S,'spacing','inferno')

##

seed=552 
np.random.seed(seed)

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=1
n=150
oa=pi/2
ao = 0
asym = 0
scale=5*d/(dmax-dmin)

arc_angle_t=linspace(-pi/6,pi/6,3*n)

S=SpiroData()

for j in range(2):
    offset=np.random.randint(T1.n())
    first=np.random.randint(T1.n())
    for i in range(2): 
        S.add(triangles_on_frame(T1,skip=skip,scale=scale[::skip]*(1+(i+0.5)*2/10),oangle=oa,
                                 n=n,first=first,fh=0.5,fb=0.5,
                                 pts=500*def_factor,asym=asym,orient_follow=offset,orient=ao,
                                 arc_angle=arc_angle_t).rotate((i+0.5)*pi/6))

figure(S,'y-direction','bone')

##

seed=835 
np.random.seed(seed)

print(seed)

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)

skip=1
n=150
oa=pi/2
ao = 0 
asym = 0
scale=5

arc_angle_t=linspace(-pi/6,pi/6,3*n)
arc_angle_p=linspace(-pi/6,pi/6,4*n)

pts = np.round(linspace(500*def_factor,2*def_factor,3*n)).astype(int)

for j in range(1):
    offset=np.random.randint(T1.n())
    first=np.random.randint(T1.n())
    for i in range(3): 
        S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                                 first=first,fh=0.5,fb=0.5,
                                 pts=pts,asym=asym,orient_follow=offset,orient=ao,
                                 arc_angle=arc_angle_t).rotate(i*2*pi/3))

figure(S,'cycles',emerald_woman)

###

e=0.7
R=7
ppl=1000
a=circum(R1,semi_minor(R1,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

skip=1
n=T1.n()//skip//5
oa=pi/2
ao = linspace(0,pi,n)
asym = 0.3

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=0*(d-dmin)/(dmax-dmin)+4.0

arc_angle_p=[pi/20,pi/8,pi/20,pi/8]
pts = [500,50,500,50]

seed = 11
np.random.seed(seed)
offset=np.random.randint(T1.n())
first=np.random.randint(T1.n())

S = pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,
                  first=first,fh=0.5,fb=0.5,
                  pts=pts*def_factor,asym=asym,orient_follow=offset,orient=ao,
                  arc_angle=arc_angle_p)

figure(S,'cycles','autumn')
