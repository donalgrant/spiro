from SpiroData import *
import numpy as np
from numpy import sin,cos,arctan2,arccos,pi,sqrt,tan,array
from Wheel import *
from Ellipse import *
from SpiroGeometry import *

def spiro(R=10,wheel=Wheel(4,3.5,0.0),loops=5,
          slide = lambda t: 1,
          spacing=pi/4000,orient=0,inside=True):
    return spiro_arc(x0=0,y0=0,orient=orient,R=R,wheel=wheel,loops=loops,
                     slide=slide,
                     spacing=spacing,invert=True if inside else False,reverse=False)

def wheel_in_ellipse(x0=0,y0=0,wheel=Wheel(4,3.5,0),ellipse=Ellipse(10,0.5,0,0),
              loops=1,pts_per_loop=4000,
              slide = lambda t: 1,
              start_guard=0,end_guard=0,start_guard_angle=0,end_guard_angle=0,
              orient=0,invert=False,reverse=False):  
    '''roll on the outside (inside if invert=True) of an elliptical arc
    centered on x0, y0.  Direction of motion can be reversed by setting reverse=True
    '''
    
    iv = -1 if invert else 1
    
    sd = SpiroData()

    a = wheel.r
    m = wheel.m
    
    t=np.linspace(0,loops,int(loops*pts_per_loop))
    
    if reverse: t *= -1
    
    p = t * ellipse.c / wheel.c * 2 * pi + wheel.o - orient

    theta = np.array([ iv * ellipse.phi_at_arc(wheel.arc(phi)) + ellipse.o for phi in p ])

    normal = np.array([ ellipse.normal_at_phi(th) for th in theta ])

    xnc = np.array([ ellipse.r(th)*sin(th) for th in theta ])
    ync = np.array([ ellipse.r(th)*cos(th) for th in theta ])

    x0_wheel = xnc + iv * wheel.r * sin(normal)
    y0_wheel = ync + iv * wheel.r * cos(normal)
    
    sd.t=t
    sd.x=x0_wheel + m*sin(p)
    sd.y=y0_wheel + m*cos(p)
    sd.p=p

    sd.rotate(orient)

    sd.x += x0
    sd.y += y0
    
    return sd

def wheel_in_ellipse(x0=0,y0=0,wheel=Wheel(4,3.5,0),ellipse=Ellipse(10,0.5,0,0),
              loops=1,pts_per_loop=4000,
              slide = lambda t: 1,
              start_guard=0,end_guard=0,start_guard_angle=0,end_guard_angle=0,
              orient=0,invert=False,reverse=False):  
    '''roll on the outside (inside if invert=True) of an elliptical arc
    centered on x0, y0.  Direction of motion can be reversed by setting reverse=True
    '''
    
    iv = -1 if invert else 1
    
    sd = SpiroData()

    a = wheel.r
    m = wheel.m
    
    t=np.linspace(0,loops,int(loops*pts_per_loop))
    
    if reverse: t *= -1
    
    p = t * ellipse.c / wheel.c * 2 * pi + wheel.o - orient

    theta = np.array([ iv * ellipse.phi_at_arc(wheel.arc(phi)) + ellipse.o for phi in p ])

    normal = np.array([ ellipse.normal_at_phi(th) for th in theta ])

    xnc = np.array([ ellipse.r(th)*sin(th) for th in theta ])
    ync = np.array([ ellipse.r(th)*cos(th) for th in theta ])

    x0_wheel = xnc + iv * wheel.r * sin(normal)
    y0_wheel = ync + iv * wheel.r * cos(normal)
    
    sd.t=t
    sd.x=x0_wheel + m*sin(p)
    sd.y=y0_wheel + m*cos(p)
    sd.p=p

    sd.rotate(orient)

    sd.x += x0
    sd.y += y0
    
    return sd

def spiro_arc(x0=0,y0=0,orient=0,R=10.0,wheel=Wheel(4,3.5,0),
                    loops=1,spacing=pi/4000,
                    quadrants=0, qfuzz=50,
                    slide = lambda t: 1,
                    start_guard=0,end_guard=0,start_guard_angle=0,end_guard_angle=0,
                    invert=False,reverse=False):  
    '''roll on the outside (inside if invert=True) of an arc
    centered on x0, y0, with radius, starting at orientation of
    orient radians cw from the vertical.  Arc has length loops * 2pi
    Direction of motion can be reversed by setting reverse=True
    '''
    iv = -1 if invert else 1
    sd = SpiroData()

    a = wheel.r
    b = wheel.m
    offset = wheel.o
    
    # work out guard effects:  change in arc-length
    if start_guard_angle==0:  start_guard_angle = start_guard/(R+iv*a)
    if end_guard_angle==0:    end_guard_angle   = end_guard/(R+iv*a)

    t=np.linspace(0.0,(2*pi*R/a)*loops-(start_guard_angle+end_guard_angle)*R/a,int(loops/spacing))

    p = t
    
    guard_offset_angle=start_guard_angle
    
#    guard_offset_angle=end_guard_angle if False else start_guard_angle  # work this out later

    theta_factor = iv * a/R * slide(t)
    phi_factor   = 1
    
    # work out start_guard and end_guard effects in invert and reverse situations

    if invert:
        phi_factor   *= -1
        theta_factor *= -1
    if reverse:
        phi_factor   *= -1
        theta_factor *= -1
    
    guard_offset_angle=start_guard_angle
    
#    guard_offset_angle=end_guard_angle if False else start_guard_angle  # work this out later

    p     = phi_factor   * t + offset
    theta = theta_factor * t + orient + guard_offset_angle
    r     = R + iv * a

    if quadrants != 0:
        qtheta = 2 * pi / quadrants
        int_th = array([ int(th/qtheta) for th in theta ])
        theta = int_th*qtheta + np.random.normal(0,qtheta/qfuzz,theta.size)
        
    sd.p=p
    sd.t=theta
    sd.x=x0+r*sin(theta) + b*sin(p)
    sd.y=y0+r*cos(theta) + b*cos(p)
    
    return sd

def spiro_steps(R=10,wheel=Wheel(4,3.5,0),loops=1,n=10,offset=pi/10,spacing=pi/2000):
    sd = SpiroData()
    for i in range(n):
        wheel.o = offset*i
        sd.add(spiro(R=R,wheel=wheel,loops=loops,spacing=spacing)) 
    return sd

