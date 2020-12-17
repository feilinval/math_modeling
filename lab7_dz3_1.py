import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


fig,ax=plt.subplots()



babochka,=plt.plot([],[],"-")
xdata,ydata=[],[]

def babochka_func(t):
   
   
    
    xdata.append(np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    ydata.append(np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    babochka.set_data(xdata,ydata)
    return babochka,
    
                      
    
    
    
edge=3
plt.axis("equal")
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
    

      
ani=FuncAnimation(fig,
                  babochka_func,
                  frames=np.arange(0,2*np.pi,0.1),
                  interval=100
                  )
ani.save("lab7_dz3.gif")
  
    
    
    
    
  
