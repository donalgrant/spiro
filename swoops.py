from SpiroDraw import *
from Ring import *
from Wheel import *
from Ellipse import *
from spiro import *
from spiro_ellipse import *

def swoops(n=40,ring=10,radius=2.5,wheel_e=0.0,ring_e=0.0,
           seed=11,xscale=40,yscale=40,exponential=False,
           swoop_min=0.01,swoop_mean=0.26,swoop_spread=0.15):
    np.random.seed(seed)
    a = radius
    bv = [0.9*a + 0.03*a*i for i in range(10)]
    if exponential:
        x0=np.random.exponential(xscale,n)
        y0=np.random.exponential(yscale,n)
    else:
        x0=np.random.standard_normal(n)*xscale-xscale/2
        y0=np.random.standard_normal(n)*yscale-yscale/2
    sd=SpiroData()
    for o in range(x0.shape[0]):
        o0  = np.random.uniform(2*pi)
        of0 = np.random.uniform(2*pi)
        for i in range(np.random.randint(3,10)): 
            l=max(swoop_min,swoop_mean+swoop_spread*np.random.standard_normal(1)[0])
            if (wheel_e==0):
                if (ring_e==0):
                    r = Ring(ring,origin=np.array([x0[o],y0[o]]),orient=o0)
                    sd.add(circle_in_circle(r,Wheel(a,bv[i],of0+pi/5*i),loops=l))
                else:
                    e = Ellipse(ring,ring_e,0,pi/2+o0,origin=np.array([x0[o],y0[o]]))
                    sd.add(circle_in_ellipse(e,Wheel(a,bv[i],of0+pi/5*i),loops=l))
            else:
                r = Ring(ring,origin=np.array([x0[o],y0[o]]),orient=o0)
                sd.add(ellipse_in_circle(r,Ellipse(a,wheel_e,bv[i],of0+pi/5*i),loops=l))

    return sd
