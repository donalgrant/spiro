import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="Biframes Examples")
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

F._figname='Biframes-'

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

R = 50

r1 = R
r2 = R/2

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/3,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/7,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,0.5*a1),
         loops=1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,0.5*a2),
         loops=1,ppl=1000,inside=False).rotate(0).move(0,0)

F.plot(S1,color_scheme='cyan',dot_size=.5)
F.plot(S2,color_scheme='green',dot_size=.5,new_fig=False)

S = biframe(S1,S2,2,7,ppl=4000,ng=1,fn=0.05,nk=8,base=0.5,amp=0.5,rate=16,g0=0.3,gf=1.0,n2f=1)

figure(S,'spacing','autumn')

###

R = 50

r1 = R
r2 = R/2

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/4,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/7,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,0.5*a1),
         loops=1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,0.5*a2),
         loops=1,ppl=1000,inside=False).rotate(0).move(0,0)

S = biframe(S1,S2,3,7,ppl=4000,ng=3,fn=0.02,nk=3,base=0.5,amp=0.3,rate=16/3,g0=0.3,gf=1.0,n2f=3)

figure(S,'spacing','turbo')

###

# change to drive with l1 and l2 as primes, then compute ppl's

R = 50

r1 = R
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/4,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/4,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,0.5*a1),
         loops=1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,0.5*a2),
         loops=1,ppl=1000,inside=True,reverse=True).rotate(0).move(R,0)

S = biframe(S1,S2,1,1,ppl=4000,ng=5,fn=0.05,nk=10,base=0.5,amp=0.5,rate=8,g0=0.0,gf=1.0,n2f=1)

figure(S,'spacing','pretty_reds')

###

R = 50

r1 = R
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/4,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/4,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,0.5*a1),
         loops=1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,0.5*a2),
         loops=1,ppl=1000,inside=True,reverse=True).rotate(pi/4).move(R,0)

S = biframe(S1,S2,7,5,ppl=4000,ng=1,fn=0.15,nk=15,base=0.4,amp=0.5,rate=14,g0=0.4,gf=1.0,n2f=1)

figure(S,'spacing','cmap1')

##

S = biframe(S1,S2,3,5,ppl=4000,ng=1,fn=0.25,nk=25,base=0.4,amp=0.5,rate=30,g0=0.4,gf=1.0,n2f=1)

figure(S,'phase','pretty_blues')

###

# change to drive with l1 and l2 as primes, then compute ppl's

R = 50

r1 = R
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/4,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/4,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,a1),
         loops=1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.5*a2),
         loops=1,ppl=1000,inside=True,reverse=False).rotate(pi/7).move(R/10,0)

S = biframe(S1,S2,8,2,ppl=4000,ng=3,fn=0.25,nk=25,base=0.4,amp=0.5,rate=12,g0=0.0,gf=1.0,n2f=1)

figure(S,'cdist3','inferno_r')

###

# change to drive with l1 and l2 as primes, then compute ppl's

R = 50

r1 = R
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/4,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/4,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.3*a1),
         loops=1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.5*a2),
         loops=1,ppl=1000,inside=True,reverse=False).rotate(pi/7).move(R/10,0)

S = biframe(S1,S2,7,2,ppl=4000,ng=2,fn=0.05,nk=5,base=0.4,amp=0.5,rate=28,g0=0.0,gf=1.0,n2f=1)

figure(S,'fcdist3','gist_heat_r')

###

# change to drive with l1 and l2 as primes, then compute ppl's

R = 50

r1 = R*0.75
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/2,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/3,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.3*a1),
         loops=1,ppl=1000,inside=True).rotate(-pi/14)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.5*a2),
         loops=1,ppl=1000,inside=True,reverse=False).rotate(pi/7).move(R/5,0)

S = biframe(S1,S2,3,2,ppl=4000,ng=4,fn=0.10,nk=10,base=0.4,amp=0.5,rate=30,g0=0.0,gf=1.0,n2f=1)

figure(S,'spacing','pretty_reds')

###

# change to drive with l1 and l2 as primes, then compute ppl's

R = 50

r1 = R*0.75
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/2,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/3,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.3*a1),
         loops=1,ppl=1000,inside=True).rotate(-pi/14)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,1.3*a2),
         loops=1,ppl=1000,inside=True,reverse=False).rotate(pi/7).move(R/5,0)

l1=11
l2=17
S = biframe(S1,S2,l1,l2,ppl=4000,ng=1,fn=0.25,nk=5,base=0.2,amp=0.2,rate=2*np.lcm(l1,l2),g0=0.0,gf=1.0,n2f=1)

figure(S,'cdist3','turbo')

###  Redo Figure 0002 as the cover

R = 50

r1 = R
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/4,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/4,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,0.5*a1),
         loops=1,ppl=1000,inside=True)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,0.5*a2),
         loops=1,ppl=1000,inside=True,reverse=True).rotate(0).move(R,0)

S = biframe(S1,S2,1,1,ppl=4000,ng=5,fn=0.05,nk=10,base=0.5,amp=0.5,rate=8,g0=0.0,gf=1.0,n2f=1)

F.plot(S1, color_scheme='cyan', dot_size=1,alpha=1,new_fig=True)
F.plot(S2, color_scheme='yellow', dot_size=1,alpha=1,new_fig=False)
F.plot(S, color_scheme='spacing',cmap='turbo_r',dot_size=0.1,alpha=0.4,new_fig=False)

F.save_fig('Biframes-cover.png')

###

R = 50

r1 = R*0.75
r2 = R

er1 = 0.3
er2 = 0.3

ew1 = 0.0
ew2 = 0.0

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/2,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/3,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,1.3*a1),
         loops=1,ppl=1000,inside=True).rotate(0)
S2 = S1.copy().rotate(pi/10).move(R,0)

l1=1
l2=1
S = biframe(S1,S2,l1,l2,ppl=4000,ng=5,fn=0.2,nk=10,base=0.0,amp=0.4,
            rate=5*np.lcm(l1,l2),g0=0.0,gf=1.0,n2f=1)

figure(S,'cdist3','gist_heat_r')
