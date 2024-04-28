import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

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

S = SpiroData()
R = 50
p = 3
q = 5
ppl = 2000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a1 = R/3
a2 = R/7

S1 = cIc(ring=Ring(R),wheel=Wheel(a1,0.8*a1),loops=l//ppl1,ppl=ppl1,inside=True).rotate(pi/9)
S2 = cIc(ring=Ring(R),wheel=Wheel(a2,1.2*a2),loops=l//ppl2,ppl=ppl2,inside=True)

ptfN = 30*S2.n()
ptf = array([ 0.5 + 1.5 * sin(2*pi*j/ptfN) for j in range(ptfN) ])

nk = 1
for k in range(nk):
    f = 0 
    S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                     normal_intersect=False,object=k))

figure(S,'fcdirs3','turbo')

###

S = SpiroData()
R = 50
p = 2
q = 3
ppl = max(p,q)*3000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a=2

S1 = spiro_cross(width=R,height=R,wheel=Wheel(a,2*a),inside=False,loops=l//ppl1).rotate(pi/4)
S2 = spiro_nstar(4,r1=1.3*R/2,r2=0.3, wheel=Wheel(a,0.8*a),inside=True,loops=l//ppl2)

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = 1*S2.n()
ptf = array([ 0.5 + 0.0 * sin(2*pi*j/ptfN) for j in range(ptfN) ])

nk = 10
nf = 50

o = linspace(0,1.0-1/nf,5)

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                         normal_intersect=False,object=k))

figure(S,'length','gist_heat')

###

S = SpiroData()
R = 50
p = 5
q = 3
ppl = max(p,q)*3000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

a=2

S1 = spiro_cross(width=R,height=R,wheel=Wheel(a,2*a),inside=False,loops=l//ppl1).rotate(pi/4)
S2 = spiro_nstar(4,r1=1.3*R/2,r2=0.3, wheel=Wheel(a,0.8*a),inside=True,loops=l//ppl2)

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = 1*S2.n()
ptf = array([ 0.5 + 0.3 * sin(2*pi*j/ptfN) for j in range(ptfN) ])

nk = 20
nf = 100

o = linspace(0.25,0.75-1/nf,30)

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=500,
                         normal_intersect=False,object=k))

figure(S,'fwidth','hot')

###

S = SpiroData()
R = 50
p = 23
q = 19
ppl = 20000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

r1 = R
r2 = 0.8*R

er = 0.3
ew = 0.6

a1 = major_from_circum(circum(r1,semi_minor(r1,er))/3,ew)
a2 = r2/7

S1 = eIe(ring=Ellipse(r1,er),wheel=Ellipse(a1,ew,1.2*a1),loops=l//ppl1,ppl=1000,inside=True).rotate(pi/9)
S2 = cIc(ring=Ring(r2),wheel=Wheel(a2,a2),loops=l//ppl2,ppl=1000,inside=True)

a=6

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = 5*S2.n()
ptf = array([ 0.5 + 0.0 * sin(7*pi*j/ptfN) for j in range(ptfN) ])

nk = 1
nf = 1

o = linspace(0.0,1.0-1/nf,1)

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                         normal_intersect=False,object=k))

figure(S,'spacing','hot_r',dot_size=0.5)

###

S = SpiroData()
R = 50
p = 17
q = 13
ppl = 15000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

r1 = R
r2 = R

er1 = 0.0
er2 = 0.4

ew1 = 0.6
ew2 = 0.6

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/3,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/3,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.2*a1),
         loops=l//ppl1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.2*a2),
         loops=l//ppl2,ppl=1000,inside=True).rotate(pi/3).move(10,0)

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = S2.n()
ptf = array([ 0.5 + 0.0 * sin(1*pi*j/ptfN) for j in range(ptfN) ])

nk = 6
nf = 10

o = linspace(0.0,1.0-1/nf,4)  

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                         normal_intersect=False,object=k))

figure(S,'spacing','gist_heat_r')

###

R = 50
p = 17
q = 13
ppl = 30000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

r1 = R
r2 = R

er1 = 0.0
er2 = 0.0

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/3,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/7,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.2*a1),
         loops=l//ppl1,ppl=1000,inside=False)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.2*a2),
         loops=l//ppl2,ppl=1000,inside=True).rotate(0).move(0,0)

S = SpiroData()

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = 3*S2.n()
ptf = array([ -0.5 + 0.0 * sin(1*pi*j/ptfN) for j in range(ptfN) ])

nk = 1
nf = 10

o = linspace(0.0,1.0-1/nf,10)  

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                         normal_intersect=False,object=k))

figure(S,'spacing','autumn')

###

R = 50
p = 3
q = 2
ppl = 4000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

r1 = R
r2 = R

er1 = 0.0
er2 = 0.0

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/3,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/7,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.2*a1),
         loops=l//ppl1,ppl=1000,inside=False)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.2*a2),
         loops=l//ppl2,ppl=1000,inside=True).rotate(0).move(0,0)

S = SpiroData()

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = S2.n()
ptf = array([ 0.5 + 0.0 * sin(1*pi*j/ptfN) for j in range(ptfN) ])

nk = 30
nf = 10

o = linspace(0.3,1.0-1/nf,1)  

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        print(oj,k,f)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                         normal_intersect=False,object=k))

figure(S,'cdirs3','pretty_reds')

###

R = 50
p = 3
q = 2
ppl = 8000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

r1 = R
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.7
ew2 = 0.7

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/3,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/7,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.5*a1),
         loops=l//ppl1,ppl=1000,inside=False)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.5*a2),
         loops=l//ppl2,ppl=1000,inside=True).rotate(0).move(0,0)

S = SpiroData()

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = S2.n()//2
ptf = array([ 0.5 + 0.4 * sin(7*pi*j/ptfN) for j in range(ptfN) ])

nk = 30
nf = 20

o = linspace(0.3,1.0-1/nf,1)  

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        print(oj,k,f)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                         normal_intersect=False,object=k))

figure(S,'spacing','Reds')

###

R = 50
p = 13
q = 11
ppl = 10000//max(p,q)
ppl1 = p*ppl
ppl2 = q*ppl
l = np.lcm(ppl1,ppl2)

r1 = R
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/3,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/7,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,0.5*a1),
         loops=l//ppl1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,0.5*a2),
         loops=l//ppl2,ppl=1000,inside=False).rotate(0).move(0,0)

S = SpiroData()

S1 = S1.resample(S1.max_path()*frame_sampling(ppl1))
S2 = S2.resample(S2.max_path()*frame_sampling(ppl2))

ptfN = S2.n()//2
ptf = array([ 0.5 + 0.3 * sin(3*pi*j/ptfN) for j in range(ptfN) ])

nk = 30
nf = 10

o = linspace(0.2,1.0-1/nf,1)  

for oj in range(o.shape[0]):
    for k in range(nk):
        f = int( o[oj]*ppl1 + ppl1/nf * k/nk)
        print(oj,k,f)
        S.add(frame_pair(S1,S2,first1=f,frame_only=True,pin_to_frame1=ptf, n2=ptfN,
                         normal_intersect=False,object=k))

figure(S,'spacing','hot_r')
