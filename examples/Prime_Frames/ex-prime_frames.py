import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="Prime Frames Examples")
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

F._figname='Prime_Frames-'

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

S = SpiroData()
R = 50
p = 2
q = 3
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/7

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,a1),loops=l//ppl1,ppl=ppl1,inside=True)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,a2),loops=l//ppl2,ppl=ppl2,inside=True)

ptf = array([ 0.5 + 0.5 * sin(2*pi*j/S2.n()) for j in range(S2.n()) ])

nk = 100
for k in range(nk):
    f = int(k/nk * S2.n()//3)
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf,
                     normal_intersect=False,object=k))

figure(S,'fradii','cmap1')

###

S = SpiroData()
R = 50
p = 2
q = 3
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/7

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,a1),loops=l//ppl1,ppl=ppl1,inside=True)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,a2),loops=l//ppl2,ppl=ppl2,inside=True)

ptf = array([ 0.5 + 0.5 * sin(2*pi*j/S2.n()) for j in range(S2.n()) ])

nk = 1000
for k in range(nk):
    f = int(k/nk * S1.n()//3)
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf,n2=S2.n()//10,
                     normal_intersect=False,object=k))

figure(S,'cdist4','twilight')

###

S = SpiroData()
R = 50
p = 2
q = 3
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/7

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,a1),loops=l//ppl1,ppl=ppl1,inside=True).rotate(pi/3)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,a2),loops=l//ppl2,ppl=ppl2,inside=True).rotate(0)

ptf = 0.5

nk = 200
for k in range(nk):
    f = int(k/nk * S1.n()//3)
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf,
                     normal_intersect=False,object=k))

figure(S,'length','autumn')

###

S = SpiroData()
R = 50
p = 3
q = 5
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/6

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,0.8*a1),loops=l//ppl1,ppl=ppl1,inside=True).rotate(pi/8)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,0.8*a2),loops=l//ppl2,ppl=ppl2,inside=True).rotate(0)

ptf = array([ 0.5 + 1.0 * sin(4*pi*j/S2.n()) for j in range(S2.n()) ])

nk = 200
for k in range(nk):
    f = int(k/nk * S1.n()//2)
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, 
                     normal_intersect=False,object=k))

figure(S,'spacing','Blues')

###

S = SpiroData()
R = 50
p = 11
q = 13
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/4

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,1.0*a1),loops=l//ppl1,ppl=ppl1,inside=True).rotate(pi/3)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,1.2*a2),loops=l//ppl2,ppl=ppl2,inside=True).rotate(0)

ptf = array([ 0.6 + 0.0 * sin(4*pi*j/S2.n()) for j in range(S2.n()) ])

nk = 10
for k in range(nk):
    f = int(k/nk * S1.n()//12)
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf,
                     normal_intersect=False,object=k))

figure(S,'length','emerald_woman')

###

S = SpiroData()
R = 50
p = 11
q = 13
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/4

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,1.0*a1),loops=l//ppl1,ppl=ppl1,inside=True).rotate(pi/3)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,1.2*a2),loops=l//ppl2,ppl=ppl2,inside=True).rotate(0)

ptf = array([ 0.6 + 0.0 * sin(4*pi*j/S2.n()) for j in range(S2.n()) ])

nk = 20
for k in range(nk):
    f = 0
    ptf = k/nk 
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, # n2=S2.n()//10,
                     normal_intersect=False,object=k))

figure(S,'spacing','pretty_reds')

###

S = SpiroData()
R = 50
p = 53
q = 91
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/3

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,1.0*a1),loops=l//ppl1,ppl=ppl1,inside=True).rotate(pi/3)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,1.0*a2),loops=l//ppl2,ppl=ppl2,inside=True).rotate(0)

nk = 1
for k in range(nk):
    f = 0 
    ptf = 0.2 
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, # n2=S2.n()//10,
                     normal_intersect=False,object=k))

figure(S,'length','pale_pink')

###
