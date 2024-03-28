import sys
sys.path.append('../..')
import argparse

import numpy as np

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

import imageio.v2 as imageio
import glob

parser = argparse.ArgumentParser(description="Frame Pair A Examples")
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

F._figname='Sliding_Frame_Pairs-'

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

### original frames

pplf=2
ppl1=500
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf))
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf))
T3 = frame_pair(T1,T2,skip1=1,skip2=1,first1=0,first2=0,polyfunc=tcoords,pin_to_frame1=0.5,frame_only=True)

F.plot(T1,color_scheme='cyan',dot_size=1.0,no_frame=False)
F.plot(T2,color_scheme='orange',dot_size=1.0,new_fig=False)
F.plot(T3,color_scheme='white',dot_size=1.0,new_fig=False)

F.save_fig()

### frames moved and rotated

pplf=2
ppl1=500
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)
T3 = frame_pair(T1,T2,skip1=1,skip2=1,first1=0,first2=0,polyfunc=tcoords,pin_to_frame1=0.5,frame_only=True)

F.plot(T1,color_scheme='cyan',dot_size=1.0,no_frame=False)
F.plot(T2,color_scheme='orange',dot_size=1.0,new_fig=False)
F.plot(T3,color_scheme='white',dot_size=1.0,new_fig=False)

F.save_fig()

### reduce sampling for first frame

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

T3 = frame_pair(T1,T2,skip1=1,skip2=1,first1=0,first2=0,polyfunc=tcoords,pin_to_frame1=0.5,frame_only=True)

F.plot(T1,color_scheme='cyan',dot_size=1.0,no_frame=False)
F.plot(T2,color_scheme='orange',dot_size=1.0,new_fig=False)
F.plot(T3,color_scheme='white',dot_size=1.0,new_fig=False)

F.save_fig()

### continue moving around both frames until the new frame returns to the start position

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

n  = np.lcm(T1.n(),T2.n())

T3 = frame_pair(T1,T2,skip1=1,skip2=1,first1=0,first2=0,polyfunc=tcoords,pin_to_frame1=0.5,frame_only=True)
T4 = frame_pair(T1,T2,skip1=1,skip2=1,first1=T2.n(),first2=0,n2=n-T2.n(),
                polyfunc=tcoords,pin_to_frame1=0.5,frame_only=True)

F.plot(T3,color_scheme='white',dot_size=1.0,no_frame=False)
F.plot(T4,color_scheme='red',dot_size=1.0,new_fig=False)

F.save_fig()

### divide new frame into four parts

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = np.lcm(T1.n(),T2.n())//nk # T2.n()//nk 

T3 = SpiroData()

for k in range(nk):
    first1 = k*ns
    first2 = k*ns
    T3.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                      polyfunc=tcoords,pin_to_frame1=0.5,frame_only=True,object=k))


F.plot(T3,color_scheme='object',cmap='Set1',dot_size=1.0)

F.save_fig()

### sinusoidally move the pin coord between the two frames, rather than just midway between them

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

npts=150*def_factor
pts = npts

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = np.lcm(T1.n(),T2.n())//nk # T2.n()//nk 

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

T3 = SpiroData()

for k in range(nk):
    first1 = k*ns
    first2 = k*ns
    T3.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                      polyfunc=tcoords,pin_to_frame1=ptf,frame_only=True,object=k))


F.plot(T3,color_scheme='object',cmap='Set1',dot_size=1.0)

F.save_fig()

### shorten the segments to only use the first portion of the frame

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

npts=150*def_factor
pts = npts

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = np.lcm(T1.n(),T2.n())//nk # T2.n()//nk 

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

T3 = SpiroData()

for k in range(nk):
    first1 = k*ns
    first2 = k*ns
    T3.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                      polyfunc=tcoords,pin_to_frame1=ptf,frame_only=True,object=k))


F.plot(T3,color_scheme='object',cmap='Set1',dot_size=1.0)

F.save_fig()

### draw triangles on the new frame, pinned between original and new frame

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

npts=150*def_factor
pts = npts

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

T3 = SpiroData()

S = SpiroData()

for k in range(nk):
    first1 = k*ns
    first2 = k*ns
    T3.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                      polyfunc=tcoords,pin_to_frame1=ptf,frame_only=True,object=k))
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     oangle=pi/3,polyfunc=tcoords,
                     pts=pts,arc_angle=0,object=k,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1))

