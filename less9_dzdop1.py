import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


r=np.arange(2*6371000,6371000,-100)
G=6.67*10**(-11)

m=5.97*(10**24)
v_0=0.01



def function (v,r):
    dvdr =  -(G*m)/(r**2*v)
    return dvdr

solve_Bi=odeint(function, v_0,r)
plt.plot(r,solve_Bi[:,0],label="210")





plt.show()