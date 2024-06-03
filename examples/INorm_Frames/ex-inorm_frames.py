import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="INorm_Frames Examples")
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

F._figname='INorm_Frames-'

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None,color_dither=0.0,new_fig=True):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,color_dither=color_dither,new_fig=new_fig)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,color_dither=color_dither,new_fig=new_fig)

###

R = 50
ppl = 3000
a = R*3/4
S1 = cIc(ring=Ring(R),wheel=Wheel(a,a/2.4),loops=3,ppl=ppl,inside=True,reverse=False)
f=S1.n()//8

S=SpiroData()

ns = 10
lbox=0.75*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+i*10)
    S.add(T.valid_in_box(0.75*R))

figure(S,'length','turbo')

###

R = 50
ppl = 6000
a = R/5
S1 = cIc(ring=Ring(R),wheel=Wheel(a,a*4),loops=1,ppl=ppl,inside=False,reverse=False)

f=S1.n()//2-12

S=SpiroData()

ns = 20
lbox=4*R

for i in range(ns):
    T = auto_inorm_frame(S1,first=f+i*4,norm_off1=pi/10*i/ns,
                         base=0.5,intersect_tol=.1,amp=0.4,rate=8,norm_off2=0,object=i)
    S.add(T.valid_in_box(4*R))

figure(S,'direction','pretty_reds')

###

R = 50
ppl = 15000
a = R/5
S1 = cIc(ring=Ring(R),wheel=Wheel(a,a*4),loops=1,ppl=ppl,inside=False,reverse=False)
f=S1.n()//4

S=SpiroData()

ns = 20
lbox = 2*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+i*4,norm_off1=pi/10*i/ns,base=0.5,
                         intersect_tol=.1,amp=0.4,rate=8,norm_off2=0,object=i)
    S.add(T.valid_in_box(2*R))

figure(S,'cdist7','gist_heat')

###
R = 50
ppl = 5000
a = R/3

S1 = cIc(ring=Ring(R),wheel=Wheel(a,a*2),loops=1,ppl=ppl,inside=True,reverse=False)

f=S1.n()//7

S=SpiroData()

ns = 25

for i in range(ns):
    T = auto_inorm_frame(S1,first=f,norm_off1=pi/6*i/ns,object=i)
    S.add(T.valid_in_box(2*R))

figure(S,'length','cmap1')

###

R = 50
ppl = 1000
a = 63/64*R

S1 = cIc(ring=Ring(R),wheel=Wheel(a,0.02*a),loops=64,ppl=ppl,inside=True,reverse=False)
f=S1.n()//7

S=SpiroData()

ns = 8
lbox = 2*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+i*8,norm_off1=0,norm_off2=0,
                         base=0.5,amp=0.5,rate=16,object=i)
    for j in range(T.n()):
        T.fx[j]=S1.x[j]
        T.fy[j]=S1.y[j]

    S.add(T.valid_in_box(lbox))
    
figure(S,'dist_to_frm','inferno')

###

R = 50
ppl = 1000
a = R*5/6

S1 = cIc(ring=Ring(R),wheel=Wheel(a,0.3*a),loops=5,ppl=ppl,inside=True,reverse=False).rotate(pi/6)

f=S1.n()//3

S=SpiroData()

ns = 20
lbox = 20*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+i*4,norm_off1=pi/10*i/ns,norm_off2=-pi/8,
                         base=0.0,amp=0.0,rate=2,object=i)
    for j in range(T.n()):
        T.fx[j]=S1.x[j]
        T.fy[j]=S1.y[j]

    S.add(T.valid_in_box(lbox))

figure(S,'fradii','Wistia')

###

R = 50
ppl = 2000
e = 0.02
e_circum=circum(R,semi_minor(R,e))
a = 11/12*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,0.2*a),loops=11,ppl=ppl,inside=True,reverse=False).rotate(pi/6)

f=S1.n()//7

S=SpiroData()

ns = 15
lbox = 2*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+i*5,norm_off1=0,norm_off2=pi/2,
                         base=0.5,amp=0.4,rate=8,object=i)
    for j in range(T.n()):
        T.fx[j]=S1.x[j]
        T.fy[j]=S1.y[j]

    S.add(T.valid_in_box(lbox))

figure(S,'length','gist_heat_r')

###

R = 50
ppl = 2000
e = 0.02
e_circum=circum(R,semi_minor(R,e))
a = 5/7*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,0.5*a),loops=5,ppl=ppl,inside=True,reverse=False).rotate(pi/6)

