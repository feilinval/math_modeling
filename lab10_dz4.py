import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt




t=np.arange(-5,5,0.01)


y0=4


a0 = x0, y0 

def func(a,t):
    x,y=a
    dy_dt=
    dy_dt=
    return 

sol=odeint(func,a0,t    )

plt.plot(t,sol[:,1],"b",label="theta(x)")
plt.legend()
plt.show()    
    