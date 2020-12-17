import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
ball,=plt.plot([],[],"o",color="r",label="ball")

def circle_move(R):
    x0=5
    y0=5
    alpha=np.arange(0,2*np.pi,0.1)
    x=x0+R*np.cos(alpha)
    y=y0+R*np.sin(alpha)
    return x,y

edge=10
plt.axis("equal")
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)

def animate(i):
    ball.set_data(circle_move(R=i*0.3))
    
ani=FuncAnimation(fig,
                  animate,
                  frames=100,
                  interval=100 
                  )
    
ani.save("lab7_dz3.gif")