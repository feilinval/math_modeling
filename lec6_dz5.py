import matplotlib.pyplot as plt
import numpy as np

def spiralka(b=0.1):
    
    
    f=np.arange(0,8*np.pi,0.1) 
    r=np.e**(b*f)
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.show()

spiralka()
    