import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

frames=200
t=np.linspace(0,5,frames)



m=0.5

v0=0.5



g=10
k=12
y0=0.2
a0=v0,y0
def move(a,t):
    y,v=a
    dv_dt=v
    
    dy_dt=g-(k/m)*y
    
    return dy_dt,dv_dt
fig,ax=plt.subplots()

def solve_func (i,key):
    sol=odeint(move,a0,t)
    if key=='point':
        x=sol[i,0]
    return x

ball,=plt.plot([],[],"o",color="r",label="ball")
def animate(i):
    ball.set_data(solve_func(i,'point'))
    

    
    
ani=FuncAnimation(fig,
                  animate,
                  frames=frames,
                  interval=30)
edge=15
ax.set_xlim(0,edge)
ax.set_ylim(0,edge)

ani.save('lab_11_dz3.gif')

plt.show
   
    



         
               


    
