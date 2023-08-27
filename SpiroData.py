import numpy as np

class SpiroData:
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = np.array([])
        self.y = np.array([])
        self.p = np.array([])
        self.t = np.array([])   # parameterize the drawing data (not sure if this is needed yet)

    def add(self, sd):
        self.x = np.append(self.x,sd.x)
        self.y = np.append(self.y,sd.y)
        self.p = np.append(self.p,sd.p)
        self.t = np.append(self.t,sd.t)

    def set(self,x=0,y=0,p=0,t=0):
        self.x = np.array([x])
        self.y = np.array([y])
        self.p = np.array([p])
        self.t = np.array([t])

    def set_array(self,x,y,p,t):
        for i in range(x.shape[0]):
            np.append(self.x,x)
            np.append(self.y,y)
            np.append(self.p,y)
            np.append(self.t,t)
    
    def xc(self):  return self.x[-1] 
    def yc(self):  return self.y[-1] 
    def pc(self):  return self.p[-1]
    def tc(self):  return self.t[-1]
    
