from SpiroData import *
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array
from Wheel import *
from Ellipse import *
from Ring import *
from spiro import *

def line(coords,npts=20):

    sd = SpiroData()
    
    if abs(coords[1,0]-coords[0,0]) < 1.0e-8:
        x = np.linspace(0,npts) * 0 + coords[0,0]
        y = np.linspace(coords[0,1],coords[1,1],npts)
    else:
        x = np.linspace(coords[0,0],coords[1,0],npts)
        y = coords[0,1] + (coords[1,1]-coords[0,1]) / (coords[1,0]-coords[0,0]) * (x - coords[0,0])
    
    # (sd.x,sd.y,sd.t,sd.p) = (x,y,x*0,x*0)
    
    for i in range(npts):
        sd.add(spiro_arc(x0=x[i],y0=y[i],orient=0,R=0.01,wheel=Wheel(0.01,0.0),loops=1))
    
    return sd

def line_at_angle(center=np.array([0,0]),vert_angle=0.0,length=10.0,npts=20):

    dx = length/2 * sin(vert_angle)
    dy = length/2 * cos(vert_angle)
    
    coords=np.array([ [ center[0]-dx, center[1]-dy ], [ center[0]+dx, center[1]+dy ] ])
        
    return line(coords,npts)

def ring_wheel_diagram(ring=Ring(radius=20,origin=np.array([0,0]),orient=0),wheel=Wheel(4,3.5,0.0),phi0=0,inside=True):

    # Draw the ring
    
    sd = SpiroData()
    sd.add(spiro(ring.r,wheel=Wheel(0.01,0.0,0.0),loops=1))

    # Draw the wheel

    theta_offset = ring.o
    x0 = ring.O[0]
    y0 = ring.O[1]

    iv = -1 if inside else 1
    
    phi = wheel.o
    theta = iv * wheel.c / ring.c * (phi-phi0) + theta_offset

    wheel_center_r = ring.r + iv * wheel.r
    x0_wheel = x0 + wheel_center_r * sin(theta)
    y0_wheel = y0 + wheel_center_r * cos(theta)
    
    sd.add(spiro_arc(x0=x0_wheel,y0=y0_wheel,orient=phi,R=wheel.r,wheel=Wheel(0.01,0.0),loops=1))

    # Mark the center location

    sd.add(spiro_arc(x0=x0_wheel,y0=y0_wheel,orient=0,R=wheel.r/20,wheel=Wheel(0.01,0.0),loops=1))

    # Mark the pen location

    x0_pen = x0_wheel + wheel.m * sin(phi)
    y0_pen = y0_wheel + wheel.m * cos(phi)

    sd.add(spiro_arc(x0=x0_pen,y0=y0_pen,orient=0,R=0.01,wheel=Wheel(0.01,0.0),loops=1))

    # draw a line from center to pen location

    sd.add(line(np.array([ [x0_wheel,y0_wheel],[x0_pen,y0_pen] ])))
        
    return sd

def ring_ellipse_diagram(ring=Ellipse(20,0.5),wheel=Wheel(4,3,0.0),phi0=0,inside=True):

    # Draw the ring
    
    sd = SpiroData()
    sd.add(wheel_in_ellipse(wheel=Wheel(0.01,0.0),ellipse=ring,loops=1))

    # Draw the wheel

    theta_offset = ring.o
    x0 = ring.O[0]
    y0 = ring.O[1]

    iv = -1 if inside else 1

    phi = wheel.o

    theta = iv * ring.phi_at_arc(wheel.arc(phi-phi0)) + theta_offset

    # Mark the normal at this theta:  draw a line from ring along the normal

    normal = ring.normal_at_phi(theta)

    xnc = x0 + ring.r(theta)*sin(theta)
    ync = y0 + ring.r(theta)*cos(theta)

    sd.add(line_at_angle(np.array([xnc,ync]),normal,length=wheel.r/2))

    x0_wheel = xnc + iv * wheel.r * sin(normal)
    y0_wheel = ync + iv * wheel.r * cos(normal)
    
    sd.add(spiro_arc(x0=x0_wheel,y0=y0_wheel,orient=phi,R=wheel.r,wheel=Wheel(0.01,0.0),loops=1))

    # Mark the center location

    sd.add(spiro_arc(x0=x0_wheel,y0=y0_wheel,orient=0,R=wheel.r/20,wheel=Wheel(0.01,0.0),loops=1))

    # Mark the pen location

    x0_pen = x0_wheel + wheel.m * sin(phi)
    y0_pen = y0_wheel + wheel.m * cos(phi)

    sd.add(spiro_arc(x0=x0_pen,y0=y0_pen,orient=0,R=0.01,wheel=Wheel(0.01,0.0),loops=1))

    # draw a line from center to pen location

    sd.add(line(np.array([ [x0_wheel,y0_wheel],[x0_pen,y0_pen] ])))

    return sd
