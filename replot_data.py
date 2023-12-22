import sys
sys.path.append('../..')
sys.path.append('../')
sys.path.append('./')

import SpiroData
from SpiroData import *
import SpiroDraw
from SpiroDraw import *
import argparse

def print_list(l):
    j = 1
    for i in l:
        print(i,', ',end="")
        if j % 8 == 0:  print()
        j+=1
    if not j%8==1: print()

F=SpiroFig()
F.text_color='white'

parser = argparse.ArgumentParser(description="replot stored pickle file")
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
cs   = ['length']  if len(cs)==0   else cs

ss   = 5           if args.subsample is None else args.subsample
fd   = 10          if args.fd        is None else args.fd
dpi  = 150         if args.dpi       is None else args.dpi
ds   = 0.1         if args.dot_size  is None else float(args.dot_size)
alpha = 0.4        if args.alpha     is None else float(args.alpha)
dither=0.0         if args.dither    is None else float(args.dither)

if args.full_res:
    ss = 1
    fd = 30
    dpi = 300
    
for data_file in args.file:
    print(f'replotting {data_file}')
    S = SpiroData.read(data_file)
    for cmap_i in cmap:
        cmap_name = cmap_name.name if hasattr(cmap_i,'name') else cmap_i
        for cs_i in cs:
            filename=f'{data_file}-{cmap_name}-{cs_i}-ss{ss}-fd{fd}-cd{dither}.png'
            print(f'Plotting and saving {filename} with dot_size={ds}, alpha={alpha}')
            F.plot(S.subsample(ss),cmap=cmap_i,color_scheme=cs_i,fig_dim=fd,alpha=alpha,
                   dot_size=ds,color_dither=dither)
            F.save_fig(filename,dpi=dpi)
