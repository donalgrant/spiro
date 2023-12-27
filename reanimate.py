import sys
sys.path.append('../..')
sys.path.append('../')
sys.path.append('./')

import SpiroData
from SpiroData import *

import SpiroDraw
from SpiroDraw import *
import argparse

import imageio
import glob

def print_list(l):
    j = 1
    for i in l:
        print(i,', ',end="")
        if j % 8 == 0:  print()
        j+=1
    if not j%8==1: print()

F=SpiroFig()
F.text_color='white'

parser = argparse.ArgumentParser(description="3D animate a stored pickle file")
parser.add_argument("file", help="input data file(s)", nargs='+')
parser.add_argument("--cmap", help="comma-separated list of colormaps")
parser.add_argument("--all_cmaps", help="replot with every available color map", action="store_true")
parser.add_argument("--cs", help="comma-separated list of color schemes")
parser.add_argument("--all_cs", help="replot with every available color scheme", action="store_true")
parser.add_argument("--cmap_list", help="list all colormap options", action="store_true")
parser.add_argument("--cs_list", help="list all color scheme options", action="store_true")
parser.add_argument("--full_res", help="use high-definition mode", action="store_true")
parser.add_argument("--fd", help="figure dimensions (10 by default, 30 for high-def")
parser.add_argument("--dpi", help="dots per inch for png (150 by default)", type=int)
parser.add_argument("--subsample", help="choose every n'th point", type=int)
parser.add_argument("--dither", help="random color choice:  0 is default, 0.1 typical, 1 is large")
parser.add_argument("--dot_size", help="size of each dot; 0.1 by default, 10 typical for subsampled dot version")
parser.add_argument("--alpha", help="transparency; 0.4 by default, 1 is max, 0.0 is invisible")
parser.add_argument("--new_cmap", help="comma-separated list of (xkcd:) colors for colormap generation")
parser.add_argument("--nrotY", help="number of rotations around the Y axis")
parser.add_argument("--nrotX", help="number of rotations around the X axis")
parser.add_argument("--nsteps", help="number of images to generate", type=int)

args = parser.parse_args()

if args.cs_list:
    print_list(cs_list())
    quit()

if args.cmap_list:
    print_list(cmap_list())
    quit()

cmap = []
cs   = []

if args.new_cmap is not None:
    clist = [ 'xkcd:'+i for i in args.new_cmap.split(',') ]
    cmap.extend(cmap_from_list(clist,cname='new_cmap').name)

if args.all_cmaps:  cmap.extend(cmap_list())
if args.all_cs:       cs.extend(cs_list())

if not args.cmap is None:
    cmap.extend(args.cmap.split(','))

if not args.cs is None:
    cs.extend(args.cs.split(','))
    
cmap = ['Oranges'] if len(cmap)==0 else cmap
cs   = ['cycles']  if len(cs)==0   else cs

ss   = 5           if args.subsample is None else args.subsample
fd   = 10          if args.fd        is None else args.fd
dpi  = 150         if args.dpi       is None else args.dpi
ds   = 0.1         if args.dot_size  is None else float(args.dot_size)
alpha = 0.4        if args.alpha     is None else float(args.alpha)
dither=0.0         if args.dither    is None else float(args.dither)
nsteps=60          if args.nsteps    is None else args.nsteps
nrotX=0.0          if args.nrotX      is None else float(args.nrotX)
if nrotX==0:
    nrotY = 1.0 if args.nrotY is None else float(args.nrotY)
else:
    nrotY = 0.0 if args.nrotY is None else float(args.nrotY)

if args.full_res:
    ss = 1
    fd = 30
    dpi = 300

for data_file in args.file:
    print(f'3D animating {data_file}')
    S = SpiroData.read(data_file).subsample(ss)
    for cmap_i in cmap:
        cmap_name = cmap_name.name if hasattr(cmap_i,'name') else cmap_i
        for cs_i in cs:

            print(f'Animating and saving {data_file} with dot_size={ds}, alpha={alpha}')
            print(f'Rotate about Y by {nrotY} rotations and about X by {nrotX} rotations')

            theta = linspace(0,2*pi*nrotY,nsteps)

            l1 = min(S.x)
            l2 = max(S.x)
            l3 = min(S.y)
            l4 = max(S.y)

            xscale=l2-l1
            
            for i in range(nsteps):
                if i%10==0:  print(i)

                xyz=rotY(S.xyp(scale=xscale),theta[i])
                
                x = xyz[:,0]
                y = xyz[:,1]
                z = xyz[:,2]

                U = SpiroData.SpiroData()

                fnz = str(i).zfill(4)
                filename=f'{data_file}-animate-{fnz}.png'

                F.plot(U.set_array(x,y,S.p,S.t),cmap=cmap_i,color_scheme=cs_i,fig_dim=fd,alpha=alpha,
                       dot_size=ds,color_dither=dither,limits=[l1,l2,l3,l4],
                       transparent=False,save=True,filename=filename)
            
            images=[]
            filelist=glob.glob(f'{data_file}-animate-*.png')
            for image in sorted(filelist):
                images.append(imageio.imread(image))
            for image in sorted(filelist,reverse=True):
                images.append(imageio.imread(image))

            imageio.mimsave(f'{data_file}-animate.gif',images,duration=0.2,loop=0)
