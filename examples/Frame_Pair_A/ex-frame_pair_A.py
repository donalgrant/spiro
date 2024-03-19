import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

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

F._figname='Frame_Pair_A-'

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

ppl=1000

maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=ppl)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a/2,a),loops=1.0,inside=True,ppl=ppl)

S = SpiroData()

npts=200*def_factor

S =  frame_pair(T1,T2,skip1=1,skip2=1,first1=0,first2=0,
               scale=1,oangle=pi/3,fb=0.0,fh=0.0,asym=0,orient=0,polyfunc=tcoords,  # tcoords or pcoords
               pts=npts,arc_angle=0,object=linspace(0,T2.n(),T2.n()),prot=0,vertex_order=None,
               pin_to_frame1=1.0,autoscale=True,pinned_vertex=1)

figure(S,'fradii','emerald_woman')


##

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

for k in range(nk):
    first1 = k*ns
    first2 = k*ns+ns//4

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,
                       scale=0.5,oangle=pi/2,fb=0.0,fh=0.0,asym=0,orient=pi/2,polyfunc=tcoords, 
                       pts=pts,arc_angle=0,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=1.0,autoscale=True,pinned_vertex=1))

figure(S,'width','hot_r')

##

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)//2
ns = T2.n()//nk 

pts = npts

oa = array([ pi/2 + 0.7*pi/2*cos(2*pi*j/n) for j in range(n) ])

start=ns

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+ns+start
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=1,oangle=oa,fb=0.0,fh=0.0,asym=0.3,orient=pi/2,polyfunc=tcoords,
                       pts=pts,arc_angle=0,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=1.0,autoscale=True,pinned_vertex=1))

figure(S,'time','autumn')

##

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)//2
ns = T2.n()//nk 

pts = npts

oa = array([ pi/2 + 0.7*pi/2*cos(2*pi*j/n) for j in range(n) ])

start=ns

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+ns//2+start
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=1,oangle=oa,fb=0.3,fh=0.3,asym=-0.3,orient=pi/2,polyfunc=tcoords,
                       pts=pts,arc_angle=0,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=1.0,autoscale=True,pinned_vertex=1))

figure(S,'time','pretty_reds')

##

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
ao = linspace(0,2*pi,n)
aa = -2*pi/3

start=ns

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+ns//2+start
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=1,oangle=oa,fb=0.,fh=0.,asym=0.,orient=oa,polyfunc=tcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=0.0,autoscale=True,pinned_vertex=2))

figure(S,'time','turbo')

###


ppl=3000
maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=ppl)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a/2,a),loops=1.0,inside=True,ppl=ppl)

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)//2
ns = T2.n()//nk 

pts = npts

oa = pi/3
ao = linspace(0,2*pi,n)
aa = pi/3

start=3*ns//2

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+ns+start
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=1,oangle=oa,fb=0.,fh=0.,asym=0.,orient=oa,polyfunc=tcoords,
                       pts=[0,0,pts],arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=0.0,autoscale=True,pinned_vertex=1))

figure(S,'width','gist_heat_r')

###

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
n  = T2.n()//(nk+gs)//3
ns = T2.n()//nk 

pts = npts

oa = pi/4
ao = linspace(0,-pi,n)
aa = 0

start=0
offset = ns//2

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=1,oangle=oa,fb=0.,fh=0.,asym=0.,orient=ao,polyfunc=pcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=1.0,autoscale=True,pinned_vertex=2))

figure(S,'spacing','autumn')

##

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)//3
ns = T2.n()//nk 

pts = npts

oa = linspace(pi/6,pi/2,n)
ao = linspace(0,-pi,n)
aa = 0

start=int(0.8*ns)
offset = int(0.4*ns)

shift = 0

size = 1 

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=0,orient=ao,polyfunc=pcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=1.0,autoscale=True,pinned_vertex=2))

figure(S,'time','pretty_blues')

##

S = SpiroData()

npts=200*def_factor

nk=1
gs=0
n  = T2.n()//(nk+gs)//3
ns = T2.n()//nk 

pts = npts

oa = pi/4
ao = linspace(0,-pi,n)
aa = pi/4

start=int(0.0*ns)
offset = int(0.6*ns)

shift = 0.2

