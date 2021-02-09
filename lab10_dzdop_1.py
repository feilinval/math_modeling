import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t=np.arange(-1,1,0.01)


x0=-71
y0=1
z0=-3


a0 = x0, y0 ,z0

def func(a,t):
    x,y,z=a
    dx_dt=3*x-y+z
    dy_dt=x+y+z
    dz_dt=4*x-y+4*z
    return  dx_dt,dy_dt,dz_dt

sol=odeint(func,a0,t    )

plt.plot(t,sol[:,1],"b",label="theta(x)")
plt.plot(t,sol[:,0],"r",label="theta(z)")
plt.plot(t,sol[:,2],"g",label="theta(x)")


plt.legend()
plt.show()    