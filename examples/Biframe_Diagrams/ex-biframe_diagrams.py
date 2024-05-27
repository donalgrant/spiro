import sys
sys.path.append('../..')
import argparse

from SpiroDraw import *
from spiro import *
from spiro_ellipse import *
from spiro_frame import *
from polygon import *

from fractions import Fraction

parser = argparse.ArgumentParser(description="Biframe Diagrams Examples")
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

F._figname='Biframe_Diagrams-'

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

###  First frame S1 is the larger one with 3 lobes, second S2 is inner with 7 lobes

R = 50

r1 = R
r2 = 0.8*R

er1 = 0.0
er2 = 0.0

ew1 = 0.0
ew2 = 0.0

ppl = 3000

a1 = major_from_circum(circum(r1,semi_minor(r1,er1))/3,ew1)
a2 = major_from_circum(circum(r2,semi_minor(r2,er2))/7,ew2)

S1 = eIe(ring=Ellipse(r1,er1),wheel=Ellipse(a1,ew1,0.5*a1),loops=1,ppl=ppl,inside=False)
S2 = eIe(ring=Ellipse(r2,er2),wheel=Ellipse(a2,ew2,0.5*a2),loops=1,ppl=ppl,inside=False)

##

S0 = SpiroData()

F.plot(S1,color_scheme='cyan', dot_size=.2, new_fig=True)
F.plot(S2,color_scheme='green',dot_size=.2, new_fig=False)

for base in [-0.5,0.25,0.5,0.75,1.5]:
    S0.add(biframe(S1,S2,1,1,ppl=1000, amp=0, base=base))

figure(S0,'orange','Reds',new_fig=False,dot_size=1.0,alpha=1.0)

##

S0 = SpiroData()

F.plot(S1,color_scheme='cyan', dot_size=.2, new_fig=True)
F.plot(S2,color_scheme='green',dot_size=.2, new_fig=False)

S0 = biframe(S1,S2,1,1,ppl=1000, amp=0.5, base=0.5, rate=20)

figure(S0,'orange','Reds',new_fig=False,dot_size=1.0,alpha=1.0)

##

(l1,l2) = (1,1)

(nk,fn,ng,g0,gf) = (1,0.0,1,0.0,1.0)
(base,amp,rate,n2f) = (0.5,0.0,8,1)

npp = max(l1,l2) * 100

S  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f)
Sa = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=1.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
Sb = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=0.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
S0 = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f,
            show_line=True)

T  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=0.5,rate=rate,g0=g0,gf=gf,n2f=n2f)
T0 = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=0.5,rate=rate,g0=g0,gf=gf,n2f=n2f,
            show_line=True)

small_offsets = linspace(0,0.5,Sa.n())
alpha = linspace(1.0,0.5,npp)

F.plot(S, color_scheme='red',cmap='Reds',dot_size=20,alpha=alpha,new_fig=True)
F.plot(T, color_scheme='red',cmap='Reds',dot_size=20,alpha=alpha,new_fig=False)

F.plot(Sa.move(small_offsets,small_offsets), color_scheme='cyan',dot_size=20,alpha=alpha,new_fig=False)
F.plot(Sb.move(small_offsets,small_offsets), color_scheme='green',dot_size=20,alpha=alpha,new_fig=False)
F.plot(S1,color_scheme='cyan', dot_size=.2, new_fig=False)
F.plot(S2,color_scheme='green',dot_size=.2, new_fig=False)

nj = npp//10
show_line_offsets = linspace(g0*npp,(1+g0)*npp,nj,dtype=int)
for j in show_line_offsets:
    F.plot(S0.select(np.where(S0.s==j)),color_scheme='orange',dot_size=.3,new_fig=False)
    F.plot(T0.select(np.where(S0.s==j)),color_scheme='orange',dot_size=.3,new_fig=False)

F.save_fig()

##

(l1,l2) = (1,1)

(nk,fn,ng,g0,gf) = (1,0.0,1,0.3,1.0)
(base,amp,rate,n2f) = (0.5,0.0,8,1)

npp = max(l1,l2) * 100

S  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f)

Sa = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=1.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
Sb = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=0.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
S0 = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f,
            show_line=True)

small_offsets = linspace(0,0.5,Sa.n())
alpha = linspace(1.0,0.5,npp)

F.plot(S, color_scheme='red',cmap='Reds',dot_size=20,alpha=alpha,new_fig=True)

