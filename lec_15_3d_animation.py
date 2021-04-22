import numpy as np
	
import matplotlib.pyplot as plt
	
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig=plt.figure()
ax=p3.Axes3D(fig)
N=100
alpha=np.linspace(0,10,N)

x=np.cos(alpha)
y=np.sin(alpha)
z=alpha*0.1

ball,=ax.plot(x,y,z,"o",color="b")
line,=ax.plot(x,y,z,"_",color="b")

def animation_func(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])

    line.set_data(x[:i],y[:i]) 
    line.set_3d_properties(z[:i])
    
    
ax.strides_xlim3d([-1.0,1.0])
ax.set_xlabel("x")

ax.strides_ylim3d([-1.0,1.0])
ax.set_ylabel("y")

ax.strides_zlim3d([-1.0,1.0])
ax.set_zlabel("z")

ani = animation.FuncAnimation(fig,
                    animation_func,
                    N,
                    interval=50)  
plt.show()
    



