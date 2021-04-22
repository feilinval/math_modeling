import numpy as np
	

	
import matplotlib.pyplot as plt
	
from mpl_toolkits.mplot3d import Axes3D

fig= plt.figure()
ax= fig.gca(projection="3d")

t=np.arange(0.01,4*np.pi,0.01)
R=1

x=R*np.cos(t)
y=R*t**0.5
z=R*np.log10(t)
#Построение пространственной прямой 
ax.plot(x,y,z, label="dich")
ax.legend()

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_title("3D test")

arrow_x0=0
arrow_y0=0
arrow_z0=0

arrow_x1=1
arrow_y1=1
arrow_z1=1

ax.quiver(arrow_x0,arrow_x0,arrow_x0,
          arrow_x1,arrow_x1,arrow_x1,
          length=1,normalize=True,color="r")

plt.show

