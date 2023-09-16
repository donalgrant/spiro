import sys
sys.path.append('../..')

from SpiroData import *
from SpiroDraw import *
from spiro import *
from spiro_ellipse import *

S = SpiroData()
F = SpiroFig()

###

S.reset()
T = SpiroData()
for wo in linspace(0,5*pi,3):
    for i in range(30):
        T.reset()
        m=5+i/2
        w=Ellipse(major=7,  eccen=0.4,pen=m, offset=0, pen_offset=0)
        r=Ellipse(major=20, eccen=0.7,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.5))
        S.add(T)

F.plot(S,color_scheme='t-waves',cmap='jet',save=True)

###

S.reset()
T = SpiroData()
for wo in linspace(0,3*pi,5):
    for i in range(12):
        T.reset()
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=m, offset=0, pen_offset=0)
        r=Ellipse(major=20, eccen=0.7,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.3))
        T.rotate(wo)
        T.x+=i
        S.add(T) 

F.plot(S,color_scheme='length',cmap='jet',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-10,5)
    for i in range(20):
        T.reset()
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.06))
 #       T.rotate(wo)
 #       T.x+=i
        S.add(T)
F.plot(S,color_scheme='length',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='time',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(10):
        m=5+i/3
        w=Ellipse(major=3,  eccen=0.4,pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,       offset=0, pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=False,loops=0.1))
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)

F.plot(S,color_scheme='cycles',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=3, eccen=0.3, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.0,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/120)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='cycles',cmap='ocean',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=3, eccen=0.3, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.1,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/240)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='cycles',cmap='terrain',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=6, eccen=0.3, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.1,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='t-waves',cmap='ocean',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=6, eccen=0.8, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.8,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='rrand',cmap='hsv',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(25):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(20):
        m=5+i/3
        w=Ellipse(major=6, eccen=0.8, pen=4, offset=i*pi/20, pen_offset=0)
        r=Ellipse(major=R, eccen=0.8,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.1))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='x+y',cmap='rainbow',save=True)

###

S.reset()
T = SpiroData()
for sweep in range(15):
    wo = np.random.uniform(0,2*pi)
    R = 20 + np.random.uniform(-15,5)
    T.reset()
    for i in range(10):
        m=5+i
        w=Ellipse(major=6, eccen=0.2, pen=m, offset=i*pi/20, pen_offset=pi/4)
        r=Ellipse(major=R, eccen=0.6,        offset=0,       pen_offset=wo)
        T.add(eIe(ring=r,wheel=w,inside=True,loops=0.2))
        T.rotate(i/280)
    T.x+=np.random.uniform(-R,R)
    T.y+=np.random.uniform(-R,R)
    S.add(T)
F.plot(S,color_scheme='length',cmap='rainbow',save=True)