size = 1 

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=0,orient=ao,polyfunc=pcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=0.0,autoscale=True,pinned_vertex=1))

F.plot(S,color_scheme='spacing',cmap='pale_pink',alpha=0.4,dot_size=.1,no_frame=False)

##

S = SpiroData()

npts=200*def_factor

nk=6
gs=2
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/4
ao = linspace(0,-pi/2,n)
aa = pi/4

start=int(0.0*ns)
offset = int(0.6*ns)

shift = 0.5

size = 1

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=0,orient=ao,polyfunc=pcoords,
                       pts=[pts,0,pts,0],arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=1.0,autoscale=True,pinned_vertex=3))

figure(S,'time','inferno_r')

###

ppl=2000

maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=ppl)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a/2,a),loops=1.0,inside=True,ppl=ppl)

S = SpiroData()

npts=200*def_factor

nk=24
gs=0
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = array([ int(npts/4 + 3/4 * (npts-npts*sin(pi*j/n))) for j in range(n) ])

oa = pi/4
aa = pi/3

start=int(0.0*ns)
offset = int(1.5*ns)

shift = linspace(0,0.3,n)

size = 1 # linspace(1,0.3,n)

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 2*k*pi/nk+linspace(0,pi/6,n)

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=-0.3,orient=ao,polyfunc=pcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=0.0,autoscale=True,pinned_vertex=3,show_side=array([0,1,0,0])))

figure(S,'width','hot')

##

S = SpiroData()

npts=200*def_factor

nk=3
gs=0
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/6
aa = pi/3

start=int(0.0*ns)
offset = int(1.5*ns)

shift = 0

size = 10 

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 2*k*pi/nk+linspace(0,pi/6,n)

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=size,oangle=6,fb=shift,fh=shift,asym=0.3,orient=ao,polyfunc=ngon_coords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=[0,2,4,1,3,5,0],
                       pin_to_frame1=0.0,autoscale=False,pinned_vertex=1,show_side=array([1,0,1,0,1,0])))

figure(S,'cdist5','Oranges')

###

ppl=1000

maj=24
ecc=0.0
a = circum(maj,semi_minor(maj,ecc))/(2*pi)/3
T1 = cIe(Ellipse(maj,ecc),wheel=Wheel(a,a),loops=1.0,inside=True,ppl=ppl)
T2 = cIe(Ellipse(maj,ecc),wheel=Wheel(a/2,a),loops=1.0,inside=True,ppl=ppl)

S = SpiroData()

npts=200*def_factor

nk=3
gs=3
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/6
aa = pi/3

ptf = linspace(0.3,0.5,n)

start=int(0.0*ns)
offset = int(1.0*ns)

shift = 0 

size = 1 

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 0

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n-k*n//5,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=0.3,orient=ao,polyfunc=pcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=ptf,autoscale=True,pinned_vertex=1))

figure(S,'fradii','turbo')

##

S = SpiroData()

npts=200*def_factor

nk=3
gs=2
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

oa = pi/3
aa = -pi/3

ptf = linspace(0.3,0.5,n)

start=int(0.0*ns)
offset = int(1.0*ns)

shift = 0 

size = 1 

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = 2*k*pi/nk+linspace(0,pi/6,n)

    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n-k*n//5,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=0.3,orient=ao,polyfunc=pcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=ptf,autoscale=True,pinned_vertex=1))

figure(S,'cycles','ocean')

###

ppl=2000

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

pts = array([ int(npts/4 + 3/4 * (npts-npts*cos(pi/24*pi*j/n))) for j in range(n) ])

oa = pi/3
aa = pi/5

ptf = array([ cos(2*pi*j/n) for j in range(n) ])

start=int(0.0*ns)
offset = int(1.0*ns)

shift = 0

size = 10

for k in range(nk):
    first1 = k*ns+start
    first2 = k*ns+start+offset
    ao = pi/4

    print(k,first1,first2,n)
    S.add(frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,n2=n,
                       scale=size,oangle=oa,fb=shift,fh=shift,asym=0.3,orient=ao,polyfunc=pcoords,
                       pts=pts,arc_angle=aa,object=k,prot=0,vertex_order=None,
                       pin_to_frame1=ptf,autoscale=False,pinned_vertex=1))

figure(S,'time','inferno')
