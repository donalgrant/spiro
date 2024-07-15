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

parser = argparse.ArgumentParser(description="Hexagon Examples")
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

F._figname='Hexed-'

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1*(1+hd),filename=None,color_dither=0.0):
    transparent=True
    if hd:
        transparent=False
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,color_dither=color_dither,transparent=transparent)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,color_dither=color_dither,transparent=transparent)

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=False).rotate(pi/4)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

aa=0 

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = 0
pts = def_factor*200
for k in range(nk):
    first = k*ns 
    asym=0 
    scale =  4 
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=6,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=1,orient=ao, polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'cycles','pale_pink')

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/6),ppl=ppl,loops=1,inside=True).rotate(pi/4)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

aa=0

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = 0 
pts = def_factor*200
for k in range(nk):
    first = k*ns 
    asym=0 
    scale =  [ 9/W.radius(j) for j in range(first,first+n) ]
    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=6,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=1,orient=ao, polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','pretty_blues')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/6,a/3),ppl=ppl,loops=1,inside=True).rotate(pi/4)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

aa=0

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 
ao = 0 
pts = def_factor*200
for k in range(nk):
    first = k*ns 
    asym=0
    scale =  6 

    S.add(on_frame(W.rotate(0*k*pi/5),scale=scale,oangle=6,first=first,fh=0,fb=0,n=n,
                   asym=asym,orient_follow=0,orient=ao, polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'cycles',LinearSegmentedColormap.from_list(
                  "OrBl", ['xkcd:white','xkcd:azure']
                  ))

##

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200

for k in range(nk):
    first = k*ns 
    asym=0 
    scale = linspace(3.0,3.5,n) 
    pts= linspace(npts//5,npts,n,dtype=int)
    aa = -pi/6
    ao = 0 
    shift = 0.0 
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=11,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,S.o+S.s/2,'Oranges')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/4),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=12
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 # array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])

for k in range(nk):
    first = k*ns 
    asym=0 # linspace(0.5,1.0,n)
    scale = 4.0 # linspace(3.0,3.5,n) # [ 9/W.radius(j) for j in range(first,first+n) ]
    pts= linspace(npts//5,npts,n,dtype=int) # np.geomspace(20,npts,6*n,dtype=int) 
    aa = -pi/3
    ao = 0 # [ np.random.standard_normal()*pi/100 for j in range(n) ]  # [ pi/6*sin(2*pi*j/n) for j in range(n) 
    shift = 0.0 # linspace(-0.5,0.5,n)
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=11,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','cmap1')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=12
gs=18
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200

for k in range(nk):
    first = k*ns 
    asym=0 
    scale = 4.0
    pts= linspace(npts//3,npts,n,dtype=int)
    ao = 0
    shift = 0.0 
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=ngon_coords,
                   arc_angle=pi/3,pts=pts,object=k,prot=0))
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=ngon_coords,
                   arc_angle=-pi/3,pts=pts,object=k,prot=0))

figure(S,'cycles','ocean')

###

e=0.0
R=4
ppl=1200
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/4,a/2),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2)).inverted_radii()

nk=12
gs=18
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 # array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])

S = SpiroData()

for k in range(nk):
    first = k*ns 
    asym=0 # linspace(0.5,1.0,n)
    scale = 1 # linspace(3.0,3.5,n) # [ 9/W.radius(j) for j in range(first,first+n) ]
    pts= linspace(npts//3,npts,n,dtype=int) # np.geomspace(20,npts,6*n,dtype=int) 
    ao = 0 # [ np.random.standard_normal()*pi/100 for j in range(n) ]  # [ pi/6*sin(2*pi*j/n) for j in range(n) 
    shift = 0.0 # linspace(-0.5,0.5,n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=ngon_coords,
                   arc_angle=pi/3,pts=pts,object=k,prot=0))
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=ngon_coords,
                   arc_angle=-pi/3,pts=pts,object=k,prot=0))

figure(S,'segment','hot')

##

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=3
gs=3
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200

for k in range(nk):
    first = k*ns 
    asym=0
    scale = 2
    pts= 150 
    ao = linspace(0,pi,n)
    shift = 0.0 
    aa = -pi/3
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=0,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','Oranges')

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=False).rotate(pi/7)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=3
gs=1
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*150 

for k in range(nk):
    first = k*ns 
    asym=0
    scale = 3
    pts= npts
    ao = linspace(0,pi,n)
    shift = 0.0
    aa = -pi
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'cycles','autumn_r')

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)

T = spiro_line(R,Wheel(1.5/pi,0.7/pi),loops=3,fold=False,invert=False)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,7))

S=SpiroData()

nk=15
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*150 # array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])

for k in range(nk):
    first = k*ns + W.n()//6
    asym=0
    scale = 2
    pts= linspace(npts//5,npts,6*n,dtype=int) 
    ao = 0 
    shift = 0.0
    aa = -pi/1.75
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'object','turbo')

###

R=4

