import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(6,12,0.1)

e_0=1367
s_0=1600
k=300*10**(-8)


def function(s,t):
    dsdt =k*(np.sqrt(s/np.pi))*e_0*s*np.cos((np.pi)/12*(t-12))
    return dsdt

solve_Bi=odeint(function, s_0,t)
plt.plot(t,solve_Bi[:,0],label="210")





plt.show()