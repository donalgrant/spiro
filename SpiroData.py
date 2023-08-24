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

    def xc(self):  return self.x[-1] 
    def yc(self):  return self.y[-1] 
    def pc(self):  return self.p[-1]
    def tc(self):  return self.t[-1]
    
