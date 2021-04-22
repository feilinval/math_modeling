import numpy as np
	
import matplotlib.pyplot as plt
	
import mpl_toolkits.mplot3d.axes3d as p3

fig=plt.figure()
ax=p3.Axes3D(fig)

phi=np.linspace(0,2* np.pi,100)
theta = np.linspace(0,2*np.pi,100)
#параметрическое задание 
a=2
b=3
c=4
x=a*np.outer(np.cos(phi),np.sinh(theta))
y=b*np.outer(np.sin(phi),np.sinh(theta))
z=c*np.outer(np.ones(np.size(phi)),np.sinh(theta))

ax.plot_surface(x,y,z,color="b")
plt.show()