T = spiro_ngon(6,R,Wheel(R/(3*2*pi),R/(2*pi)),loops=1,fold=False,inside=False)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,5))

S=SpiroData()

nk=15
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*150

for k in range(nk):
    first = k*ns + W.n()//6
    asym=0
    scale = 0.7
    pts= linspace(npts//5,npts,6*n,dtype=int) 
    ao = 0
    shift = 0.0
    aa = linspace(pi,-pi,3*n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=0,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','hot')

##

S=SpiroData()

nk=15
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*150 

for k in range(nk):
    first = k*ns + W.n()//6
    asym=0 
    scale = 1 
    pts= linspace(npts//5,npts,6*n,dtype=int) 

    ao = 0 
    shift = 0.0
    aa = linspace(pi,-pi,3*n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//12,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'direction','Reds')

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)

T = spiro_nstar(6,0.5,3*R,Wheel(R,R/3),loops=1,fold=False,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,20))

nk=18
gs=6
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*150 # array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])

S=SpiroData()

for k in range(nk):
    first = k*ns + W.n()//6
    asym=0 
    scale = [ W.radius(j)**0.8 for j in range(first,first+n) ]
    pts= linspace(npts//5,npts,6*n,dtype=int) 
    # pts = np.geomspace(20,npts,6*n,dtype=int) 
    ao = linspace(0,pi/4,n)
    shift = 0.0
    aa = linspace(0,-pi,6*n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//7,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','autumn')

##

S=SpiroData()

nk=12
gs=12
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*150 # array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])

for k in range(nk):
    first = k*ns + W.n()//6
    asym=0 # linspace(0.5,1.0,n)
    scale = 45 # linspace(3.0,3.5,n) # [ 9/W.radius(j) for j in range(first,first+n) ]
    pts= linspace(npts//5,npts,6*n,dtype=int) 
    # pts = np.geomspace(20,npts,6*n,dtype=int) 
    ao = linspace(0,pi/2,n) # [ np.random.standard_normal()*pi/100 for j in range(n) ]  # [ pi/6*sin(2*pi*j/n) for j in range(n) 
    shift = 0.0 # linspace(-0.5,0.5,n)
    aa = linspace(0,-pi,6*n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//7,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','turbo')

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)

T = spiro_nstar(6,-0.5,3*R,Wheel(R/30,R/30),loops=1,fold=False,inside=True)

F.plot(T,no_frame=False,dot_size=10,cmap='pale_pink',color_scheme='#fc642d')
t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,20))

S=SpiroData()

nk=12
gs=12
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200

for k in range(nk):
    first = k*ns + W.n()//6
    asym=0 
    scale = 3
    pts= linspace(npts//5,npts,6*n,dtype=int) 

    ao = linspace(0,pi/4,n)
    shift = 0.0
    aa = linspace(0,-pi,6*n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','Oranges')

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)

T = spiro_nstar(6,-0.5,3*R,Wheel(R/30,R/30),loops=1,fold=False,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,10)).inverted_radii()

S=SpiroData()

nk=6
gs=12
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*300

for k in range(nk):
    first = k*ns + W.n()//20
    asym=0
    scale = [ 6/W.radius(j) for j in range(first,first+n) ]
    pts= linspace(npts//5,npts,6*n,dtype=int) 

    ao = linspace(0,pi/2,n)
    shift = 0.0
    aa = linspace(0,-pi,6*n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'time','gist_heat')

###

e=0.0
R=4
ppl=600
a=circum(R,semi_minor(R,e))/(2*pi)
#T = cIe(Ellipse(R,e),wheel=Wheel(a/3,a/3),ppl=ppl,loops=1,inside=True).rotate(pi/7)

T = spiro_nstar(6,-0.5,3*R,Wheel(R/30,R/30),loops=1,fold=False,inside=True)

t1=0
tn=T.n()
j = np.where( (T.x**2+T.y**2>1.0) )
W=T.select(j).subsample(5).inverted_radii()

S=SpiroData()

nk=6
gs=12
n = W.n()//(nk+gs)
ns = W.n()//nk 

def_factor=1
npts = def_factor*200 # array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])

for k in range(nk):
    first = k*ns + W.n()//36
    asym=0 # linspace(0.5,1.0,n)
    scale = 1 # [ 6/W.radius(j) for j in range(first,first+n) ] # 4 # linspace(3.0,3.5,n) 
    pts= linspace(npts//5,npts,6*n,dtype=int) 
    # pts = np.geomspace(20,npts,6*n,dtype=int) 
    ao = linspace(0,pi/2,n) # [ np.random.standard_normal()*pi/100 for j in range(n) ]  # [ pi/6*sin(2*pi*j/n) for j in range(n) 
    shift = 0.0 # linspace(-0.5,0.5,n)
    aa = linspace(0,-pi,6*n)
    
    S.add(on_frame(W,scale=scale,oangle=6,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=ngon_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

figure(S,'segment','turbo')
