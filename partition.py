import sys
sys.path.append('../..')
import argparse


import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array
from SpiroData import *
from SpiroGeometry import *

def objectify(SA):
    S = SpiroData()
    for Q in SA:  S.add(Q)
    return S

def partition_rings(sd,n,scalex=1.0,prot=0,pad=0):

    SA = []
    
    for i in range(n):
        S = sd.copy().rotate(array_val(prot,i))
        S.scalex(array_val(scalex,i))
        r = S.radii()
        mr = max(r)
        S=S.remove(np.where( r < (i+array_val(pad,i))/n * mr))
        r = S.radii()
        mr = max(r)
        T=S.remove(np.where( r > (i+1-array_val(pad,i))/n * mr))
        T.scalex(1.0/array_val(scalex,i))
        T.rotate(-array_val(prot,i))
        SA.append(T)

    return SA

def partition_azimuth(sd,n,pad=0,min=-pi,max=pi,):
    SA=[]
    dp = (max-min)/n
    for i in range(n):
        S = sd.copy()
        p = S.polars()
        S = S.remove(np.where( p < min + (i+array_val(pad,i)) * dp ))
        p = S.polars()
        T = S.remove(np.where( p > min + (i+1-array_val(pad,i)) * dp ))
        SA.append(T)

    return SA

def partition_panels(sd,n=3,pad=0.1):
    return partition_tiles(sd,nx=n,ny=1,padx=pad,pady=0)

def partition_tiles(sd,nx=1,ny=1,padx=0.0,pady=0.0):

    S=sd.copy()
    SA = []

    minx = min(S.x)
    miny = min(S.y)
    maxx = max(S.x)
    maxy = max(S.y)
    rangex = maxx-minx
    rangey = maxy-miny

    k=0

    for ix in range(nx):
        for iy in range(ny):
            x1 = ix/nx * rangex + minx
            x2 = (ix+1)/nx * rangex + minx
            y1 = iy/ny * rangey + miny
            y2 = (iy+1)/ny * rangey + miny
            j = np.where( (S.x > x1) & (S.x < x2) & (S.y > y1) & (S.y < y2) )
            sd = S.select(j)
            sd = sd.remove(np.where( (sd.x > x1+(1-padx)*rangex/nx) | (sd.x < x1+padx*rangex/nx) |
                                     (sd.y > y1+(1-pady)*rangey/ny) | (sd.y < y1+pady*rangey/ny) ))
            sd.load_meta('tile-xc',(x1+x2)/2)
            sd.load_meta('tile-yc',(y1+y2)/2)
            SA.append(sd)
    
    return SA
