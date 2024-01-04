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

import imageio.v2 as imageio
import glob

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

filename='animate-figure-3d.png'

###

e=0.0
R=7
ppl=1000

a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/6),ppl=ppl,loops=1,inside=True)

skip=3
n=120

scale=5
oa=pi/3
ao=0.0
asym=0
aa=pi/3
of=1
pts=[200,0,200]

S = SpiroData()

nr=6
for i in range(nr):
    first=i*T.n()//nr
    S.add(triangles_on_frame(T,first=first,skip=skip,scale=scale,oangle=oa,n=n,fh=0,fb=0,
                             asym=asym,orient_follow=1,orient=ao,arc_angle=aa,pts=pts))

my_cmap='turbo'

xscale=max(S.x)-min(S.x)

images=[]

for theta in linspace(0,2*pi,96):
    
    xyz=rotY(S.xyp(scale=xscale),theta)
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()
    F.plot(U.set_array(x,y,S.p,S.t,S.o,S.s),
           color_scheme='cycles',cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=0.1,save=True,
           limits=[-15,15,-15,15],transparent=False,filename=filename)

    images.append(imageio.imread(filename))
    
for theta in linspace(0,2*pi,96):
    
    xyz=rotX(S.xyp(scale=xscale),theta)
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()
    F.plot(U.set_array(x,y,S.p,S.t,S.o,S.s),
           color_scheme='cycles',cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=0.1,save=True,
           limits=[-15,15,-15,15],transparent=False,filename=filename)

    images.append(imageio.imread(filename))

    
imageio.mimsave("animate_rot-triangle_sets-p.gif", images, duration=0.1, loop=0)

###

# demonstration of rotating, zooming in, and showing the spirograph frame, while evolving

e=0.0
R=7
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/2.5),ppl=ppl,loops=1,inside=True)

my_cmap='turbo'
cs = 'cycles'

skip=1
n=40

scale=3
oa=pi/3
ao=0.0
asym=0
of=1
pts=[200,0,200]

nr=120

theta = linspace(0,2*pi,nr)
aa = linspace(0,pi/2,nr)
lmax = append(linspace(25,3,nr//2),linspace(3,25,nr//2))

images=[]

for i in range(nr):
    if i%10==0:  print(i)
    
    first=i*T.n()//nr
    S=triangles_on_frame(T,first=first,skip=skip,scale=scale,oangle=oa,n=n,fh=0,fb=0,
                         asym=asym,orient_follow=1,orient=ao,arc_angle=aa[i],pts=pts)

    xscale=max(S.x)-min(S.x)

    xyz=rotY(S.xyl(scale=xscale/4),theta[i])
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()

    l=lmax[i]
    ds = 62.5/(l*l)
    
    F.plot(U.set_array(x,y,S.p,S.t,S.o,S.s),color_scheme=cs,cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=ds,save=False,
           limits=[-l,l,-l,l],transparent=False,filename=filename)

    images.append(imageio.imread(filename))
    
    v = rotY(T.xyl(scale=1.0),theta[i])
    x = v[:,0]
    y = v[:,1]
    z = v[:,2]

    U = SpiroData()

    F.plot(U.set_array(x,y,T.p,T.t,S.o,S.s),
           color_scheme=cs,cmap='pale_pink',alpha=.2,fig_dim=fd,dot_size=ds*10,save=True,
           limits=[-l,l,-l,l],transparent=False,new_fig=False,filename=filename)

    images.append(imageio.imread(filename))
    
imageio.mimsave("animate_evolve-zoom-w-frame.gif", images, duration=0.2, loop=0)
