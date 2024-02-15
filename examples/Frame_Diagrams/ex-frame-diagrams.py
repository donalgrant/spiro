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

n_positions=20
T=cIc(Ring(7),W0,ppl=n_positions,loops=1)

##  varying triangle arc-angle, fixed orientation, centered, no asym

S = SpiroData()

parm=linspace(-pi,pi,n_positions-1)

for i in range(n_positions-1):
    scale=1
    oa=pi/3
    ao=0.0
    asym=0
    arc_angle=parm[i]
    of=None
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0.5,fb=0.5,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

##  varying open-angle, fixed orientation, vertex on origin, no asym, straight sides

S = SpiroData()

parm=linspace(pi/n_positions,pi*(n_positions-1)/n_positions,n_positions-1)

for i in range(n_positions-1):
    scale=1
    oa=parm[i]
    ao=0.0
    asym=0
    arc_angle=0
    of=None
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=0,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

##  fixed open-angle, fixed orientation, vertex on origin, varying asym, three-different arc'd sides

S = SpiroData()

parm=linspace(-0.9,0.9,n_positions-1)

for i in range(n_positions-1):
    scale=1
    oa=pi/3
    ao=0.0
    asym=parm[i]
    arc_angle=[pi/2,0,-pi/2]
    of=None
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=0,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

##  fixed open-angle, absolute orientation varying, vertex on origin, no asym, three-different arc'd sides one fading

S = SpiroData()

for i in range(n_positions-1):
    scale=1
    oa=pi/3
    ao=pi/3*i/(n_positions-1)
    asym=0
    arc_angle=0
    of=None
    pts=[30,30*i//(n_positions-1)+2,0]

    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=0,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle,pts=pts))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

##  fixed open-angle, neighbor orientation, vertex varying, no asym, straight sides

S = SpiroData()

parm=linspace(-1.0,1.0,n_positions-1)

for i in range(n_positions-1):
    scale=1
    oa=pi/3
    ao=0
    asym=0
    arc_angle=0
    of=1
    pts=50
    fh=parm[i]
    fb=0.5
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle,pts=pts))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

##  fixed open-angle, orientation towards 1/3 around ring, vertex fixed, no asym, straight sides

S = SpiroData()

parm=linspace(-1.0,1.0,n_positions-1)

for i in range(n_positions-1):
    scale=1
    oa=pi/2
    ao=0
    asym=0
    arc_angle=0
    of=T.n()//3
    pts=50
    fh=0.0
    fb=0.0
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle,pts=pts))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

##  three objects, all fixed open-angle, no asym, straight sides;
# red:  orientation towards neighbor, vertex moving on baseline, increasing size around the frame
# green:  orientation towards neighbor with increasing offset from 0 to pi/2 around ring, vertex just below frame,
#         scaled as red
# cyan: fixed small scale, two sides (second side of triangle has no points), vertext  well below frame point,
#       rotated by 2 pi around frame (orientation absolute)

S = SpiroData()

for i in range(n_positions-1):
    scale=0.5+i/(n_positions-1)*0.5
    oa=pi/2
    ao=0
    asym=0
    arc_angle=0
    of=1
    pts=50
    fh=0.0
    fb=0.5+0.5*cos(2*pi*i/(n_positions-1))
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle,pts=pts))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=False,color_dither=0.0,new_fig=False)

S.reset()

for i in range(n_positions-1):
    scale=0.5+i/(n_positions-1)*0.5
    ao=pi/2*i/(n_positions-1)
    fh=0.1 # sin(2*pi*i/(n_positions-1))+0.1
    fb=0.0 # 0.5+0.5*cos(2*pi*i/(n_positions-1))+0.1
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle,pts=pts))

F.plot(S,color_scheme='green',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=False,color_dither=0.0,new_fig=False)

S.reset()

for i in range(n_positions-1):
    scale=0.3
    ao=2*pi*i/(n_positions-1)
    fh=2 # sin(2*pi*i/(n_positions-1))+0.1
    fb=0.0 # 0.5+0.5*cos(2*pi*i/(n_positions-1))+0.1
    pts=[50,0,50]
    S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                             asym=asym,orient_follow=None,orient=ao,
                             arc_angle=arc_angle,pts=pts))

F.plot(S,color_scheme='cyan',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

##  varying parallelogram opening angle, fixed orientation, centered, no asym;
#   red:  unvarying fixed orientation, centered on frame
#   green: is nearest neighbor orientation, vertex on frame

S = SpiroData()

parm=linspace(pi/15,pi-pi/15,n_positions-1)

scale=1
ao=0.0
asym=0.0
arc_angle=0
of=None

for i in range(n_positions-1):

    oa=parm[i]

    S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,fh=0.5,fb=0.5,n=1,
                             asym=asym,orient_follow=of,orient=ao,
                             arc_angle=arc_angle))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=False,color_dither=0.0,new_fig=False)

