import matplotlib.pyplot as plt
import SpiroData
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array,linspace

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
            'YlOrRd','OrRd','PuRd','RdPu','BuPu','GnBu','PuBu','YlGnBu','PuBuGn','BuGn','YlGn'
            ]

class SpiroFig:

    def new_fig(self,no_frame=True,**kw_args):
        self._fig = plt.figure(figsize=(10,10))
        self._ax=self._fig.add_subplot(frameon=False)
        self._ax.set(aspect=1)
        if no_frame:
            self._ax.set(xticks=[],yticks=[])
            self._ax.set_axis_off()
        return self._ax
        
    def __init__(self,ax=None):
        self._ax=ax
        
    def plot(self,sd,cmap='viridis',color_scheme='radial',
             dot_size=0.1,linestyle='',alpha=1.0,
             subsample=None,no_frame=True,
             new_fig=True,smooth=False, caption=False):
        
        if new_fig or not self._ax:  self.new_fig(no_frame=no_frame)

        r = sqrt(sd.x**2+sd.y**2)
        
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

        if (smooth):
            self._ax.plot(x,y)
        else:
            self._ax.scatter(x,y,c=clr,linestyle=linestyle,s=dot_size,cmap=cmap,alpha=alpha)

        if caption:
            self._fig.text(0.0, 0.05, f'{color_scheme} Color Scheme, {cmap} color map', ha='left')
            self._fig.text(1.0, 0.05, 'David A. Imel 2023', ha='right')

    def caption(self,text):
        self._fig.text(0.4, 0.05, text, ha='left')
        
    def save_fig(self,filename='spiro.png'):
        self._fig.savefig(filename,bbox_inches='tight',transparent=True)

    def close(self):  plt.close(self._fig)
