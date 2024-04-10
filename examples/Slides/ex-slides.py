import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *

parser = argparse.ArgumentParser(description="Slides Examples")
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

F._figname='Slides-'

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


S = SpiroData()

###

S.reset()
cs='time'
c='autumn'
a=9.0
bv=[0.9*a-0.03*a*i for i in range(10)]
for i in range(10):
    S.add(spiro(Ring(2.0),Wheel(a,bv[i]),9,slide=1.5))
figure(S,cs,c)

###

S.reset()
cs='width'
ring = Ring(100)
F.plot(spiro(ring,Wheel(-30,31),loops=20,
             slide=array([ 0.2 + sin(t) for t in linspace(0,2*pi*2,1000)])),
       cmap='Blues',color_scheme=cs)
F.plot(spiro(ring,Wheel(30,25), 20,
             slide=array([ 0.1 + cos(t) for t in linspace(0,2*pi*2,1000)])),
       cmap='Reds',color_scheme=cs,new_fig=False)
F.save_fig()

###

S.reset()
cs='time'
ring = Ring(100)
ppl=5000
F.plot(spiro(ring,Wheel(-30,31),100,ppl=ppl,
             slide=array([ 0.2 +  5*sin(t) for t in linspace(0,5,ppl)])),
       cmap='Blues',color_scheme=cs,alpha=0.4,dot_size=0.1)
ppl*=2
F.plot(spiro(ring,Wheel(30,25),50,ppl=ppl,
             slide=array([ 1+ 20*cos(t) for t in linspace(0,10,ppl)])),
       cmap='Reds',color_scheme=cs,new_fig=False,alpha=0.4,dot_size=0.1)
F.save_fig()

###

S.reset()
w=Ellipse(8,0.9,11,0,pi/4)
l=20
S.add(eIe(wheel=w,slide=-0.5,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'cycles','autumn')

###

S.reset()
w=Ellipse(10,0.9,11,0,pi/4)
l=20
S.add(eIe(wheel=w,slide=-0.5,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'l-waves','autumn')

###

S.reset()
w=Ellipse(9,0.9,11,0,pi/4)
l=20
S.add(eIe(wheel=w,slide=-0.5,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'t-waves','autumn')

###

S.reset()
w=Ellipse(9,0.9,17,0,pi/5)
l=20
S.add(eIe(wheel=w,slide=0.1,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'l-waves','ocean')

###

S.reset()
w=Ellipse(9,0.9,17,0,pi/5)
l=20
S.add(eIe(wheel=w,slide=2.0,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'s-ripples','ocean')

###

S.reset()
w=Ellipse(9,0.3,17,0,pi/5)
l=20
S.add(eIe(wheel=w,slide=2.0,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'cycles','turbo')

###

S.reset()
w=Ellipse(9,0.6,17,0,pi/5)
l=20
S.add(eIe(wheel=w,slide=2.0,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'cycles','jet')

###

S.reset()
w=Ellipse(9,0.6,17,0,pi/5)
l=40
S.add(eIe(wheel=w,slide=1.7,inside=True,loops=l/0.5,ppl=10000))
S.rotate(pi/3)
figure(S,'cycles','inferno')

###

S.reset()
a=9.0
nc=10
bv=[0.7*a-0.03*a*i for i in range(nc)]
F.text_color='white'
for sl in linspace(1.5,2.0,1):
    S.reset()
    for i in range(nc):
        S.add(spiro(Ring(17),Wheel(a,bv[i]),18,slide=sl))
    for cs in ['length','l-waves','radial','time','t-waves','cycles']:
        figure(S,cs,'viridis')
