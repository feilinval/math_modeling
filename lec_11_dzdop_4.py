import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
     
frames=200 
t= np.linspace(0,5,frames)

l0=2.5
l=0.1
g=10
n=51   
vx0=2
x0=2                                                                    
a0=x0,vx0

def move(a,t):
    x,vx=a
    dx_dt= vx 
    dvx_dt=g*(x/l)-n*g*(l-x/l)
        
    return  dx_dt, dvx_dt
fig,ax=plt.subplots()

sol=odeint(move,a0,t)


ball,=plt.plot([],[],"o",color="r",label="ball")
def animate(i):
    ball.set_data(t,sol[i,0])
    

    
    
ani=FuncAnimation(fig,
                  animate,
                  frames==frames,
                  interval=30)
edge=15
ax.set_xlim(0,edge)
ax.set_ylim(0,edge)

ani.save('lab_11_dz3.gif')

plt.show  