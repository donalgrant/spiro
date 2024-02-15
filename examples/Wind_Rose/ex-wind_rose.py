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
from spiro_frame import *
from polygon import *
from Ring import *

parser = argparse.ArgumentParser(description="Wind Rose Examples")
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

F._figname='Wind_Rose-'

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

e=0.2
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/4,a/16),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=16
gs=8
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 # array([ 105 + int(100*cos(pi*j/n)) for j in range(n) ])

for k in range(nk):
    first = k*ns
    asym= 0.5
    scale = 2.5 
    pts= npts
    ao = linspace(0,0.5*pi/nk,n) 
    shift = 0.0
    aa = 0
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

clist = [ 'xkcd:'+i for i in ['pale pink','strong pink','dark fuchsia'] ]
pink_bone = cmap_from_list(clist,'pink_bone')
figure(S,'cycles','pink_bone')

###

e=0.2
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/8,a/3),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=8
gs=8
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200

for k in range(nk):
    first = k*ns 
    asym= 0.4
    scale = 1.5

    pts = linspace(npts//5,npts,8*n,dtype=int) 
    ao = linspace(0,2*pi/nk,n)
    shift = 0.0
    aa = -pi/6
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'segment','inferno')

###

e=0.2
R=4
ppl=900
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/8,a/3),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=8
gs=8
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*160 

for k in range(nk):
    first = k*ns
    asym= 0.1
    scale = 2
    pts= npts
    ao = 0
    shift = 0.0 
    aa = pi
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'time','Blues')

###

e=0.2
R=4
ppl=4000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/8,a/3),ppl=ppl,loops=1,inside=True)

t1=T.n()//11
tn=T.n()//7
W=T.select(slice(t1,t1+tn,4))

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*250 

for k in range(nk):
    first = k*ns
    asym= 0.0
    scale = 2
    pts= npts
    pts = linspace(npts,npts//10,8*n,dtype=int) 
    ao = linspace(0,2*pi/nk,n)
    shift = 0.0 
    aa = pi
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'length','pretty_blues')

##

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*250 

for k in range(nk):
    first = k*ns 
    asym= 0.0 
    scale = 2 
    pts= npts 
    pts = linspace(npts,npts//10,8*n,dtype=int) 
    ao = linspace(0,2*pi/nk,n) 
    shift = 0.0 
    aa = [-pi/2,pi/4]
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'length','Oranges')

###

e=0.2
R=4
ppl=4000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/8,a/3),ppl=ppl,loops=1,inside=True)

t1=3*T.n()//11
tn=T.n()//13
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=1
gs=0
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*250 

for k in range(nk):
    first = k*ns
    asym= linspace(-0.3,0.3,n)
    scale = 2
    pts = linspace(npts,npts//10,8*n,dtype=int) 
    ao = linspace(0,pi/nk,n)
    shift = 0.0 
    aa = linspace(0,-pi/2,8*n)
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'time','pretty_reds')

###

e=0.2
R=4
ppl=4000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/8,a/3),ppl=ppl,loops=1,inside=True)

t1=T.n()//3
tn=T.n()//6
W=T.select(slice(t1,t1+tn,3))

S=SpiroData()

nk=8
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*250

for k in range(nk):
    first = k*ns 
    asym= linspace(-0.3,0.3,n) 
    scale = 4 
    pts = linspace(npts,npts//10,8*n,dtype=int) 
    ao = linspace(0,pi/nk,n) 
    shift = 0.0 
    aa = linspace(pi/3,-pi/3,8*n)
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'cycles','cmap1')

###

e=0.1
R=4
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/4,a/2.5),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=4
gs=2
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200

for k in range(nk):
    first = k*ns + W.n()//9
    asym= 0.2 
    scale = [ 2 + abs(W.direction(j)) for j in range(first,first+n) ]
    pts = [ npts, 0 ]
    ao = linspace(0,2*pi/nk,n)
    shift = 0.0
    aa = linspace(pi/3,pi/9,8*n)
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//3,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'time','emerald_woman')

###

e=0.1
R=4
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/4,a/2.5),ppl=ppl,loops=1,inside=False)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,2))

S=SpiroData()

nk=8
gs=4
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200

