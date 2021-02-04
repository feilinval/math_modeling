import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


x=np.arange(0,2,0.01)
y0=0.01
omega0=0.05
z0=y0,omega0


def diff_func(z,x):
    y, omega=z
    dy_dx=omega
    domega_dx=-np.sin(y)*omega+3*x*y+5
    return dy_dx,domega_dx
    
sol=odeint(diff_func,z0,x)
plt.plot(x,sol[:,1],"b",label="theta(t)")

plt.legend()
plt.show()


