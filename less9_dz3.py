import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t=np.arange(0,10,0.1)
g= 0.5
a=1
m=5
v_0=0

def radio_function(v,t):
    dvdt =  (-g/m)*v**2+a
    return dvdt

solve_Bi=odeint(radio_function, v_0,t)
plt.plot(t,solve_Bi[:,0],label="210")





plt.show()
    
 