for k in range(nk):
    first = k*ns + W.n()//8
    asym= 0.2 
    scale = [ 2 + 8/abs(W.radius(j)) for j in range(first,first+n) ]

    pts = linspace(npts,npts//5,8*n,dtype=int) 

    ao = -pi/4 + linspace(0,3*pi/nk,n)
    shift = 0.0
    aa = -pi/2.5
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=W.n()//9,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'cycles','turbo')

###

e=0.1
R=4
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/8,a/2.5),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=4
gs=8
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200

for k in range(nk):
    first = k*ns + W.n()//8
    asym= -0.5 
    scale = [ 2 + 8/abs(W.radius(j)) for j in range(first,first+n) ]

    pts = linspace(npts,npts//2,8*n,dtype=int) 

    ao = linspace(0,pi/((k+1)*nk),n) 
    shift = 0.0 
    aa = pi/4 
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift,fb=shift,n=n,
                   asym=asym,orient_follow=0,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'time','hot')

###

e=0.1
R=4
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/8,a/7),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=16
gs=8
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns  + W.n()//15
    asym= linspace(0.9,1.1,n) 
    scale = [ 8/abs(W.radius(j)) for j in range(first,first+n) ]
    pts = linspace(npts,npts//2,8*n,dtype=int) 

    ao = 0
    shift_b = 0
    shift_h = 0

    aa = -pi/4 
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift_h,fb=shift_b,n=n,
                   asym=asym,orient_follow=W.n()//8,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'time','pretty_blues')

###

e=0.1
R=4
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/7,a/10),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=6
gs=12
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns 
    print(k,nk,n,ns,first,W.n())
    asym= linspace(0.9,1.1,n)
    scale = 10 
    pts = linspace(npts,npts//2,8*n,dtype=int) 

    ao = 0 
    shift_b = 0
    shift_h = 0

    aa = -pi/4 
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift_h,fb=shift_b,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,'time','OrRd')

###

e=0.1
R=4
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(a/9,a/12),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=3
gs=9
n = W.n()//(nk+gs)
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns
    print(k,nk,n,ns,first,W.n())
    asym= linspace(0.9,1.1,n)
    scale = 3 
    pts = linspace(npts,npts//2,8*n,dtype=int) 

    ao = 0 
    shift_b = 0
    shift_h = 0

    aa = -pi/4 
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift_h,fb=shift_b,n=n,
                   asym=asym,orient_follow=1,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,S.s+S.o/2,'jet')

###

e=0.1
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(int(a/6),a/2),ppl=ppl,loops=7,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=4
n = 150
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns 
    print(k,nk,n,ns,first,W.n())
    asym= linspace(0.1,0.1,n) 
    scale = [ W.radius(j)/3 for j in range(first,first+n) ]
    pts = linspace(npts,npts//8,8*n,dtype=int) 
    ao = pi/4 + linspace(0,-pi/2,n)
    shift_b = 0 
    shift_h = 0 

    aa = -pi/5 
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift_h,fb=shift_b,n=n,
                   asym=asym,orient_follow=10,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))

cs=sin(4*pi*S.t/max(S.t))+sin(S.p)
figure(S,cs,'pale_pink')

###

e=0.1
R=40
ppl=1000
a=circum(R,semi_minor(R,e))/(2*pi)
T = cIe(Ellipse(R,e,pen_offset=pi/4),wheel=Wheel(int(a/6),a/2),ppl=ppl,loops=1,inside=True)

t1=0
tn=T.n()
W=T.select(slice(t1,t1+tn,1))

S=SpiroData()

nk=1
n = 250 
ns = W.n()//nk 

npts = def_factor*200 

for k in range(nk):
    first = k*ns 
    print(k,nk,n,ns,first,W.n())
    asym= linspace(0.,0.,n) 
    scale = [ W.radius(j) for j in range(first,first+n) ]
    pts = linspace(npts,npts,8*n,dtype=int) 
    ao = linspace(0,-pi/1.5,n)
    shift_b = 0 
    shift_h = 0 

    aa = [pi/4,-pi/8] 
    
    S.add(on_frame(W,scale=scale,oangle=4,first=first,fh=shift_h,fb=shift_b,n=n,
                   asym=asym,orient_follow=10,orient=ao,polyfunc=nstar_coords,
                   arc_angle=aa,pts=pts,object=k,prot=0))
    
figure(S,sin(2*S.p),'cmap1')
