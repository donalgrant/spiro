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

import imageio.v2 as imageio
import glob

parser = argparse.ArgumentParser(description="Parallelogram Examples")
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

def figure(S,cs,cmap,alpha=0.4,dot_size=0.1):
    if hd:
        if not hasattr(figure,"data_set"):  figure.data_set=0
        S.save(f'figure-{figure.data_set}.pickle')
        figure.data_set+=1

    F.plot(S,color_scheme=cs,cmap=cmap,alpha=alpha,fig_dim=fd,dot_size=dot_size,save=save)

filename='animate-image.png'

###

cs = 'spacing'
c = 'turbo'

S = SpiroData()
T = cIc(Ring(30),wheel=Wheel(6,17),loops=1,inside=True,ppl=3000).subsample(1)
ppl=T.n()

m = T.n()//50

ne=ppl//12
first=100 # np.random.randint(0,ppl-ne-2)

images=[]

for i in range(m):

    if i % 10 == 0:  print(i,m)
    
    tnd = [ T.direction(j)+pi for j in arange(first,first+ne) ]
    flat_scale = max(tnd)-min(tnd)
    flat=[ 0.2 + 0.6 * (tnd[j]-min(tnd))/flat_scale for j in range(len(tnd)) ]

    eccen_t = [ eccen_from_flat(flat[j]) for j in range(len(flat)) ]
    eccen = [ 0.97 if eccen_t[j]>0.97 else eccen_t[j] for j in range(len(eccen_t)) ]
    major =20
    orient=[ 100*T.neighbor_dist(j) for j in arange(first,first+ne) ]
    
    S = ellipses_on_frame(T,major,eccen,orient,1000*def_factor,first=first,n=ne)

    F.plot(S,color_scheme=cs,cmap=c,alpha=0.4,fig_dim=fd,dot_size=0.1,
           save=True,limits=[-30,70,-30,70],transparent=False,filename=filename)

    images.append(imageio.imread(filename))
    
    first+=1

images.extend(np.flip(images,axis=0))
imageio.mimsave("animate_more_ellipses.gif", images, duration=0.2, loop=0)


###

R1=5
ppl=300
T1 = cIc(Ring(R1),wheel=Wheel(R1/4,R1/3),ppl=ppl,loops=1,inside=True)

skip=1
n=T1.n()//skip
first=0 
offset=n//30
oa=pi/3

m=67 # n//4  # filesize constraint
ao = linspace(0,2*pi,m)
asym = linspace(0.0,0.3,m)
scale=2

cs = 'cycles'
my_cmap = emerald_woman

images=[]

for i in range(m):
    
    if i % 10 == 0:  print(i,m)

    S=pars_on_frame(T1,skip=skip,scale=scale,oangle=oa,n=n,first=first,fh=0.5,fb=0.5,
                    pts=500*def_factor,asym=asym[i],orient_follow=offset,orient=ao[i]).rotate(i*pi/4/m)

    F.plot(S,color_scheme=cs,cmap=my_cmap,alpha=0.4,fig_dim=fd,dot_size=0.1,
           save=True,limits=[-10,10,-10,10],transparent=False,filename=filename)

    images.append(imageio.imread(filename))

images.extend(np.flip(images,axis=0))
imageio.mimsave("animate_green_polygons.gif", images, duration=0.2, loop=0)

###

def_factor=1

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
n  = T2.n()//(nk+gs)
ns = T2.n()//nk 

pts = npts

images=[]

for offset in range(0,2*ns,2):
    k=1
    first1 = k*ns
    first2 = k*ns+offset
    if offset % 20 == 0:
        print(offset,first1,first2,n)
    S=frame_pair(T1,T2,skip1=1,skip2=1,first1=first1,first2=first2,
                 scale=0.5,oangle=pi/2,fb=0.0,fh=0.0,asym=0,orient=pi/2,polyfunc=tcoords,
                 pts=pts,arc_angle=0,object=k,prot=0,vertex_order=None,
                 pin_to_frame1=True,autoscale=True,pinned_vertex=1)

    filename='animate-frame-pair.png'
    F.plot(S,color_scheme='width',cmap='hot_r',alpha=0.4,dot_size=.1,save=True,filename=filename,
          limits=[-35,35,-35,35],transparent=False)
    images.append(imageio.imread(filename))

