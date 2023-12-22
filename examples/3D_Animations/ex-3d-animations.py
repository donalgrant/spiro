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

import imageio
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

###

e=0.0
R=7
ppl=1000

#T1 = spiro_line(R,Wheel(3*R/(2*pi)/4,R/5),loops=3,fold=True,invert=False)
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

for theta in linspace(0,2*pi,96):
    
    xyz=rotY(S.xyp(scale=xscale),theta)
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()
    F.plot(U.set_array(x,y,S.p,S.t),color_scheme='cycles',cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=0.1,save=True,
           limits=[-15,15,-15,15],transparent=False)

for theta in linspace(0,2*pi,96):
    
    xyz=rotX(S.xyp(scale=xscale),theta)
    x = xyz[:,0]
    y = xyz[:,1]
    z = xyz[:,2]

    U = SpiroData()
    F.plot(U.set_array(x,y,S.p,S.t),color_scheme='cycles',cmap=my_cmap,alpha=.4,fig_dim=fd,dot_size=0.1,save=True,
           limits=[-15,15,-15,15],transparent=False)

import imageio
import glob

images=[]

for image in sorted(glob.glob("Figure-*.png")):
    images.append(imageio.imread(image))

for image in sorted(glob.glob("Figure-*.png"),reverse=True):
    images.append(imageio.imread(image))
    
imageio.mimsave("animate_rot-triangle_sets-p.gif", images, duration=0.1, loop=0)
