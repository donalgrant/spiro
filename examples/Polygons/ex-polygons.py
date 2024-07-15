import sys
sys.path.append('../..')
import argparse

from SpiroData import *
from SpiroDraw import *
from spiro import *
from polygon import *

parser = argparse.ArgumentParser(description="Polygons")
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

F._figname='Polygons-'

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1,filename=None,limits=None,color_dither=0.0,no_frame=True):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    if filename is None:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,save=save,
               limits=limits,color_dither=0.0,no_frame=no_frame)
    else:
        F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,
               save=save,filename=filename,limits=limits,color_dither=0.0,no_frame=no_frame)
        
S = SpiroData()

###

F.plot(spiro_square(R=64,wheel=Wheel(8,8),loops=10,inside=True),new_fig=True,save=True)

###

F.plot(spiro_square(20,Wheel(4,3.5),loops=20,fold=False,inside=True),new_fig=True,save=True,filename='missing.png')

###

F.plot(spiro_square(20,Wheel(4,3.5),orient=0,loops=20,fold=False,inside=False),new_fig=True)
F.plot(spiro_square(20,Wheel(4,3.5),orient=0,loops=20,fold=False,inside=True),new_fig=False)
F.save_fig()

###

F.plot(spiro_square(23,Wheel(4,3.5),orient=pi/4,loops=20,fold=False,inside=False),new_fig=True)
F.plot(spiro_square(10,Wheel(2.5,7.5),orient=pi/2,loops=20,fold=False,inside=True),new_fig=False)
F.save_fig()

###

F.plot(spiro_square(30,Wheel(5,7),loops=30,fold=True),
       color_scheme='polar',cmap='hsv',save=True)

###

F.plot(spiro_eq_triangle(62,Wheel(20,15),orient=0,loops=20,fold=False),
       color_scheme='radial',cmap='viridis')
F.plot(spiro_eq_triangle(62,Wheel(7,11),orient=0,loops=20,inside=True),
       color_scheme='time',cmap='autumn',new_fig=False,save=True)

###

cs='time'
F.plot(spiro_eq_triangle(62,Wheel(-20,15),orient=0,loops=10,fold=False),
       color_scheme=cs,cmap='magma',new_fig=True)
F.plot(spiro_eq_triangle(62,Wheel(-20,14),orient=0,loops=10,fold=False),
       color_scheme=cs,cmap='magma',new_fig=False)
F.plot(spiro_eq_triangle(62,Wheel(-20,13),orient=0,loops=10,fold=False),
       color_scheme=cs,cmap='magma',new_fig=False)
F.save_fig()

###

F.plot(spiro_eq_triangle(50,Wheel(5,4.5),orient=0,loops=30,fold=True,inside=False),
       cmap="Oranges",color_scheme='time',  new_fig=True)
F.plot(spiro_eq_triangle(50,Wheel(7,4.0),orient=0,loops=40,fold=False,inside=True),
       cmap="BuGn",   color_scheme='cycles',new_fig=False)
F.save_fig()

###

F.plot(spiro_eq_triangle(50,Wheel(5,4.5),orient=pi,loops=30,fold=True,inside=False),
       cmap="Oranges",color_scheme='time',  new_fig=True)
F.plot(spiro_eq_triangle(50,Wheel(7,4.0),orient=pi/4,loops=40,fold=False,inside=True),
       cmap="BuGn",   color_scheme='cycles',new_fig=False)
F.save_fig()

###

F.plot(spiro_eq_triangle(6,Wheel(5.5,3.0),orient=0,loops=70,fold=False,inside=True))
F.save_fig()

###

o=0
w=Wheel(3,2)
coords=array([ [-20,0], [0,20], [20,20], [40,0], [20,-20], [0,-20] ])
F.plot(spiro_polygon(coords, Wheel(0.01,0.0), o, 1, fold=False, inside=False))
F.plot(spiro_polygon(coords, w, o, 10, fold=False, inside=False),new_fig=False)
F.plot(spiro_polygon(coords, w, o, 10, fold=False, inside=True),new_fig=False)

F.save_fig()

###

o=0
w=Wheel(3,2)
coords=array([ [-20,0], [0,20], [20,20], [40,0], [20,-20], [0,-20] ])
F.plot(spiro_polygon(coords, Wheel(0.01,0.0), o, 1, fold=True, inside=False))
F.plot(spiro_polygon(coords, w, o, 10, fold=True, inside=False),new_fig=False)
F.plot(spiro_polygon(coords, Wheel(3*w.r,2*w.m), o, 30, fold=True, inside=True),new_fig=False)

F.save_fig()

###

o=0
w=Wheel(3,2)
coords=array([ [-20,0], [20,0] ])
F.plot(spiro_polygon(coords, Wheel(0.01,0), o, 1, fold=True, inside=False))
F.plot(spiro_polygon(coords, w, o, 10, fold=False, inside=False),new_fig=False)
F.plot(spiro_polygon(coords, Wheel(0.01,0), o, 1, fold=True, inside=False))
F.plot(spiro_polygon(coords, w, o, 10, fold=True, inside=False),new_fig=False)

F.save_fig()

###

R=20
o = -pi/2
w = Wheel(3,2)
F.plot(spiro_ngon(7, R, Wheel(0.01,0), o, loops=1,  fold=False, inside=False))
F.plot(spiro_ngon(7, R, w, o, loops=10, fold=False, inside=False),new_fig=False)
F.plot(spiro_ngon(7, R, w, o, loops=10, fold=False, inside=True), new_fig=False)

