import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig,ax=plt.subplots()



heart,=plt.plot([],[],"-")
xdata,ydata=[],[]

def heart_func(t):
   
   
    
    xdata.append(16*np.sin**3(t)
    ydata.append(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    heart.set_data(xdata,ydata)
    return heart,
    
                      
    
    
    
edge=3
plt.axis("equal")
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
    

      
ani=FuncAnimation(fig,
                  heart_func,
                  frames=np.arange(0,2*np.pi,0.1),
                  interval=100
                  )
ani.save("lab7_dz3.gif")