import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,cos,arctan2,pi,sqrt,tan
import math

def plot_spiro(d,color_scheme='radial',cmap="viridis",ax=None,
               dot_size=0.1,linestyle=''):
    if not ax:
        fig, ax=plt.subplots(figsize=(10,10))
        ax.set(aspect=1,xticks=[], yticks=[])
    
    match color_scheme:
        case 'radial':    c=sqrt(d['x']**2+d['y']**2)
        case 'cycles':    c=sin(d['p'])
        case 'polar':     c=arctan2(d['x'],d['y'])
        case 'time':      c=range(len(d['p']))
        case 'random':    c=np.random.rand(len(d['x']))
        case 'x':         c=d['x']
        case 'y':         c=d['y']
        case 'xy':        c=d['x']*d['y']
        case 'x+y':       c=d['x']+d['y']
        case 'x-y':       c=d['x']-d['y']
        case 'h-waves':   c=sin(d['x'])
        case 'v-waves':   c=sin(d['y'])
        case 'r-waves':   c=sin(sqrt(d['x']**2+d['y']**2))
        case 'ripples':   c=sin((d['x']**2+d['y']**2))
        case 's-ripples': c=sin((d['x']**2+d['y']**2)**(1/4))
        case _:           c=[ 0 for i in range(len(d['x']))]
    
    ax.scatter(d['x'],d['y'],c=c,linestyle=linestyle,s=dot_size,cmap=cmap)

    return ax

def spiro(R=10.0,a=4.0,b=3.5,loops=5,offset=0,spacing=pi/4000):    
    t=np.linspace(0.0,loops*2*pi,int(loops/spacing))
    x=(R-a)*sin(t)-b*sin(t*R/a+offset)
    y=(R-a)*cos(t)+b*cos(t*R/a+offset)
    p=t*R/a+offset    
    return { 'x': x, 'y': y, 'p': p }