S.reset()
for i in range(n_positions-1):
    oa=parm[i]
    S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=0,n=1,
                             asym=asym,orient_follow=1,orient=ao,
                             arc_angle=arc_angle))
    
F.plot(S,color_scheme='green',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

## 
#   red:  varying assymetry nearest neighbor orientation, vertex on frame, straight sides, fixed open angle
#   green: fixed orientation, no asymmetry, varying arc radius, fixed open angle, "centered" on frame
#   (centered means vertex at center of base and center of "height" -- not actual center of figure.)

S = SpiroData()

parm=linspace(-0.6,0.6,n_positions-1)

scale=0.5
ao=0.0
oa=pi/3
asym=0.0
arc_angle=0

for i in range(n_positions-1):

    asym=parm[i]

    S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,n=1,fb=0,fh=0,
                             asym=asym,orient_follow=1,orient=ao,
                             arc_angle=arc_angle))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=False,color_dither=0.0,new_fig=False)

S.reset()
parm=linspace(-pi,pi,n_positions-1)

scale=1.0

for i in range(n_positions-1):
    asym=0
    oa=pi/3
    arc_angle=parm[i]
    S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,n=1,
                             asym=asym,orient_follow=None,orient=ao,
                             arc_angle=arc_angle))
    
F.plot(S,color_scheme='green',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

## 
#   red:  no asym; pts fade between both pairs of parallel sides; rotating orientation, straight sides, vertex on frame

S = SpiroData()

scale=1.0
oa=pi/3
asym=0.0
arc_angle=0

for i in range(n_positions-1):
    ao=2*pi*i/(n_positions-1)
    p1 = 25+int(25*sin(2*pi*i/(n_positions-1)))
    p2 = 25+int(25*cos(2*pi*i/(n_positions-1)))
    pts=[p1,p2,50-p1,50-p2]

    S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,n=1,fb=0,fh=0,
                             asym=asym,orient_follow=None,orient=ao,pts=pts,
                             arc_angle=arc_angle))

F.plot(T,no_frame=False,dot_size=20,cmap='pale_pink')
F.plot(S,color_scheme='red',cmap='turbo',alpha=.4,fig_dim=fd,dot_size=1,save=True,color_dither=0.0,new_fig=False)

###  Composite diagram

'''
S = SpiroData()
n_positions=25
T=cIc(Ring(9),W0,ppl=n_positions,loops=1,inside=True)
T.add(cIc(Ring(6),W0,ppl=n_positions//2+1,loops=1,inside=True))
T.add(cIc(Ring(3),W0,ppl=n_positions//4+1,loops=1,inside=True))

def_factor=10
scale=0.5
nr=10
oa=pi/3 # 2*pi/nr
ao=0 # linspace(0,2*pi,n_positions)
asym=0.
arc_angle=0
of=1
pts=[50,50,50,50]*def_factor
fh=0.
fb=0.
i=1
for nr in range(1,6):
    for j in range(nr):
        S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                                asym=asym,orient_follow=of,orient=ao,
                                arc_angle=arc_angle,pts=pts,object=i,prot=-2*j*pi/nr))
    i += 1
    
for nr in range(1,6):
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                            asym=asym,orient_follow=of,orient=ao,
                            arc_angle=arc_angle,pts=pts,object=i,prot=-2*j*pi/nr))
    i += 1
    
for nr in range(3,6):
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                            asym=asym,orient_follow=of,orient=ao,
                            arc_angle=pi/nr,pts=pts,object=i,prot=-2*j*pi/nr))
    i += 1
    
scale=1/2
oa=pi/2
asym=0
of=1
ao=0
aa=0
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=1/scale/sqrt(2),n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=pi/4))
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=1/scale/sqrt(2),fb=0,n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=-pi/4))
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=-1/scale/sqrt(2),fb=0,n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=3*pi/4))
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=-1/scale/sqrt(2),n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=-3*pi/4))
i += 1

for j in range(5,9):
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1

for j in linspace(pi/6,pi/1.5,4):
    S.add(on_frame(T,scale=1,oangle=6,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=-j,pts=pts,object=4,prot=0))
    i += 1

for j in range(3,6):
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=-pi/2,pts=pts,object=4,prot=0))
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=pi/2,pts=pts,object=4,prot=0))
    i += 1
    
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=-pi,pts=pts,object=4,prot=0))
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=pi,pts=pts,object=4,prot=0))
    i += 1

for j in range(3,7):
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0.5,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1

for j in linspace(0.2,0.8,4):
    S.add(on_frame(T,scale=1,oangle=4,first=i,fh=0,fb=0,n=1,
                   asym=j,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1


i += 1
for j in linspace(-0.5,-0.8,2):
    S.add(on_frame(T,scale=1,oangle=4,first=i,fh=0,fb=0,n=1,
                   asym=j,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1
    
for j in linspace(-0.5,-0.8,2):
    S.add(on_frame(T,scale=1,oangle=6,first=i,fh=0,fb=0,n=1,
                   asym=j,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1
    
for j in [-pi/2,pi/2]:
    S.add(on_frame(T,scale=1,oangle=4,first=i,fh=0,fb=0,n=1,
                   asym=-0.5,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=j,pts=pts,object=4,prot=0))
    i += 1

'''

