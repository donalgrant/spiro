import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="True Slides Examples")
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

F._figname='True_Slides-'

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


S = SpiroData()

###

S.reset()
r=5
num = 41
denom = 7
rf = num/denom
fmr = 19
ecc = 0.8
ppl=1000*def_factor
maj_ring = major_from_circum(rf*2*pi*r,ecc)/fmr
S = cIe(ring=Ellipse(maj_ring,ecc),wheel=Wheel(r,r),loops=fmr*denom,
        slide=array([ 0.3 + 0.1*cos(2*pi*j/ppl) for j in range(ppl) ]),
        ppl=ppl,inside=True)
figure(S,'cdist3','Oranges')

###

S = SpiroData()

r=5
num = 9
denom = 2
rf = num/denom
fmr = 1.25
ecc = 0.0
ppl=2000*def_factor
maj_ring = major_from_circum(rf*2*pi*r,ecc)/fmr
na = 64
o = linspace(0,pi/4,na)
mrf = linspace(1.0,0.9,na)
for j in range(na):
    S.add(cIe(ring=Ellipse(maj_ring*mrf[j],ecc,offset=o[j]),wheel=Wheel(r,r),loops=fmr*denom,
                slide=array([ 0.3 + 1.5*sin(3*2*pi*j/ppl) for j in range(ppl) ]),
                ppl=ppl,inside=True,object=j).rotate(pi/5))

figure(S,'object','Blues')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 5
denom = 2
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

lf=2           # extra loops factor

ppl=2000*def_factor

