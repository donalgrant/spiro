from SpiroDraw import *
from Ring import *
from Wheel import *
from Ellipse import *
from spiro import *
from spiro_ellipse import *

def swoops(n=40,ring=10,radius=2.5,wheel_e=0.0,ring_e=0.0,
           seed=11,xscale=40,yscale=40,swoop_min=0.01,swoop_mean=0.26,swoop_spread=0.15):
    np.random.seed(seed)
    a = radius
    bv = [0.9*a + 0.03*a*i for i in range(10)]
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
                    sd.add(spiro_arc(x0=x0[o],y0=y0[o],orient=o0,
                                     R=ring,wheel=Wheel(a,bv[i],of0+pi/5*i),loops=l))
                else:
                    sd.add(wheel_in_ellipse(x0=x0[o],y0=y0[o],wheel=Wheel(a,bv[i],of0+pi/5*i),
                                            ellipse=Ellipse(ring,ring_e,0,pi/2+o0),loops=l))
            else:
                sd.add(elliptical_arc(x0=x0[o],y0=y0[o],orient=o0,
                                      R=ring,wheel=Ellipse(a,wheel_e,bv[i],of0+pi/5*i),loops=l))

    return sd