F = SpiroFig()
S = SpiroData()
n_positions=25
T=cIc(Ring(9),W0,ppl=n_positions,loops=1,inside=True)
T.add(cIc(Ring(6),W0,ppl=n_positions//2+1,loops=1,inside=True))
T.add(cIc(Ring(3),W0,ppl=n_positions//4+1,loops=1,inside=True))

hd=0
fd = 10*(1+2*hd) # figure dimensions

def_factor=10
scale=0.5
nr=10
oa=pi/3 # 2*pi/nr
ao=0 # linspace(0,2*pi,n_positions)
asym=0.
arc_angle=0
of=1
pts=[50,50,50,50]*def_factor
fh=0.
fb=0.
i=1
for nr in range(1,6):
    for j in range(nr):
        S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                                asym=asym,orient_follow=of,orient=ao,
                                arc_angle=arc_angle,pts=pts,object=i,prot=-2*j*pi/nr))
    i += 1
    
for nr in range(1,6):
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                            asym=asym,orient_follow=of,orient=ao,
                            arc_angle=arc_angle,pts=pts,object=i,prot=-2*j*pi/nr))
    i += 1
    
for nr in range(3,6):
    for j in range(nr):
        S.add(pars_on_frame(T,scale=scale,oangle=oa,first=i,fh=fh,fb=fb,n=1,
                            asym=asym,orient_follow=of,orient=ao,
                            arc_angle=pi/nr,pts=pts,object=i,prot=-2*j*pi/nr))
    i += 1
    
scale=1/2
oa=pi/2
asym=0
of=1
ao=0
aa=0
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=1/scale/sqrt(2),n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=pi/4))
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=1/scale/sqrt(2),fb=0,n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=-pi/4))
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=-1/scale/sqrt(2),fb=0,n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=3*pi/4))
S.add(triangles_on_frame(T,scale=scale,oangle=oa,first=i,fh=0,fb=-1/scale/sqrt(2),n=1,
                    asym=asym,orient_follow=of,orient=ao,
                    arc_angle=aa,pts=pts,object=4,prot=-3*pi/4))
i += 1

for j in range(5,9):
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1

for j in linspace(pi/6,pi/1.5,4):
    S.add(on_frame(T,scale=1,oangle=6,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=-j,pts=pts,object=4,prot=0))
    i += 1

for j in range(3,6):
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=-pi/2,pts=pts,object=4,prot=0))
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=pi/2,pts=pts,object=4,prot=0))
    i += 1
    
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=-pi,pts=pts,object=4,prot=0))
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
                   arc_angle=pi,pts=pts,object=4,prot=0))
    i += 1

for j in range(3,7):
    S.add(on_frame(T,scale=1,oangle=j,first=i,fh=0,fb=0,n=1,
                   asym=0.5,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1

for j in linspace(0.2,0.8,4):
    S.add(on_frame(T,scale=1,oangle=4,first=i,fh=0,fb=0,n=1,
                   asym=j,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1

i += 1
for j in linspace(-0.5,-0.8,2):
    S.add(on_frame(T,scale=1,oangle=4,first=i,fh=0,fb=0,n=1,
                   asym=j,orient_follow=of,orient=ao, polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=4,prot=0))
    i += 1
    
S.add(on_frame(T,scale=1,oangle=6,first=i,fh=0,fb=0,n=1,
               asym=-0.8,orient_follow=of,orient=ao, polyfunc=nstar_coords,
               arc_angle=aa,pts=pts,object=4,prot=0))
i += 1
    
S.add(on_frame(T,scale=1,oangle=4,first=i,fh=0,fb=0,n=1,
               asym=-0.5,orient_follow=of,orient=ao, polyfunc=nstar_coords,
               arc_angle=-pi/2,pts=pts,object=4,prot=0))
i += 1
    
S.add(on_frame(T,scale=1,oangle=7,first=i,fh=0,fb=0,n=1,
               asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
               vertex_order=[0,3,6,2,5,1,4,0],
               arc_angle=0,pts=pts,object=4,prot=0))
i += 1
    
S.add(on_frame(T,scale=1,oangle=7,first=i,fh=0,fb=0,n=1,
               asym=0,orient_follow=of,orient=ao, polyfunc=ngon_coords,
               vertex_order=[0,3,6,2,5,1,4,0,2,4,6,1,3,5,0,1,2,3,4,5,6,0],
               arc_angle=-pi/6,pts=pts,object=4,prot=0))
i += 1
    
F.plot(T,no_frame=False,dot_size=20,color_scheme='cyan',cmap='turbo')
F.plot(S,color_scheme='orange',cmap='turbo',alpha=1,fig_dim=fd,dot_size=.1,new_fig=False)
F.save_fig(filename='composite-diagram.png')