F.save_fig()

###

R=20
o = -pi/2
w = Wheel(3,2)
F.plot(spiro_ngon(9, R, Wheel(0.01,0), o, loops=1,  fold=False, inside=False))
F.plot(spiro_ngon(9, R, w, o, loops=10, fold=True,  inside=False),new_fig=False)
F.plot(spiro_ngon(5, R/2, Wheel(w.r,3*w.m), o, loops=26, fold=False, inside=True), new_fig=False)

F.save_fig()

###

(w,p)=(2.9,1.1)
F.plot(poly_heart(wheel=Wheel(0.01,0),loops=1,inside=False))
F.plot(poly_heart(wheel=Wheel(w,3*p),loops=10,inside=True), new_fig=False)
F.plot(poly_heart(wheel=Wheel(w,3*p),loops=10,inside=False),new_fig=False)

F.save_fig()

###

(R,w,p,o)=(41,5,10,-pi/2)
for p in np.linspace(15,25,10):
    F.plot(spiro_ngon(5, R, Wheel(w,p,10*p*pi/180), o,
                      loops=1, fold=False, inside=True),
           new_fig=True if p==15 else False)

F.save_fig()

###

(R,w,p,o)=(41,5,10,-pi/2)

for p in np.linspace(15,25,10):
    F.plot(spiro_ngon(3, R, Wheel(w,p,10*p*pi/180), o,
                      loops=1, fold=False, inside=True),
           new_fig=True if p==15 else False)

F.save_fig()

###

(R,w,p,o)=(41,5,10,-pi/2)

for o in np.linspace(15,150,50):
    F.plot(spiro_ngon(3, R, Wheel(w,p), o*pi/180,
                      loops=1, fold=False, inside=True),
           new_fig=True if o==15 else False)

F.save_fig()

###

(R,w,p,o)=(41,5,10,-pi/2)
for o in np.linspace(15,150,50):
    F.plot(spiro_ngon(3, R+o/3, Wheel(w,p), o*pi/180,
                      loops=1, fold=False, inside=True),
           new_fig=True if o==15 else False)

F.save_fig()

###

(R,w,p,o)=(41,5,10,-pi/2)

for o in np.linspace(15,150,50):
    F.plot(spiro_ngon(3, R+o/3, Wheel(w,p), o*pi/180,
                      loops=1, fold=False, inside=False),
           new_fig=True if o==15 else False)

F.save_fig()

###

o=0
w=Wheel(3,5)
n_points=4
np.random.seed(6)
coords=np.random.uniform(0,100,(n_points,2))
F.plot(spiro_polygon(coords, w, o, 20,   fold=False, inside=False))
F.plot(spiro_polygon(coords, w, o, 10,   fold=False, inside=True),new_fig=False)

F.save_fig()

###

S=SpiroData()

c="autumn"
cs="length"

r = 10
w  = Wheel(3,2.8,0)
w0 = Wheel(0.01,0,0)

S.add(roll(0,r,r,r,wheel=w0,invert=False))
w0.o=S.pc()
S.add(cIc(Ring(r),w0,loops=0.5).move(r,0))
w0.o=S.pc()
S.add(roll(r,-r,0,-r,wheel=w0,invert=False))
w0.o = S.pc()
S.add(cIc(Ring(r),w0,loops=0.5).rotate(pi))
        
for q in (False,True):
    offset=0
    for i in range(20):
        S.add(roll(0,r,r,r,wheel=w,invert=q))
        w.o=S.pc()
        S.add(cIc(Ring(r),w,loops=0.5,inside=q).move(r,0))
        w.o=S.pc()
        S.add(roll(r,-r,0,-r,wheel=w,invert=q))
        w.o=S.pc()
        S.add(cIc(Ring(r),w,loops=0.5,inside=q).rotate(pi))
        w.o=S.pc()
    
F.plot(S,cmap=c,color_scheme=cs,save=True)

###

S.reset()
for i in range(1):
    S.add(spiro_nstar(4,r2=0.6,wheel=Wheel(5,4),orient=0,
                  loops=14,inside=False,fold=True))
    S.add(spiro_nstar(4,r2=0.6,wheel=Wheel(6,5),orient=0,
                  loops=30,inside=True,fold=False))
F.plot(S,color_scheme='time',cmap='jet',save=True)

###

S.reset()

S.add(spiro_nstar(4,r2=0.6,wheel=Wheel(5,4),orient=0,
                  loops=14,inside=False,fold=True))
S.add(spiro_nstar(4,r2=0.6,wheel=Wheel(6,5),orient=0,
                  loops=30,inside=True,fold=False))
S.add(spiro_nstar(4,r2=0.6,wheel=Wheel(18,8),orient=0,
                  loops=30,inside=False,fold=False))

F.plot(S,color_scheme='l-waves',cmap='RdPu',save=True)

###

S1 = SpiroData()
R = 50
ppl = 4000
a=R/(2*pi)/3
ns = 75
pen_scale=0.995
rot_inc=pi/75
shrink=0.998
max_po=pi/4
dy=-R/75
for i in range(ns):
    S1.add(spiro_eq_triangle(R=R,wheel=Wheel(a,a*(pen_scale**i),max_po*i/ns),
                             object=i,orient=0,loops=1,fold=False,inside=False)
           ).rotate(rot_inc).move(0,dy).scale(shrink)

figure(S1,'fradii','hot_r')