F.plot(Sa.move(small_offsets,small_offsets), color_scheme='cyan',dot_size=20,alpha=alpha,new_fig=False)
F.plot(Sb.move(small_offsets,small_offsets), color_scheme='green',dot_size=20,alpha=alpha,new_fig=False)
F.plot(S1,color_scheme='cyan', dot_size=.2, new_fig=False)
F.plot(S2,color_scheme='green',dot_size=.2, new_fig=False)
nj = npp//10
show_line_offsets = linspace(int(g0*npp),int((1+g0-1/nj)*npp),nj,dtype=int)
for j in show_line_offsets:
    F.plot(S0.select(np.where(S0.s==j)),color_scheme='orange',dot_size=.3,new_fig=False,
          alpha=alpha[j-show_line_offsets[0]])

F.save_fig()

##

(l1,l2) = (1,1)

(nk,fn,ng,g0,gf) = (1,0.0,1,0.3,1.0)
(base,amp,rate,n2f) = (0.5,0.0,8,1)

npp = max(l1,l2) * 100

S  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f)

Sa = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=1.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
Sb = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=0.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
S0 = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f,
            show_line=True)

small_offsets = linspace(0,0.5,Sa.n())
alpha = linspace(1.0,0.5,npp)

F.plot(S, color_scheme='red',cmap='Reds',dot_size=20,alpha=alpha,new_fig=True)

F.plot(Sa.move(small_offsets,small_offsets), color_scheme='cyan',dot_size=20,alpha=alpha,new_fig=False)
F.plot(Sb.move(small_offsets,small_offsets), color_scheme='green',dot_size=20,alpha=alpha,new_fig=False)
F.plot(S1,color_scheme='cyan', dot_size=.2, new_fig=False)
F.plot(S2,color_scheme='green',dot_size=.2, new_fig=False)
nj = npp//10
show_line_offsets = linspace(int(g0*npp),int((1+g0-1/nj)*npp),nj,dtype=int)
for j in show_line_offsets:
    o = j-show_line_offsets[0]
    F.plot(S0.select(np.where(S0.s==j)),color_scheme='orange',dot_size=.3,new_fig=False,
          alpha=alpha[o])
    F.plot(S.select(slice(o,o+1)),color_scheme='blue',dot_size=50,new_fig=False,
          alpha=alpha[o])

F.save_fig()

##

(l1,l2) = (2,3)

(nk,fn,ng,g0,gf) = (1,0.0,1,0.0,1.0)
(base,amp,rate,n2f) = (0.5,0.0,8,1)

npp = np.lcm(l1,l2) * 30

S  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f)
Sa = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=1.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
Sb = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=0.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
S0 = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f,
            show_line=True)

small_offsets = linspace(1.0,1.05,Sa.n())
alpha = linspace(1.0,0.2,l2*npp)

F.plot(S, color_scheme='red',cmap='Reds',dot_size=20,alpha=alpha,new_fig=True)
F.plot(Sa.scale(small_offsets), color_scheme='cyan',dot_size=20,alpha=alpha,new_fig=False)
F.plot(Sb.scale(small_offsets), color_scheme='green',dot_size=20,alpha=alpha,new_fig=False)
F.plot(S1,color_scheme='cyan', dot_size=.2, new_fig=False)
F.plot(S2,color_scheme='green',dot_size=.2, new_fig=False)

nj = npp//5
show_line_offsets = linspace(int(g0*npp),int((1+g0-1/nj)*l2*npp),nj,dtype=int)
for j in show_line_offsets:
    o = j-show_line_offsets[0]
    F.plot(S0.select(np.where(S0.s==j)),color_scheme='orange',dot_size=.3,new_fig=False,
          alpha=alpha[o])
    F.plot(S.select(slice(o,o+1)),color_scheme='blue',dot_size=50,new_fig=False,
          alpha=alpha[o])

F.save_fig()

##

(l1,l2) = (2,3)

(nk,fn,ng,g0,gf) = (1,0.0,1,0.2,1.0)
(base,amp,rate,n2f) = (0.5,0.0,8,1)

npp = np.lcm(l1,l2) * 30

S  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f)
Sa = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=1.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
Sb = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=0.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
S0 = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f,
            show_line=True)

small_offsets = linspace(1.0,1.1,Sa.n())
alpha = linspace(1.0,0.4,Sa.n())

F.plot(S,                       color_scheme='red',  dot_size=20,alpha=alpha,new_fig=True)
F.plot(Sa.scale(small_offsets), color_scheme='cyan', dot_size=20,alpha=alpha,new_fig=False)
F.plot(Sb.scale(small_offsets), color_scheme='green',dot_size=20,alpha=alpha,new_fig=False)
F.plot(S1,                      color_scheme='cyan', dot_size=.2, new_fig=False)
F.plot(S2,                      color_scheme='green',dot_size=.2, new_fig=False)

