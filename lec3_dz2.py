import numpy as np


a=3.14/3
h=100
b=np.pi/6
g=10
cos=0.9
tan=-6.4


v= np.sqrt((g*h*np.tan(b)**2)/(2*np.cos(a)**2*(1-np.tan(b)*np.tan(a))))
print(v)