na = 30
o = linspace(0,pi/3,na)
mrf = linspace(1.0,1.0,na)
pf = linspace(1.0,0.2,na)
sl = frame_sampling(ppl,3,'linear',repeat=2,deramp=True,nocum=True)-2.0
for j in range(na):
    S.add(eIe(ring=Ellipse(maj_ring*mrf[j],er,offset=o[j]),wheel=Ellipse(r,ew,r*pf[j]),loops=lf*denom,
                slide=sl+0.2*j/na,
                ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'object','emerald_woman')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.3  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 5
denom = 2
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

lf=2           # extra loops factor

ppl=2000*def_factor

na = 40
o = linspace(0,0,na)
po = linspace(0,pi/2,na)
mrf = linspace(1.0,1.0,na)
pf = linspace(1.0,1.0,na)
sl = frame_sampling(ppl,3,'linear',repeat=4,deramp=True,nocum=True)-2.0
for j in range(na):
    S.add(eIe(ring=Ellipse(maj_ring*mrf[j],er,offset=o[j]),wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),loops=lf*denom,
                slide=sl+0.00*(j-na/2)/na,
                ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'cycles','autumn')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

lf=1           # extra loops factor

ppl=2000*def_factor

na = 20
o = linspace(0,0,na)
po = linspace(0,0,na)
mrf = linspace(1.0,1.0,na)
pf = linspace(1.0,1.0,na)
for j in range(na):

    sl = frame_sampling(ppl,3,'linear',repeat=j+2,deramp=True,nocum=True)-1.5
    slf = np.average(sl)
    S.add(eIe(ring=Ellipse(maj_ring*mrf[j],er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=lf*denom/slf,
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'object','Reds')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

lf=4           # extra loops factor

ppl=1500*def_factor

na = 40
o = linspace(0,pi/4,na)
po = linspace(0,pi/2,na)
mrf = linspace(1.0,1.0,na)
pf = linspace(1.0,0.2,na)
unit = np.ones(ppl//4)
for j in range(na):

    sl = array([])
    sl = np.append(sl,unit)
    sl = np.append(sl,unit)
    sl = np.append(sl,unit*-1.0)
    sl = np.append(sl,unit)
    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator

    S.add(eIe(ring=Ellipse(maj_ring*mrf[j],er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=lf*denom/slf,
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'length',cmap2)

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

ppl=1500*def_factor

na = 5
o = linspace(0,pi/16,na)
po = linspace(0,0,na)
mrf = linspace(1.0,1.0,na)
pf = linspace(1.0,0.8,na)
unit = np.ones(ppl//3)
for j in range(na):

    sl = array([])
    sl = np.append(sl,unit)
    sl = np.append(sl,unit * -1.3)
    sl = np.append(sl,unit)
    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator

    S.add(eIe(ring=Ellipse(maj_ring*mrf[j],er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=abs(lf*denom/slf),
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'width','hot_r')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

ppl=1500*def_factor

na = 5
o = linspace(0,pi/8,na)
po = linspace(0,0,na)
mrf = linspace(1.0,1.0,na)
pf = linspace(1.0,0.5,na)
unit = np.ones(ppl//5)
for j in range(na):

    sl = array([])
    sl = np.append(sl,unit)
    sl = np.append(sl,unit * 0.5)
    sl = np.append(sl,unit * -0.75)
    sl = np.append(sl,unit * 0.5)
    sl = np.append(sl,unit)
    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator

    S.add(eIe(ring=Ellipse(maj_ring*mrf[j],er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=abs(lf*denom/slf),
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'direction','turbo')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

ppl=1500*def_factor

na = 15
o = linspace(0,0,na)
po = linspace(0,pi/2,na)
pf = linspace(1.0,0.2,na)
unit = np.ones(ppl//2)
for j in range(na):
    
    sl = array([])
    sl = np.append(sl,unit*1)
    sl = np.append(sl,unit * 0.5)

    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator 

    S.add(eIe(ring=Ellipse(maj_ring,er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=abs(lf*denom/slf),
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'object','inferno')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.5  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

ppl=2500*def_factor

na = 64
o = linspace(0,0,na)
po = linspace(0,pi/2,na)
pf = linspace(1.0,0.2,na)
unit = np.ones(ppl//16)
for j in range(na):
    
    sl = array([])
    sl = np.append(sl,unit*1)
    sl = np.append(sl,unit * -0.5)

    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator 

    S.add(eIe(ring=Ellipse(maj_ring,er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=0.5, # abs(lf*denom/slf),
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'spacing','gist_heat_r')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.5  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

ppl=2500*def_factor

na = 128
o = linspace(0,-pi/4,na)
po = linspace(0,pi/2,na)
pf = linspace(1.0,0.2,na)
unit = np.ones(ppl//15)
for j in range(na):
    
    sl = array([])
    sl = np.append(sl,unit*1)
    sl = np.append(sl,unit * -0.2)
    sl = np.append(sl,unit * 0.2)

    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator 

    S.add(eIe(ring=Ellipse(maj_ring,er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=1, # abs(lf*denom/slf),
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))
S.rotate(0.3*pi)

figure(S,'object','hot_r')

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

ppl=3000*def_factor

na = 96*2
o = linspace(0,2.5*pi,na)
po = linspace(0,pi,na)
pf = linspace(1.5,0.5,na)
fl = 0.1
ll = int(ppl*fl)
unit = np.ones(ll)
for j in range(na):
    
    sl = linspace(-2,1.5,ll)

    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator 

    S.add(eIe(ring=Ellipse(maj_ring,er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=fl,
              slide=sl,
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'object','magma_r')

###

S = SpiroData()

r=5   # wheel semi-major axis
ew = 0.0  # wheel eccentricity
er = 0.0  # ring eccentricity
num = 3
denom = 1
rf = num/denom  # multiplies wheel circumference to get ring circumference
maj_ring = major_from_circum(rf*circum(r,semi_minor(r,ew)),er)

ppl=3000*def_factor

na = 96*16
o = linspace(0,7.5*pi,na)
po = linspace(0,pi,na)
pf = linspace(3.5,0.25,na)
fl = 0.1
ll = int(ppl*fl)

for j in range(na):
    
    sl = linspace(-2,1.5,ll)

    slf = np.average(sl)
    f=Fraction(slf).limit_denominator()
    lf = f.denominator 

    S.add(eIe(ring=Ellipse(maj_ring,er,offset=o[j]),
              wheel=Ellipse(r,ew,r*pf[j],pen_offset=po[j]),
              loops=fl,
              slide=sl*(1+j/10),
              ppl=ppl,inside=True,object=j).rotate(0))

figure(S,'object','autumn')
