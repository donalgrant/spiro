from SpiroData import *
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array
from Wheel import *
from Ellipse import *
from Ring import *
from spiro import *
from spiro_ellipse import *

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
        sd.add(circle_in_circle(Ring(0.01),W0).move(x[i],y[i]))

    
    return sd

def line_at_angle(center=np.array([0,0]),vert_angle=0.0,length=10.0,npts=20):

    dx = length/2 * sin(vert_angle)
    dy = length/2 * cos(vert_angle)
    
    coords=np.array([ [ center[0]-dx, center[1]-dy ], [ center[0]+dx, center[1]+dy ] ])
        
    return line(coords,npts)

def ring_wheel_diagram(ring=Ring(radius=20,origin=np.array([0,0]),orient=0),
                       wheel=Wheel(4,3.5,0.0),phi0=0,inside=True):

    # Draw the ring
    
    sd = SpiroData()
    sd.add(spiro(ring,wheel=Wheel(0.01,0.0,0.0),loops=1))

    # Draw the wheel

    theta_offset = ring.o

    iv = -1 if inside else 1
    
    phi = wheel.o
    theta = iv * wheel.c / ring.c * (phi-phi0) + theta_offset

    normal = theta
    
    wheel_center_r = ring.r + iv * wheel.r
    x0_wheel = wheel_center_r * sin(theta)
    y0_wheel = wheel_center_r * cos(theta)
    
    sd.add(circle_in_circle(Ring(wheel.r,np.array([x0_wheel,y0_wheel]),orient=phi),
                            wheel=W0,loops=1))

    # Mark the center location

    sd.add(circle_in_circle(Ring(wheel.r/20,np.array([x0_wheel,y0_wheel])),
                            wheel=W0,loops=1))

    # Mark the pen location

    x0_pen = x0_wheel + wheel.m * sin(phi+normal)
    y0_pen = y0_wheel + wheel.m * cos(phi+normal)

    sd.add(circle_in_circle(Ring(0.01,np.array([x0_pen,y0_pen])),W0,loops=1))

    # draw a line from center to pen location

    sd.add(line(array([ [x0_wheel,y0_wheel],[x0_pen,y0_pen] ])))
        
    return sd.move(ring.O[0],ring.O[1])

def circle_in_ellipse_diagram(ring=Ellipse(20,0.5),wheel=Wheel(4,3,0.0),
                              phi0=0,inside=True):
    '''Elliptical ring, with a circular wheel.  phi0 is the initial offset of the
    circular wheel.  The current offset of the wheel is used to calculate its
    position.'''
    
    # Draw the ring
    
    sd = SpiroData()

    rframe=Ellipse(major=ring.a,eccen=ring.e)
    sd.add(circle_in_ellipse(rframe,wheel=W0,loops=1))

    # Draw the wheel

    theta_offset = ring.po

    iv = -1 if inside else 1

    phi = wheel.o

    theta = iv * ring.phi_at_arc(wheel.arc(phi-phi0)) + theta_offset

    # Mark the normal at this theta:  draw a line from ring along the normal

    normal = ring.normal_at_phi(theta)

    xnc = ring.r(theta)*sin(theta)
    ync = ring.r(theta)*cos(theta)

    sd.add(line_at_angle(array([xnc,ync]),normal,length=wheel.r/2))

    x0_wheel = xnc + iv * wheel.r * sin(normal)
    y0_wheel = ync + iv * wheel.r * cos(normal)
    
    sd.add(circle_in_circle(Ring(wheel.r,np.array([x0_wheel,y0_wheel]),phi),
                            W0,loops=1))

    # Mark the center location

    sd.add(circle_in_circle(Ring(wheel.r/20,np.array([x0_wheel,y0_wheel]),0),
                            W0,loops=1))
    # Mark the pen location

    x0_pen = x0_wheel + wheel.m * sin(phi+normal)
    y0_pen = y0_wheel + wheel.m * cos(phi+normal)

    sd.add(circle_in_circle(Ring(0.01,np.array([x0_pen,y0_pen]),0),W0,loops=1))
    
    # draw a line from center to pen location

    sd.add(line(array([ [x0_wheel,y0_wheel],[x0_pen,y0_pen] ])))

    sd.rotate(ring.o)
    
    return sd.move(ring.O[0],ring.O[1])

