import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


x=np.arange(-5,5,0.01)
y0=1
z0=-3
z = y0, z0 

def func(a,x):
    y,z=a
    dx_dt=y**2*z
    dz_dx=(z/x)-y*z**2
    return dx_dt,dz_dx

sol=odeint(func,z,x)

plt.plot(x,sol[:,1],"b",label="theta(x)")
plt.legend()
plt.show()    