pplf = npp//max(l1,l2)

nj = npp//8
flo = int(g0*l2*pplf)

show_line_offsets = linspace(flo,flo+S.n(),nj,dtype=int)
for j in show_line_offsets:
    o = j-show_line_offsets[0]
    F.plot(S0.select(np.where(S0.s==j)),color_scheme='orange',dot_size=.3,new_fig=False,alpha=1.0)
    F.plot(S.select(slice(o,o+1)),      color_scheme='blue',dot_size=50,new_fig=False, alpha=1.0)

F.save_fig()

##

(l1,l2) = (2,3)

(nk,fn,ng,g0,gf) = (1,0.0,1,0.0,1.0)
(base,amp,rate,n2f) = (0.5,0.5,4/3,1)

npp = np.lcm(l1,l2) * 300

S  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f)

Sa = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=1.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
Sb = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=0.0, amp=0,  rate=rate,g0=g0,gf=gf,n2f=n2f)
S0 = biframe(S1,S2,l1,l2,ppl=npp, ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=n2f,
            show_line=True)

T  = biframe(S1,S2,l1,l2,ppl=npp,ng=ng,fn=fn,nk=nk,base=base,amp=amp,rate=rate,g0=g0,gf=gf,n2f=3)

small_offsets = linspace(1.0,1.1,Sa.n())
alpha = linspace(1.0,0.4,Sa.n())

F.plot(S,                       color_scheme='red',  dot_size=5.0,alpha=alpha,new_fig=True)
F.plot(T,                       color_scheme='blue',  dot_size=0.5,alpha=alpha,new_fig=False)
F.plot(S1,                      color_scheme='cyan', dot_size=.2, new_fig=False)
F.plot(S2,                      color_scheme='green',dot_size=.2, new_fig=False)

F.save_fig()

### intersecting normal diagrams follow

R = 50
ppl = 400
a = R/3.0
S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.5*a),loops=1,ppl=ppl,inside=True,reverse=False)

f=S1.n()//3

npts = 5
step = 13

S = auto_inorm_frame(S1,first=f,norm_off1=0,intersect_tol=0.001,show_intersect=True)

T = S.select(S.s<0)
S = S.select(S.s>=0)

TT = T.select(-T.s <= npts*step)

H = SpiroData()
for i in range(0,npts*step,step):
    H.load(array([S1.xy(i)]))
    H.load(array([S1.xy(i+f)]))

F.plot(S1,color_scheme='cyan',dot_size=1,new_fig=True)
F.plot(TT.select(TT.s % step == step-1),color_scheme='white',cmap='turbo',dot_size=1,alpha=1,new_fig=False)
F.plot(S.select(slice(0,npts*step,step)),color_scheme='orange',dot_size=40,new_fig=False)
F.plot(S,color_scheme='orange',dot_size=0.5,new_fig=False)
F.plot(H,color_scheme='cyan',cmap='Greens',dot_size=100,alpha=1.0-H.frac_paths()/3,new_fig=False)

F.save_fig()

##

S = auto_inorm_frame(S1,first=f,norm_off1=pi/2,intersect_tol=0.001,show_intersect=True)

T = S.select(S.s<0)
S = S.select(S.s>=0)

TT = T.select(-T.s <= npts*step)

H = SpiroData()
for i in range(0,npts*step,step):
    H.load(array([S1.xy(i)]))
    H.load(array([S1.xy(i+f)]))

F.plot(S1,color_scheme='cyan',dot_size=1,new_fig=True)
F.plot(TT.select(TT.s % step == step-1),color_scheme='white',cmap='turbo',dot_size=1,alpha=1,new_fig=False)
F.plot(S.select(slice(0,npts*step,step)),color_scheme='orange',dot_size=40,new_fig=False)
F.plot(S,color_scheme='orange',dot_size=0.5,new_fig=False)
F.plot(H,color_scheme='cyan',cmap='Greens',dot_size=100,alpha=1.0-H.frac_paths()/3,new_fig=False)

F.save_fig()

##

f=S1.n()//10

npts = 3
step = 43

S = auto_inorm_frame(S1,first=f,norm_off1=pi/9,norm_off2=pi/10,intersect_tol=0.001,show_intersect=True)

T = S.select(S.s<0)
S = S.select(S.s>=0)

