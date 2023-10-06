import matplotlib.pyplot as plt
import SpiroData
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array,linspace

from pathlib import Path

import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
cmap1 = LinearSegmentedColormap.from_list("RedOrangePink",["Red","Orange","Pink"])
cmap2 = LinearSegmentedColormap.from_list("Pinks",["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = LinearSegmentedColormap.from_list("DarkGreen",["seagreen","teal","cornflowerblue","mediumblue","indigo"])

def cmap_list():
    return ['viridis','magma','inferno','plasma','cividis',
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

def cmap_from_list(clist,cname=None):
    if cname is None:
        cname=''
        for c in clist: cname+=c[:2]
    return LinearSegmentedColormap.from_list(cname,clist)

cmap1 = cmap_from_list(["Red","Orange","hotpink"])
cmap2 = cmap_from_list(["rebeccapurple","darkmagenta","orchid","pink"])
cmap3 = cmap_from_list(["seagreen","teal","cornflowerblue","mediumblue","indigo"])

# would like a better way to capture the color_scheme name with the encoding in a single
# place, rather than both here and in the match statement.

def cs_list():
    return ['radial','cycles','polar','time','length','random',
            'x','xrand','y','yrand','rrand','xy','x+y',
            'x-y','h-waves','t-waves','l-waves','v-waves',
            'r-waves','ripples','s-ripples'
            ]

class SpiroFig:

    def new_fig(self,no_frame=True,**kw_args):
        
        n_subs = self.rows*self.cols
        expansion = int(sqrt(n_subs))*10
        sub_expansion = expansion / 2 if expansion > 20 else 10
        if self.multi:
            self._fig = plt.figure(figsize=(expansion,expansion))
            self._fig, self.ax = plt.subplots(self.rows,self.cols,
                                              figsize=(sub_expansion,sub_expansion),
                                                layout='compressed')
            self.plot_num=0
            for i in range(self.rows):
                for j in range(self.cols):
                    self.ax[i,j].set(aspect=1)
                    if no_frame:
                        self.ax[i,j].set(xticks=[], yticks=[])
                        self.ax[i,j].set_axis_off()
            return self.ax
                                                
        else:
            self._fig = plt.figure(figsize=(10,10))
            self.ax=self._fig.add_subplot(frameon=False)
            self.ax.set(aspect=1)
            if no_frame:
                self.ax.set(xticks=[],yticks=[])
                self.ax.set_axis_off()
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
             dot_size=0.1,linestyle='',alpha=1.0,
             subsample=None,no_frame=True, save=False, no_multi_inc=False,
             new_fig=True,smooth=False, caption='', fontsize=18):

        if new_fig or self.ax is None or (self.multi and not self.ax.any):
            self.new_fig(no_frame=no_frame)

        r = sqrt(sd.x**2+sd.y**2)

        if color_scheme is None:  color_scheme=self.cs
        if cmap         is None:  cmap        =self.cmap
        
        match color_scheme:
            case 'radial':    clr=r
            case 'cycles':    clr=sin(sd.p)
            case 'polar':     clr=arctan2(sd.x,sd.y)
            case 'time':      clr=sd.t
            case 'length':    clr=linspace(0,sd.x.shape[0],sd.x.shape[0])
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
            ax.scatter(x,y,c=clr,linestyle=linestyle,s=dot_size,
                       cmap=cmap,alpha=alpha)

        if len(caption)>0:
            ax.set_title(caption,color=self.text_color,y=-0.1,fontsize=fontsize)
#            self._fig.text(1.0, 0.05, 'David A. Imel 2023', ha='right',
#                           color=self.text_color)
        if self.multi and not no_multi_inc:
            self.plot_num+=1
        
        if save:
            self.save_fig()

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
                filename=self._path+self._figname+f'{self.fig_number}.png'
            self._fig.savefig(filename,bbox_inches='tight',
                              transparent=transparent,dpi=dpi)
            self.close()
        
        self.fig_number+=1
        if self.multi: self.plot_num=0     # reset the counter

    def close(self):  plt.close(self._fig)