def spiro_arc(x0=0,y0=0,orient=0,R=10.0,a=4.0,b=3.5,
              loops=1,offset=0,spacing=pi/4000,invert=False,reverse=False):  
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    Direction of motion can be reversed by setting reverse=True
    '''
    iv = -1 if invert else 1
    t=np.linspace(0.0,2*pi*loops*R/a,int(loops/spacing)) # roll distance
    if reverse: t=-1*t
    x=x0+(R+iv*a)*sin(t*a/R+orient) +iv*b*sin(t+offset)  # should orient come into the argument of the sin?
    y=y0+(R+iv*a)*cos(t*a/R+orient) + b*cos(t+offset)
    p=t+offset 
    
    return { 'x': x, 'y': y, 'p': p }

def spiro_steps(R=10,a=4,b=3.5,loops=1,n=10,offset=pi/10,spacing=pi/2000):
    x=np.array([])
    y=np.array([])
    p=np.array([])
    for i in range(n):
        d=spiro(R,a,b,loops,offset=offset*i,spacing=spacing)
        x=np.append(x,d['x'])
        y=np.append(y,d['y'])
        p=np.append(p,d['p'])
        
    return { 'x': x, 'y': y, 'p': p }

def roll(x1,y1,x2,y2,a,b,offset=0,guard=0,invert=False):
    '''roll in straight line from (x1,y1) to (x2,y2)
    using wheel of diameter a and pen position b.
    offset is the start angle off the vertical for the pen, in radians.
    invert keyword controls sense of wheel location:  default
    is above and/or to the right.  invert=True is the opposite.
    '''
    R=sqrt((x2-x1)**2+(y2-y1)**2) - 2*guard # roll distance
    A=arctan2(y2-y1,x2-x1)                  # roll angle
    t=np.linspace(0,R/a,1000)               # angle through which the wheel rolls

    iv = -1 if invert else 1

    xs=x1-iv*a*sin(A)+guard*cos(A)
    ys=y1+iv*a*cos(A)+guard*sin(A)
        
    x=xs+a*t*cos(A) +iv*b*sin(t+offset)
    y=ys+a*t*sin(A) +   b*cos(t+offset)  # consistent with spiro
        
    return { 'x': x, 'y': y, 'p': t+offset }

def rotate(x0,y0,xr,yr,angle):
    '''rotate the coordinate (xr,yr) about the
    origin (x0,y0) by angle
    '''
    t=np.linspace(0.0,np.abs(angle),int(500*np.abs(angle)/pi))
    r=sqrt((xr-x0)**2+(yr-y0)**2)
    phi=arctan2(xr-x0,yr-y0)
    
    if (angle<0): t*=-1
    
    x=x0+r*sin(t+phi)
    y=y0+r*cos(t+phi)
        
    return { 'x': x, 'y': y, 'p': t+phi  }

def spiro_line(R=60,a=12,b=7.2,loops=60,n=1,fold=False):
        
    x=np.array([])
    y=np.array([])
    p=np.array([])
    
    xc=[-R/2,R/2]
    yc=[0.0,0.0]
    rot_angle=pi
    if (fold): rot_angle = rot_angle - 2*pi
    
    offset=0
    
    for i in range(loops):
        
        for c in range(len(xc)):
        
            cn=(c+1) % len(xc)
            
            d=roll(xc[c],yc[c],xc[cn],yc[cn],a,b,offset)  # cycloids roll
            x=np.append(x,d['x'])
            y=np.append(y,d['y'])
            p=np.append(y,d['p'])
            offset=p[-1]
        
            d=rotate(xc[cn],yc[cn],x[-1],y[-1],rot_angle) # roll over upper right
            x=np.append(x,d['x'])
            y=np.append(y,d['y'])
            p=np.append(y,d['p'])
            offset+=rot_angle
        
    return { 'x': x, 'y': y, 'p': p }

def spiro_eq_triangle(R=60,a=12,b=7.2,loops=60,n=1,fold=False,inside=False):
        
    x=np.array([])
    y=np.array([])
    p=np.array([])
    
    rot_angle=2.0*pi/3.0
    if (fold): rot_angle = rot_angle - 2*pi
    
    ytop = R*sin(pi/3.0)
    
    xc=[-R/2,0,R/2]
    yc=[-ytop/3,2*ytop/3,-ytop/3]
    
    bump = a/(np.tan(np.pi/6)) if inside else 0
    
    offset=0
    
    for i in range(loops):
        
        for c in range(len(xc)):
        
            cn=(c+1) % len(xc)
            
            d=roll(xc[c],yc[c],xc[cn],yc[cn],a,b,offset,guard=bump,invert=inside)  # cycloids roll
            x=np.append(x,d['x'])
            y=np.append(y,d['y'])
            p=np.append(p,d['p'])
            offset=p[-1]
        
            if not inside:
                d=rotate(xc[cn],yc[cn],x[-1],y[-1],rot_angle) # roll over upper right
                x=np.append(x,d['x'])
                y=np.append(y,d['y'])
                p=np.append(p,d['p'])
                offset+=rot_angle
        
        
    return { 'x': x, 'y': y, 'p': p }

def spiro_square(R=60,a=12,b=7.2,loops=60,scatter=False,mono=False,fold=False,inside=False):
        
    x=np.array([])
    y=np.array([])
    p=np.array([])
    
    xc=[-R/2,R/2,R/2,-R/2]
    yc=[R/2,R/2,-R/2,-R/2]
    
    bump = a if inside else 0
    
    rot_angle=pi/2.0
    if (fold): rot_angle = rot_angle - 2*pi
    
    offset=0
    
    for i in range(loops):
        
        for c in range(len(xc)):
        
            cn=(c+1) % len(xc)
            
            d=roll(xc[c],yc[c],xc[cn],yc[cn],a,b,offset,guard=bump,invert=inside)  # cycloids roll
            x=np.append(x,d['x'])
            y=np.append(y,d['y'])
            p=np.append(p,d['p'])
            offset=p[-1]
        
            if not inside:
                d=rotate(xc[cn],yc[cn],x[-1],y[-1],rot_angle) # roll over upper right
                x=np.append(x,d['x'])
                y=np.append(y,d['y'])
                p=np.append(p,d['p'])
                offset+=rot_angle
    
    return { 'x': x, 'y': y, 'p': p }

def heart(x0=0,y0=0,width=40,depth=25,wheel=2.2,pen=1.0,loops=1,offset=0.0,invert=False,
          cmap='inferno',color_scheme='radial',ax=None):

    if not ax:
        fig, ax=plt.subplots(figsize=(10,10))
        ax.set(aspect=1,xticks=[], yticks=[])
        
    d=roll(x0,y0-depth,x0-width/2,y0,wheel,pen,offset=offset)
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    
    d=rotate(x0-width/2,y0,d['x'][-1],d['y'][-1],pi)
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    
    d=spiro_arc(x0-width/4,y0,-pi/2,width/4,wheel,pen,loops=0.5,offset=d['p'][-1])
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    
    d=rotate(x0-width/2,y0,d['x'][-1],d['y'][-1],pi/2)
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    
    d=spiro_arc(x0+width/4,y0,-pi/2,10,wheel,pen,loops=0.5,offset=d['p'][-1])
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    
    d=rotate(x0+width/2,y0,d['x'][-1],d['y'][-1],pi)
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    
    d=roll(x0+width,y0,x0,y0-depth,wheel,pen,offset=d['p'][-1])
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    
    d=rotate(x0,y0-depth,d['x'][-1],d['y'][-1],pi/2)
    plot_spiro(d,ax=ax,cmap=cmap,color_scheme=color_scheme)
    offset=d['p'][-1]
