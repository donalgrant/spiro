import sys
sys.path.append('../..')
import argparse

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_arcs import *
from spiro_string import *
from spiro_frame import *
from polygon import *
from Ring import *

import imageio.v2 as imageio
import glob

parser = argparse.ArgumentParser(description="Morph Examples")
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

filename='animate-image.png'

###

R1=5
ppl=300
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/3),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//skip
first=0 
offset=n//30
oa=pi/3

m=67 # n//4  # filesize constraint
ao = linspace(0,2*pi,m)
asym = linspace(0.0,0.3,m)
scale=2

cs = 'cycles'
my_cmap = emerald_woman

images=[]

for i in range(m):
    
    if i % 10 == 0:  print(i,m)

    S=pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                    pts=500*def_factor,asym=asym[i],orient_follow=offset,orient=ao[i]).rotate(i*pi/4/m)

    F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,
           save=True,limits=[-10,10,-10,10],transparent=False,filename=filename)

    images.append(imageio.imread(filename))

images.extend(np.flip(images,axis=0))
imageio.mimsave("animate_green_polygons.gif", images, duration=0.2, loop=0)

###

def_factor=1

ppl=1000

maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=ppl)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a/2,a),loops=1.0,inside=True,ppl=ppl)

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

images=[]

for offset in range(0,2*ns,2):
    k=1
    first1 = k*ns
    first2 = k*ns+offset
    if offset % 20 == 0:
        print(offset,first1,first2,n)
    S=frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,
                 scale=0.5,oangle=pi/2,fb=0.0,fh=0.0,asym=0,orient=pi/2,polyfunc=tcoords,
                 pts=pts,arc_angle=0,object=k,prot=0,vertex_order=None,
                 pin_to_frame1=True,autoscale=True,pinned_vertex=1)

    filename='animate-frame-pair.png'
    F.plot(S,color_scheme='width',cmap='hot_r',alpha=0.4,dot_size=.1,save=True,filename=filename,
          limits=[-35,35,-35,35],transparent=False)
    images.append(imageio.imread(filename))

imageio.mimsave('animate-frame-pair.gif',images,duration=0.06,loop=0)

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=5,circuits=1,ppl=1000)
S2 = S1.copy()

n = S2.n()
print(n)
nv = 60
v = linspace(0,nv-1,nv,dtype=int)
o = 0

pts = 600//nv

S = SpiroData()


fps = 10  # frames per second

images=[]

f0=0
for div in linspace(1,S2.n()-1,n//8,dtype=int):
    print(div)
    S=on_frame(S2,scale=8,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=div,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)
    
    filename='animate-ie-ellipse-01.png'
    
    F.plot(S,color_scheme='segment',cmap='pretty_reds',alpha=0.4,dot_size=.1,
           save=True,filename=filename,
           limits=[-35,35,-35,35],transparent=False)
    
    images.append(imageio.imread(filename))

images.extend(np.flip(images,axis=0))
imageio.mimsave('animate-ie-ellipse-01.gif',images,duration=1.0/fps,loop=0)