imageio.mimsave('animate-frame-pair.gif',images,duration=0.06,loop=0)

###

S1 = integral_ellipticals(1,0.7,0.5,min_pen=1.3,rounds=5,circuits=1,ppl=1000)
S2 = S1.copy()

n = S2.n()
print(n)
nv = 60
v = linspace(0,nv-1,nv,dtype=int)
o = 0

pts = 600//nv

S = SpiroData()


fps = 10  # frames per second

images=[]

f0=0
for div in linspace(1,S2.n()-1,n//8,dtype=int):
    print(div)
    S=on_frame(S2,scale=8,oangle=nv,fb=0.5,fh=0.5,asym=0.9,orient=o,
                   polyfunc=ecoords,pts=pts,first=f0,n=n,orient_follow=div,
                   arc_angle=0,object=0,vertex_order=v,
                   pin_coord=None,pin_to_frame=0.0,autoscale=False,pinned_vertex=0)
    
    filename='animate-ie-ellipse-01.png'
    
    F.plot(S,color_scheme='segment',cmap='pretty_reds',alpha=0.4,dot_size=.1,
           save=True,filename=filename,
           limits=[-35,35,-35,35],transparent=False)
    
    images.append(imageio.imread(filename))

images.extend(np.flip(images,axis=0))
imageio.mimsave('animate-ie-ellipse-01.gif',images,duration=1.0/fps,loop=0)
    
###

ppl=800

S1 = cIc(Ring(30),Wheel(5,6),loops=1,ppl=ppl,inside=True)
S2 = cIc(Ring(24),Wheel(4,5),loops=1,ppl=ppl,inside=True).move(15,0)

S1 = S1.resample(S1.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=True,repeat=40)).rotate(pi/5)
S2 = S2.resample(S2.max_path()*frame_sampling(ppl,parm=10,spacing='sinusoid',
                                              deramp=False,repeat=40))
n = S2.n()

nf=n//23+10

nv = 2
v = linspace(0,nv-1,nv,dtype=int)

pts = 400

nn = 600
rp_opts = { 'n': nn, 'parm': 10.0, 'spacing':  ['sinusoid'], 'repeat': 10, 'deramp': True }

aa = pi/5 # [pi/40,pi/5,pi/40,pi/5]


fps = 10  # frames per second
time= 25  # seconds
nframes = fps*time
images=[]

png_file='animate-vituvian-mollusc.png'
gif_file='animate-vituvian-mollusc.gif'

orient = linspace(0,2*pi,nframes)
half_sin=array([ sin(pi*j/nframes) for j in range(nframes) ])
walk = array([ int(half_sin[j]*nframes/2) for j in range(nframes) ]) 

f0 = 0 + walk
f2 = S2.n()//17 + walk
oa = pi/4 + 0.9*pi/4 * half_sin
asym = 0.2 - 0.4 * half_sin
offset = 0.25 * half_sin

rot = linspace(0,2*pi,nframes)

for iframe in range(nframes):
    if iframe % nframes//10 == 0:  print(iframe)
        
    S=SpiroData()

    sc = linspace(1,3,nf)
    T=frame_pair(S1,S2,skip1=1,skip2=1,
                 first1=f0[iframe],
                 first2=f2[iframe],
                 scale=sc,
                 oangle=oa[iframe],
                 fb=offset[iframe],fh=offset[iframe],
                 asym=asym[iframe],
                 orient=orient[iframe],
                 polyfunc=pcoords, 
                 pts=pts,n1=1,n2=nf,arc_angle=aa,object=0,prot=0,vertex_order=None,
                 pin_to_frame1=0.0,autoscale=True,pinned_vertex=0,show_side=None,
                 normal_intersect=True,norm_off1=0.0,norm_off2=0,frame_only=False,
                 intersect_tol=1.0e-1,rp_opts=rp_opts)

    ni=7
    dn=2*pi/11
    for i in range(ni):  S.add(T.rotate(dn))

    S.rotate(-pi/5+rot[iframe])

    ll = 80
    l = [-ll,ll,-ll,ll]
    F.plot(S,color_scheme='time',cmap='twilight',dot_size=0.1,alpha=0.4,
           save=True,filename=png_file,limits=l,transparent=False)

    images.append(imageio.imread(png_file))