F.plot(S,color_scheme='object',cmap='Set1',dot_size=0.1,alpha=0.4)
F.plot(T3,color_scheme='object',cmap='Set1',dot_size=1.0,new_fig=False)
F.plot(T1,color_scheme='cyan',dot_size=1.0,new_fig=False)

F.save_fig()

### Select just the last of the four parts

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

npts=150*def_factor
pts = npts

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

T3 = SpiroData()

S = SpiroData()

for k in range(3,4):
    first1 = k*ns
    first2 = k*ns
    T3.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                      polyfunc=tcoords,pin_to_frame1=ptf,frame_only=True,object=k))
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     oangle=pi/3,polyfunc=tcoords,
                     pts=pts,arc_angle=0,object=k,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1))

F.plot(S,color_scheme='object',cmap='Set1',dot_size=0.1,alpha=0.4)
F.plot(T3,color_scheme='white',cmap='Set1',dot_size=1.0,new_fig=False)
F.plot(T1,color_scheme='cyan',dot_size=1.0,new_fig=False)

F.save_fig()

### give the triangles arc'd sides

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

npts=150*def_factor
pts = npts

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

T3 = SpiroData()

S = SpiroData()

for k in range(3,4):
    first1 = k*ns
    first2 = k*ns
    T3.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                      polyfunc=tcoords,pin_to_frame1=ptf,frame_only=True,object=k))
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     oangle=pi/3,polyfunc=tcoords,
                     pts=pts,arc_angle=pi/4,object=k,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1))

F.plot(S,color_scheme='object',cmap='Set1',dot_size=0.1,alpha=0.4)
F.plot(T3,color_scheme='white',cmap='Set1',dot_size=1.0,new_fig=False)
F.plot(T1,color_scheme='cyan',dot_size=1.0,new_fig=False)

F.save_fig()

### choose a color map and scheme

F = SpiroFig()
def_factor=1

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

npts=150*def_factor
pts = npts

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

S = SpiroData()

for k in range(3,4):
    first1 = k*ns
    first2 = k*ns
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     oangle=pi/3,polyfunc=tcoords,
                     pts=pts,arc_angle=pi/4,object=k,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1))

images=[]

cslist = ['spacing','direction','time','cycles','phase','length',
           'lengths','flengths','fradii','fpolars','width','fwidth',
           'fcdist3','cdist3','fcdirs3','cdirs3',
           'l-waves','t-waves','x-direction','y-direction','object','segment']
clist = ['Blues','Reds','Greens','Oranges','OrRd',
         'cmap1','cmap2','cmap3','copper','bone','autumn','Wistia','twilight','turbo','ocean',
         'pretty_blues','emerald_woman','pretty_reds','pale_pink','hot','gist_heat','inferno',
         'hot_r','gist_heat_r','inferno_r']

for cmap in clist:
    for cs in cslist:
        filename='Movement_and_Grace-color_choice.png'
        print(cmap,' - ',cs)
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=0.4,dot_size=0.1,
               save=True,filename=filename,transparent=False)
    
        images.append(imageio.imread(filename))

imageio.mimsave('Movement_and_Grace-color_choice.gif',images,duration=0.25,loop=0)

### Movement and Grace

pplf=2
ppl1=400
ppl2=500
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=int(ppl1*pplf)).rotate(pi/6)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a*3/4,a),loops=1.0,inside=True,ppl=int(ppl2*pplf)).move(20,0)

S = SpiroData()

npts=150*def_factor

nk=4
gs=0
n  = np.lcm(T1.n(),T2.n())//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
aa = pi/4

ptf = array([ 0.5+0.6*cos(6*pi*j/n) for j in range(n) ])

start=int(0.0*ns)
offset = int(0.0*ns)

shift = 0.0 

size = 1.0 

o = 3
for k in range(o,o+1):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 0 

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                     scale=size,oangle=oa,fb=shift,fh=shift,asym=0.0,orient=ao,polyfunc=tcoords,
                     pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                     pin_to_frame1=ptf,autoscale=True,pinned_vertex=1,show_side=array([1,1,1])))

figure(S,'fcdist3','gist_heat_r')
