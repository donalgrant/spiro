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

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None,color_dither=0.0):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,color_dither=color_dither)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,color_dither=color_dither)

###

e=0.1
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/4,a*0.6),ppl=ppl,loops=1,inside=True).rotate(pi/4).subsample(1)

oa=pi/4
ao = pi/4 

scale=3

arc_angle_t=[pi/6,pi/8,pi/6]
pts = [500,0,500]
offset=20

S = triangles_on_frame(T1,scale=scale,oangle=oa,n=T1.n(),
                       pts=pts*def_factor,orient_follow=offset,orient=ao,
                       arc_angle=arc_angle_t)

figure(S,'cycles','pretty_blues')

###

e=0.0
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/5),ppl=ppl,loops=1,inside=True).rotate(pi/4)

pts = [500,0,500]

offset=1 # np.random.randint(T1.n())

S = triangles_on_frame(T1,scale=3,oangle=pi/3,pts=pts*def_factor,orient_follow=1)

figure(S,'x-direction','hot')

###

e=0.0
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/8),ppl=ppl,loops=1,inside=False)

n=T1.n()//9
oa=pi/3

asym = 0.4

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=5
ao=pi/2*(d-dmin)/(dmax-dmin)

arc_angle_t=0 #[pi/6,pi/8,pi/6]

pts = [500,0,500]

S = SpiroData()
n_swoops=6
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,scale=scale,oangle=oa,n=n-1,first=first,
                             pts=pts*def_factor,asym=asym,orient_follow=1))

figure(S,'direction','turbo')

###

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True)

skip=2
n=T1.n()//skip//3

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
ao=pi/2*(d-dmin)/(dmax-dmin)

oa=pi/3
asym=0.4
scale=5

arc_angle_t=[-pi/3,0,-pi/3]

pts = [500,0,500]

my_cmap='Reds'

S = SpiroData()
n_swoops=3
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n-1,
                      first=first,fh=0.5,fb=0.5,
                      pts=pts*def_factor,asym=asym,orient_follow=1,orient=ao,
                      arc_angle=arc_angle_t))

figure(S,'cycles','Reds')

##

skip=2
n=T1.n()//skip//18

d = T1.neighbor_distances()
dmax=max(d)
dmin=min(d)
scale=5
ao=pi/2*(d-dmin)/(dmax-dmin)

pts = [0,500,500]

my_cmap='Oranges'

offset=1 # np.random.randint(T1.n())

S = SpiroData()
n_swoops=12
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=pi/3,n=n-1,orient=ao,
                             first=first,pts=pts*def_factor,orient_follow=1,arc_angle=pi/2))

figure(S,'cycles','Oranges')

###

e=0.0
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/6),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//skip//18

ao = linspace(0,pi/2,n)+pi/3 # T1.polars()+pi/2 # linspace(0,pi/4,n) # linspace(0,4*pi,n)

pts = [0,500,500]

S = SpiroData()
n_swoops=12
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=3,oangle=pi/3,n=n-1,first=first,
                             pts=pts*def_factor,asym=0.3,orient_follow=1,orient=ao,arc_angle=pi/5))

figure(S,'cycles','autumn')

##

skip=2
n=T1.n()//skip//18

scale=8

pts = [500,500,0]

S = SpiroData()
n_swoops=12
for i in range(n_swoops):
    first=T1.n()*i//n_swoops
    S.add(triangles_on_frame(T1,skip=skip,scale=scale,oangle=pi/3,n=n-1,
                      first=first,fh=0.5,fb=0.5,
                      pts=pts*def_factor,asym=0.8,orient_follow=T1.n()//2,arc_angle=pi/5))

figure(S,'y-direction','bone')

###

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T1 = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/6),ppl=ppl,loops=1,inside=True)

skip=2
n=T1.n()//skip

pts = [500,500,0]

my_cmap=pretty_blues

offset=1 # np.random.randint(T1.n())

S = triangles_on_frame(T1,skip=skip,scale=3,oangle=pi/3,n=n-1,
                       pts=pts*def_factor,orient_follow=1,arc_angle=-pi/5)

figure(S,'cycles',pretty_blues,color_dither=0.15)

##

n=T1.n()

ao = linspace(0,pi/9,n) # T1.polars()+pi/2 # linspace(0,pi/4,n) # linspace(0,4*pi,n)

pts=[]
for j in range(n):  pts.extend([0,252+int(250*sin(6*pi*j/n+pi/3)),0])

my_cmap=emerald_woman

S = triangles_on_frame(T1,scale=5,oangle=pi/3,n=n-1,
                       pts=pts*def_factor,asym=0.5,orient_follow=1,orient=ao,
                       arc_angle=pi/5)

figure(S,'cycles','emerald_woman',color_dither=0.05)