TT = T.select(-T.s <= npts*step)

H = SpiroData()

for i in range(0,npts*step,step):
    H.load(array([S1.xy(i)]))
    H.load(array([S1.xy(i+f)]))

F.plot(S1,color_scheme='cyan',dot_size=1,new_fig=True)
F.plot(TT.select(TT.s % step == step-1),color_scheme='white',cmap='turbo',dot_size=1,alpha=1,new_fig=False)
F.plot(S.select(slice(0,npts*step,step)),color_scheme='orange',dot_size=40,new_fig=False)
F.plot(S,color_scheme='orange',dot_size=0.5,new_fig=False)
F.plot(H,color_scheme='cyan',cmap='Greens',dot_size=100,alpha=1.0-H.frac_paths()/2,new_fig=False)

F.save_fig()

##

f=S1.n()//10

npts = 3
step = 43

S = auto_inorm_frame(S1,first=f,norm_off1=0,base=0.5,norm_off2=0,intersect_tol=0.001,show_intersect=True)

T = S.select(S.s<0)
S = S.select(S.s>=0)

TT = T.select(-T.s <= npts*step)

H = SpiroData()

for i in range(0,npts*step,step):
    H.load(array([S1.xy(i)]))
    H.load(array([S1.xy(i+f)]))

F.plot(S1,color_scheme='cyan',dot_size=1,new_fig=True)
F.plot(TT.select(TT.s % step == step-1),color_scheme='white',cmap='turbo',dot_size=1,alpha=1,new_fig=False)
F.plot(S.select(slice(0,npts*step,step)),color_scheme='orange',dot_size=40,new_fig=False)
F.plot(S,color_scheme='orange',dot_size=0.5,new_fig=False)
F.plot(H,color_scheme='cyan',cmap='Greens',dot_size=100,alpha=1.0-H.frac_paths()/2,new_fig=False)

F.save_fig()

###

R = 50
ppl = 1000
a = R/3.0

S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.5*a),loops=1,ppl=ppl,inside=True,reverse=False)

f=S1.n()//3

npts = 10
step = 13

S = auto_inorm_frame(S1,first=f,norm_off1=0,base=0.5,amp=0.6,rate=8,
                     norm_off2=0,intersect_tol=0.001,show_intersect=True)

T = S.select(S.s<0)
S = S.select(S.s>=0)

TT = T.select(-T.s <= npts*step)

H = SpiroData()

for i in range(0,npts*step,step):
    H.load(array([S1.xy(i)]))
    H.load(array([S1.xy(i+f)]))

F.plot(S1,color_scheme='cyan',dot_size=1,new_fig=True)
F.plot(TT.select(TT.s % step == step-1),color_scheme='white',cmap='turbo',dot_size=1,alpha=1,new_fig=False)
F.plot(S.select(slice(0,npts*step,step)),color_scheme='orange',dot_size=40,new_fig=False)
F.plot(S,color_scheme='orange',dot_size=0.5,new_fig=False)
F.plot(H,color_scheme='cyan',cmap='Greens',dot_size=100,alpha=1.0-H.frac_paths()/2,new_fig=False)

F.save_fig()

###

R = 50
ppl = 1000
a = R/3.0

S1 = cIc(ring=Ring(R),wheel=Wheel(a,1.5*a),loops=1,ppl=ppl,inside=True,reverse=False)

f=S1.n()//2

npts = 10
step = 10

S = auto_inorm_frame(S1,first=f,norm_off1=0,base=0.0,amp=0.0,rate=8,norm_off2=-pi/2,show_intersect=True)

T = S.select(S.s<0)
S = S.select(S.s>=0)

TT = T.select(-T.s <= npts*step)

H = SpiroData()

for i in range(0,npts*step,step):
    H.load(array([S1.xy(i)]))
    H.load(array([S1.xy(i+f)]))

a=1.5
F.plot(S1,color_scheme='cyan',dot_size=1,new_fig=True,limits=[-a*R,a*R,-a*R,a*R])
F.plot(TT.select(TT.s % step == step-1),color_scheme='white',cmap='turbo',dot_size=1,alpha=1,new_fig=False)
F.plot(S.select(slice(0,npts*step,step)),color_scheme='orange',dot_size=40,new_fig=False)
F.plot(S,color_scheme='orange',dot_size=0.5,new_fig=False)
F.plot(H,color_scheme='cyan',cmap='Greens',dot_size=100,alpha=1.0-H.frac_paths()/2,new_fig=False)

F.save_fig()
