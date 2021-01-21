import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,4,0.1)
k=0.08
n=1000
m_o=10
def radio_function(m,t):
    gmdt =  k*m*t
    return gmdt

solve_Bi=odeint(radio_function, m_o,t)
plt.plot(t,solve_Bi[:,0],label="210")

plt.plot(t,m_o*10*np.ones(len(t)))



plt.show()