def new_elliptical_diagram(ring=Ring(20),wheel=Ellipse(4,0.7,3,0.0),
                           phi0=0,inside=True):
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    pen_offset should become part of the wheel's attributes
    '''

    iv = -1 if inside else 1
    
    # Draw the ring
    
    sd = SpiroData()
    sd.add(spiro(ring,wheel=Wheel(0.01,0.0,0.0),loops=1))

    # find the elliptical wheel along the ring

    rp = wheel.r(wheel.o)
    arc = wheel.arc(phi0,wheel.o)
    theta = iv * arc / ring.r + ring.o

     # coordinate of contact
    
    cx = ring.r * sin(theta)
    cy = ring.r * cos(theta)

    # mark that point of contact, temporarily...

    sd.add(line_at_angle(array([cx,cy]),theta,wheel.a/4))

    # unrotated ellipse center coord

    ucx = cx + iv * rp * sin(-wheel.o)
    ucy = cy + iv * rp * cos(-wheel.o)

    # unrotated ellipse pen coord

    upx = ucx + wheel.m * sin(wheel.po)
    upy = ucy + wheel.m * cos(wheel.po)

    # normal to ellipse at wheel.o -- must be lined up with ring radial (theta)
    
    normal = wheel.normal_at_phi(wheel.o)

    # rotate ellipse center and pen positions to align normal with ring radial

    ec = rot_about(array([cx,cy]),normal+theta,array([ [ucx,ucy],[upx,upy] ]))

    # Draw the ellipse wheel

    sd.add(circle_in_ellipse(Ellipse(wheel.a,wheel.e,offset=normal+theta,
                                     origin=array([ec[0,0],ec[0,1]])),
                             wheel=W0, loops=1))

    # Mark the center location

    sd.add(circle_in_circle(Ring(wheel.a/20,np.array([ec[0,0],ec[0,1]])),
                            W0,loops=1))

    # draw a line from the center of the ellipse wheel to the pen

    sd.add(line(ec))

    return sd.move(ring.O[0],ring.O[1])

def ee_diagram(ring,wheel,phi0=0,inside=True):
    '''roll an ellipse on the outside (inside if invert=True) of an elliptical arc
    the wheel starts at phi0 -- its rotation from the position lined with the major
    axis of the ring.
    '''

    iv = -1 if inside else 1
    
    # Draw the ring
    
    sd = SpiroData()

    sd.add(circle_in_ellipse(ring,W0))

    # find the elliptical wheel along the ring

    rp = wheel.r(wheel.o)
    arc = wheel.arc(phi0,wheel.o)
    ring_phi = ring.phi_at_arc(iv * arc, ring.po)  # ring.po is initial angle of wheel
    ring_r = ring.r(ring_phi)

    # normal to ellipse at wheel.o -- must be lined up with ring normal at ring_phi
    
    wheel_n = wheel.normal_at_phi(wheel.o)
    ring_n = ring.normal_at_phi(ring_phi)

     # coordinate of contact
    
    cx = ring_r * sin(ring_phi)  # move offsets to the end?
    cy = ring_r * cos(ring_phi)

    # mark that point of contact

    sd.add(line_at_angle(array([cx,cy]),ring_n,wheel.a/4))

    # unrotated ellipse center coord

    ucx = cx + iv * rp * sin(-wheel.o)
    ucy = cy + iv * rp * cos(-wheel.o)

    # unrotated ellipse pen coord

    upx = ucx + wheel.m * sin(wheel.po)
    upy = ucy + wheel.m * cos(wheel.po)

    # rotate ellipse center and pen positions to align normal with ring radial

    ec = rot_about(array([cx,cy]),wheel_n+ring_n,array([ [ucx,ucy],[upx,upy] ]))

    # Draw the ellipse wheel

    sd.add(circle_in_ellipse(Ellipse(wheel.a,wheel.e),
                             W0).rotate(wheel_n+ring_n).move(ec[0,0],ec[0,1]))

    # Mark the center location

    sd.add(circle_in_circle(Ring(wheel.a/20,np.array([ec[0,0],ec[0,1]])),
                            W0,loops=1))

    # draw a line from the center of the ellipse wheel to the pen

    sd.add(line(ec))

    sd.rotate(ring.o)
    
    return sd.move(ring.O[0],ring.O[1])