f=S1.n()//7

S=SpiroData()

ns = 75

lbox = 3*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+int(S1.n()/10*i/ns),norm_off1=0,norm_off2=0.5*pi,
                         intersect_tol=0.001,
                         base=0.0,amp=0.8,rate=10,object=i,n=S1.n()//3).rotate(pi/3*i/ns).valid_in_radius(lbox)
    for j in range(T.n()):
        T.fx[j]=S1.x[j]
        T.fy[j]=S1.y[j]

    S.add(T)

figure(S,'lengths','twilight')

###

R = 50
ppl = 2000
e = 0.02
e_circum=circum(R,semi_minor(R,e))
a = 5/7*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,0.5*a),loops=5,ppl=ppl,inside=True,reverse=False).rotate(pi/6)

f=S1.n()//7

S=SpiroData()

ns = 20

norm = array([ pi/6+pi/3*sin(1*pi*j/S1.n()) for j in range(S1.n()) ])

lbox = 3*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+int(S1.n()/200*i/ns),norm_off1=0,norm_off2=norm,
                         intersect_tol=0.001,
                         base=0.0,amp=0.0,rate=10,object=i,n=S1.n()).rotate(pi/2*i/ns).valid()

    S.add(T)

S = S.valid_in_radius(lbox)

figure(S,'length','autumn')

###

R = 50
ppl = 10000
e = 0.6
e_circum=circum(R,semi_minor(R,e))
a = 1/3*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,0.8*a),loops=1,ppl=ppl,inside=True,reverse=False).rotate(0)

f=S1.n()//7

S=SpiroData()

ns = 40

norm = array([ pi/9*sin(12*pi*j/S1.n()) for j in range(S1.n()) ])

lbox = 1*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                         intersect_tol=0.001,
                         base=0.0,amp=0.0,rate=10,object=i,n=S1.n()).rotate(1.9*pi*i/ns).valid() 
    for j in range(T.n()):
        T.fx[j]=S1.x[j]
        T.fy[j]=S1.y[j]

    S.add(T)

S = S.valid_in_radius(lbox)

figure(S,'dist_to_frm','gist_heat_r')

###

R = 50
ppl = 10000
e = 0.6
e_circum=circum(R,semi_minor(R,e))
a = 1/3*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,0.8*a),loops=1,ppl=ppl,inside=True,reverse=False).rotate(0)

F.plot(S1,color_scheme='cyan',dot_size=.5)

f=S1.n()//7

S=SpiroData()

ns = 200

norm = array([ pi/9*sin(2*pi*j/S1.n()) for j in range(S1.n()) ])

lbox = 2*R
for i in range(ns):
    T = auto_inorm_frame(S1,first=f+int(S1.n()/1*i/ns),norm_off1=0,norm_off2=norm,
                         intersect_tol=0.001,
                         base=0.0,amp=0.0,rate=10,object=i,n=S1.n()//10).rotate(1*pi*i/ns).valid() 
    for j in range(T.n()):
        T.fx[j]=S1.x[j]
        T.fy[j]=S1.y[j]

    S.add(T)

S = S.valid_in_radius(lbox)


figure(S,'width','turbo')

###

R = 50
ppl = 25000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/3*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,1.3*a),loops=1,ppl=ppl,inside=True,reverse=False).rotate(0)

f0=S1.n()//11

S=SpiroData()

ns = 60

n = S1.n()//50

norm = array([ pi/9*sin(2*pi*j/n) for j in range(n) ])

lbox = 1*R
nk = 3
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=0.001,
                             base=0.0,amp=0.6,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        S.add(T)

S = S.valid_in_radius(lbox)

figure(S,'object','pretty_blues')


###

S1 = integral_ellipticals(1,0.7,0.8,max_po=0.0,rounds=2,circuits=1,ppl=10000)
f0=S1.n()//100

S=SpiroData()

nk = 1
ns = 60 

n = S1.n() 

norm = array([ pi/2 + pi/9*sin(2*pi*j/n) for j in range(n) ])

lbox = 20

for k in range(nk):
    f = k*S1.n()//nk//40
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/15*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=0.001,
                             base=0.0,amp=0.4,rate=10,object=i,n=n).rotate(.5*pi*i/ns-pi/3.5).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        S.add(T)

S = S.valid_in_radius(lbox)

figure(S,'length','cmap2')