imageio.mimsave(gif_file,images,duration=1.0/fps,loop=0)

###  animated autonorm design

R = 50
ppl = 1000
e = 0.0
e_circum=circum(R,semi_minor(R,e))
a = 1/5*e_circum/2/pi
S1 = cIe(ring=Ellipse(R,e),wheel=Wheel(a,2.3*a),
         loops=1,ppl=ppl,inside=True,reverse=True).rotate(pi/7)

f0=S1.n()//11

U=SpiroData()

ns = 1 # 60

n = S1.n() # S1.n()//50

norm = array([ pi/6 + pi/12*sin(2*pi*j/n) for j in range(n) ])

lbox = 3*R
nk = 1
for k in range(nk):
    f = k*S1.n()//nk//4
    for i in range(ns):
        T = auto_inorm_frame(S1,first=f0+f+int(S1.n()/20*i/ns),norm_off1=0,norm_off2=norm,
                             intersect_tol=.2,
                             base=0.0,amp=0.0,rate=10,object=i,n=n).rotate(1*pi*i/ns).valid() 
        for j in range(T.n()):
            T.fx[j]=S1.x[j]
            T.fy[j]=S1.y[j]

        U.add(T)

U = U.valid_in_radius(lbox)

U = U.resample(U.max_path()*frame_sampling(2*ppl,parm=9,spacing='sinusoid',
                                              deramp=True,repeat=30))

n = 2*U.n()//5

o = 0 
pts = 100
aa = -pi/3

nv = 3
v = linspace(0,nv-1,nv,dtype=int)

rp_opts = { 'n': nv*pts, 
            'parm': 9.0,
            'spacing':  ['sinusoid'], 'repeat': 5, 'deramp': False }

offset = 0.5
sc = 15

asym = 0.8 + frame_sampling(n,parm=5,spacing='sinusoid',repeat=5,deramp=True,nocum=True)/6 * 0

fps = 10 
time= 25 
nframes = fps*time
images=[]

png_file = 'animated-autonorm.png'
gif_file = 'animated-autonorm.gif'


ll = 120
l = [-ll,ll,-ll,ll]

for iframe in range(nframes):
    if iframe % nframes//10 == 0:  print(iframe)

    f0 = int(U.n()/nframes * iframe)
    follow = 1 + int(n/2*sin(iframe*pi/nframes))

    nn = n+int(n/2*sin(2*iframe*pi/nframes))
    
    S = on_frame(U,scale=sc,oangle=pi/2,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
                 polyfunc=tcoords,pts=pts,orient_follow=follow,n=nn,vertex_order=[1,2],
                 object=1,arc_angle=aa,rp_opts=rp_opts)

    S.add(on_frame(U,scale=sc,oangle=pi/2,fb=offset,fh=offset,asym=asym,orient=o,first=f0,
             polyfunc=tcoords,pts=pts//5,orient_follow=follow,n=nn-1,vertex_order=[0,1],
             object=1,arc_angle=0,rp_opts=None))

    F.plot(S,color_scheme=S.o+sin(S.t/max(S.t)*2*pi),cmap='Wistia',
           dot_size=0.1,alpha=0.4,limits=l,
           save=True,filename=png_file,transparent=False)
    
    images.append(imageio.imread(png_file))

imageio.mimsave(gif_file,images,duration=1.0/fps,loop=0)


