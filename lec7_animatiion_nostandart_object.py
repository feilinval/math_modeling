import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig,ax=plt.subplots()
ball,=plt.plot([],[],"o",color="r",label="ball")

def circle_move(R, vx0,vy0,time):
    x0=vx0*time
    y0=vy0*time
    alpha=np.arange(0,2*np.pi,0.1)
    x=x0+R*np.cos(alpha)
    y=y0+R*np.sin(alpha)
    return x,y

edge=3
plt.axis("equal")
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)

def animate(i):
    ball.set_data(circle_move(R=0.5,vx0=0.01,vy0=0,time=i))
    
ani=FuncAnimation(fig,
                  animate,
                  frames=100,
                  interval=100 
                  )
    
ani.save("lec7_animation_nostandart_object.gif")
    