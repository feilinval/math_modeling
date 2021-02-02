import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,2*np.pi,0.1)
q=147000000000
l=3.827*(10**26)
v= 30400
r= 6400000  
s=np.pi*r**2
def function(v,t):
    dsdt =s*(l/4*np.pi*q)
    return dsdt

solve_Bi=odeint(function, v,t)
plt.plot(t,solve_Bi[:,0],label="210")





plt.show()