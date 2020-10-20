import numpy as np

np.pi=3.14
t=200
ee=300
k=1.38*10**(-23)
e=2.7
h=6.63*10**(-34)

N= 2/np.sqrt(np.pi)*(h/(k*t)**3/2)*e**(-ee/(k*t))*(ee**(t/2))
print(N)