import matplotlib.pyplot as plt
import SpiroData
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array,linspace
import scipy

from pathlib import Path

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

def cmap_from_list(clist,cname=None):
    if cname is None:
        cname=''
        for c in clist: cname+=c[:2]
    cmap=LinearSegmentedColormap.from_list(cname,clist)
    mpl.colormaps.register(cmap=cmap)
    return cmap

cmap1 = cmap_from_list(["Red","Orange","hotpink"],'cmap1')
cmap2 = cmap_from_list(["rebeccapurple","darkmagenta","orchid","pink"],'cmap2')
cmap3 = cmap_from_list(["seagreen","teal","cornflowerblue","mediumblue","indigo"],'cmap3')


cyans = cmap_from_list(["xkcd:dark aqua","xkcd:dark cyan","xkcd:cyan","xkcd:light cyan","xkcd:ice"],'cyans')

clist = [ 'xkcd:'+i for i in ['sapphire','vibrant blue','carolina blue','navy blue','azul','sapphire'] ]
pretty_blues = cmap_from_list(clist,'pretty_blues')

clist = [ 'xkcd:'+i for i in ['blood red','raw umber','light forest green','forest green'] ]
wreath = cmap_from_list(clist,'wreath')

clist = [ 'xkcd:'+i for i in ['dark gold','gold','dark gold','muddy green','dark gold'] ]
gold = cmap_from_list(clist,'gold')

clist = [ 'xkcd:'+i for i in ['kelly green','light green','vivid green','grass green'] ]
emerald_woman= cmap_from_list(clist,'emerald_woman')

clist = [ 'xkcd:'+i for i in ['carnation pink','baby pink','lipstick red','darkish pink','powder pink'] ]
pinks = cmap_from_list(clist,'pinks')

clist = [ 'xkcd:'+i for i in ['lavender pink','pale mauve','pinky purple','purpleish','lavender pink'] ]
pale_pink = cmap_from_list(clist,'pale_pink')

clist = [ 'xkcd:'+i for i in ['red','crimson','fire engine red','dull red','carnation',
                              'lipstick red','bright red','blood red','red'] ]
pretty_reds = cmap_from_list(clist,'pretty_reds')

def cmap_list():
    return ['pretty_blues','wreath','gold','emerald_woman','pinks','pale_pink',
            'cmap1','cmap2','cmap3','cyans',
            'viridis','magma','inferno','plasma','cividis',
            'spring','summer','winter','autumn','Wistia','cool',
            'hot','gist_heat','copper',
            'Dark2','tab10','tab20','tab20b','Set1','Set2','Set3',
            'Pastel1','Pastel2','Paired','Accent',
            'ocean','terrain','gist_earth','gist_stern','prism',
            'turbo','gnuplot','brg','gist_rainbow','rainbow','jet',
            'nipy_spectral','gist_ncar',
            'bone','twilight','twilight_shifted','hsv',
            'Greys','Purples','Blues','Greens','Oranges','Reds','YlOrBr',
            'YlOrRd','OrRd','PuRd','RdPu','BuPu','GnBu','PuBu',
            'YlGnBu','PuBuGn','BuGn','YlGn'
            ]

# would like a better way to capture the color_scheme name with the encoding in a single
# place, rather than both here and in the match statement.

def cs_list():
    return ['radial','cycles','phase','spacing','fspacing','direction','x-direction','y-direction',
            'polar','time','length','length_r','random',
            'width','fwidth','lengths','flengths','fradii','fpolars',
            'dir_to_frm','dist_to_frm','dir_off_frm',
            'fcdist3','fcdist4','fcdist5','fcdist6','fcdist7',
            'cdist3','cdist4','cdist5','cdist6','cdist7',
            'fcdirs3','fcdirs4','fcdirs5','fcdirs6','fcdirs7',
            'cdirs3','cdirs4','cdirs5','cdirs6','cdirs7',
            'x','xrand','y','yrand','rrand', # 'prand','crand','drand','srand',  # add these?
            'xy','x+y','x-y','h-waves','t-waves','l-waves','v-waves',
            'r-waves','ripples','s-ripples'
            ]

def apply_dither(c,dfactor):
    if dfactor==0: return c
    spread = max(c)-min(c)
    g = np.random.standard_normal(len(c))*spread*dfactor
    return c+g

class SpiroFig:

    def new_fig(self,no_frame=True,fig_dim=10,limits=None,**kw_args):
        
        n_subs = self.rows*self.cols
        expansion = int(sqrt(n_subs))*10
        sub_expansion = expansion / 2 if expansion > 20 else fig_dim
        if self.multi:
            self._fig = plt.figure(figsize=(expansion,expansion),facecolor=(.0, .0, .0))
            self._fig, self.ax = plt.subplots(self.rows,self.cols,
                                              figsize=(sub_expansion,sub_expansion),
                                              facecolor=(.0, .0, .0),
                                              layout='compressed')
            self.plot_num=0
            for i in range(self.rows):
                for j in range(self.cols):
                    self.ax[i,j].set(aspect=1)
                    if no_frame:
                        self.ax[i,j].set(xticks=[], yticks=[])
                        self.ax[i,j].set_axis_off()
                    else:
                        self.ax[i,j].tick_params(labelcolor='white')
            return self.ax
                                                
        else:
            self._fig = plt.figure(figsize=(fig_dim,fig_dim),facecolor='black')
            self.ax=self._fig.add_subplot(frameon=False)
            self.ax.set(aspect=1)
            if no_frame:
                self.ax.set(xticks=[],yticks=[])
                self.ax.set_axis_off()
            else:
                self.ax.tick_params(labelcolor='white')
            if not limits is None:
                self.ax.set_xlim([limits[0],limits[1]])
                self.ax.set_ylim([limits[2],limits[3]])
                                 
            return self.ax
        
    def __init__(self,ax=None,savepath='./',rows=1,cols=1):
        self._path=savepath
        Path(savepath).mkdir(parents=True, exist_ok=True)
        self._figname='Figure-'
        self.ax=ax
        self.fig_number=0
        self.text_color='white'
        self.ok_save()
        self.rows=rows
        self.cols=cols
        self.multi = True if self.rows*self.cols > 1 else False

        self.set_default_dpi(100)
        self.set_default_cmap('viridis')
        self.set_default_color_scheme('radial')
        
    def set_default_dpi(self,dpi):  self.dpi=dpi
    def set_default_cmap(self,color):  self.cmap=color
    def set_default_color_scheme(self,cs):  self.cs=cs

    def plot_row(self):  return self.plot_num // self.cols
    def plot_col(self):  return self.plot_num % self.cols

    def plot(self,sd,cmap=None,color_scheme=None,
             dot_size=0.1,linestyle='',alpha=1.0, color_dither=0.0, coord_dither=0.0,
             subsample=None,no_frame=True, fig_dim=10, save=False, no_multi_inc=False,
             new_fig=True,smooth=False, caption='', fontsize=18, rgb=None, limits=None,
             filename=None, transparent=True):

        if new_fig or self.ax is None or (self.multi and not self.ax.any):
            self.new_fig(no_frame=no_frame,fig_dim=fig_dim,limits=limits)

        if coord_dither > 0.0:
            dr = np.random.standard_normal(sd.n())
            dt = np.random.uniform(0,2*pi,sd.n())
            sd.x += coord_dither*dr*cos(dt)
            sd.y += coord_dither*dr*sin(dt)
            
        r = sqrt(sd.x**2+sd.y**2)

        if color_scheme is None:  color_scheme=self.cs
        if cmap         is None:  cmap        =self.cmap

        if hasattr(color_scheme,"__len__") and len(color_scheme)==sd.n():
            clr=color_scheme
        else:
            match color_scheme:
                case 'radial':    clr=r
                case 'object':    clr=sd.o
                case 'segment':   clr=sd.s
                case 'cycles':    clr=sin(sd.p)
                case 'phase':     clr=sd.p
                case 'polar':     clr=arctan2(sd.x,sd.y)
                case 'x-direction': clr=cos(scipy.signal.medfilt(sd.directions()))
                case 'y-direction': clr=sin(scipy.signal.medfilt(sd.directions()))
                case 'direction': clr=scipy.signal.medfilt(sd.directions())
                case 'spacing':   clr=scipy.signal.medfilt(sd.neighbor_distances())
                case 'fspacing':  clr=scipy.signal.medfilt(sd.fneighbor_distances())
                case 'time':      clr=sd.t
                case 'length':    clr=linspace(0,sd.x.shape[0],sd.x.shape[0])
                case 'length_r':  clr=linspace(sd.x.shape[0],0,sd.x.shape[0])
                case 'random':    clr=np.random.rand(len(sd.x)) 
                case 'x':         clr=sd.x
                case 'xrand':     clr=sd.x+np.random.normal(0,max(sd.x)/3,sd.n())
                case 'y':         clr=sd.y
                case 'yrand':     clr=sd.y+np.random.normal(0,max(sd.y)/3,sd.n())
                case 'rrand':     clr=r+np.random.normal(0,max(r)/3,sd.n())
                case 'xy':        clr=sd.x*sd.y
                case 'x+y':       clr=sd.x+sd.y
                case 'x-y':       clr=sd.x-sd.y
                case 'h-waves':   clr=sin(sd.x)
                case 't-waves':   clr=sin(sd.t/max(sd.t)*4*pi)
                case 'l-waves':   clr=sin(linspace(0,4*pi,sd.n()))
                case 'v-waves':   clr=sin(sd.y)
                case 'r-waves':   clr=sin(r)
                case 'ripples':   clr=sin(r**2)
                case 's-ripples': clr=sin(sqrt(r))
                case 'fpolars':   clr=sd.fpolars()
                case 'fradii':    clr=sd.fradii()
                case 'width':     clr=sd.chord_dists(sd.n()//2)
                case 'fwidth':    clr=sd.fchord_dists(sd.n()//2)
                case 'lengths':   clr=sd.lengths()
                case 'flengths':  clr=sd.flengths()
                case 'dir_to_frm':  clr=sd.directions_to_frame()
                case 'dist_to_frm': clr=sd.dists_to_frame()
                case 'dir_off_frm': clr=sd.dirs_off_frame()
                case 'fcdist3':   clr=sd.fchord_dists(sd.n()//3)  # would love to parse for the digit
                case 'fcdist4':   clr=sd.fchord_dists(sd.n()//4)
                case 'fcdist5':   clr=sd.fchord_dists(sd.n()//5)
                case 'fcdist6':   clr=sd.fchord_dists(sd.n()//6)
                case 'fcdist7':   clr=sd.fchord_dists(sd.n()//7)
                case 'fcdirs3':   clr=sd.fchord_dirs(sd.n()//3)  # would love to parse for the digit
                case 'fcdirs4':   clr=sd.fchord_dirs(sd.n()//4)
                case 'fcdirs5':   clr=sd.fchord_dirs(sd.n()//5)
                case 'fcdirs6':   clr=sd.fchord_dirs(sd.n()//6)
                case 'fcdirs7':   clr=sd.fchord_dirs(sd.n()//7)
                case 'cdist3':    clr=sd.chord_dists(sd.n()//3)  # would love to parse for the digit
                case 'cdist4':    clr=sd.chord_dists(sd.n()//4)
                case 'cdist5':    clr=sd.chord_dists(sd.n()//5)
                case 'cdist6':    clr=sd.chord_dists(sd.n()//6)
                case 'cdist7':    clr=sd.chord_dists(sd.n()//7)
                case 'cdirs3':    clr=sd.chord_dirs(sd.n()//3)  # would love to parse for the digit
                case 'cdirs4':    clr=sd.chord_dirs(sd.n()//4)
                case 'cdirs5':    clr=sd.chord_dirs(sd.n()//5)
                case 'cdirs6':    clr=sd.chord_dirs(sd.n()//6)
                case 'cdirs7':    clr=sd.chord_dirs(sd.n()//7)
                
                case _:
                    clr=color_scheme
                    cmap=None
        
        if subsample:
            x = sd.x[::subsample]
            y = sd.y[::subsample]
            t = sd.t[::subsample]
            p = sd.p[::subsample]
            clr = clr[::subsample]
        else:
            x = sd.x
            y = sd.y
            t = sd.t
            p = sd.p

        if self.multi:
            row = self.plot_row()
            col = self.plot_col()
            ax = self.ax[row,col]
        else:
            ax = self.ax
            
        if (smooth):
            if color_scheme=='radial':  clr='blue'
            ax.plot(x,y,color=clr)
        else:
            if rgb is None:
                self.scat = ax.scatter(x,y,c=apply_dither(clr,color_dither),linestyle=linestyle,s=dot_size,
                                       cmap=cmap,alpha=alpha)
            else:
                print('color is: ',rgb)
                self.scat = ax.scatter(x,y,color=rgb,linestyle=linestyle,s=dot_size,alpha=alpha)
                

        if len(caption) > 0:
            ax.set_title(caption,color=self.text_color,y=-0.1,fontsize=fontsize)
#            self._fig.text(1.0, 0.05, 'David A. Imel 2023', ha='right',
#                           color=self.text_color)
        if self.multi and not no_multi_inc:
            self.plot_num+=1
        
        if save:
            self.save_fig(filename=filename,transparent=transparent)

    def caption(self,text):
        if self.multi:
            self._fig.suptitle(text,color=self.text_color,fontsize=22)
        else:
            self._fig.text(0.4, 0.05, text, ha='left',color=self.text_color)

    def no_save(self):  self.allow_save=0
    def ok_save(self):  self.allow_save=1
    
    def save_fig(self,filename=None,dpi=None,transparent=True):

        if dpi is None:  dpi = self.dpi
        if self.allow_save:
            if filename is None:
                fnz = str(self.fig_number).zfill(4)
                filename=self._path+self._figname+f'{fnz}.png'
            self._fig.savefig(filename,bbox_inches='tight',
                              transparent=transparent,dpi=dpi)
            self.close()
        
        self.fig_number+=1
        if self.multi: self.plot_num=0     # reset the counter

    def close(self):  plt.close(self._fig)
