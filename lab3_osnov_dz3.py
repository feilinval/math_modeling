import numpy as np

np.pi=3.14
v0x=3
g=10
y0=5
x0=4
t = np.arange(0,5,0.1)
alpha = np.pi/6

x= x0+v0x*t
y=y0+v0x*t-(g*t**2/2)

print (x)
print (y)

traj=np.ndarray(shape=(len(t),3))
for i in range(len(t)):
    traj[i,0] = t[i]
    traj[i,1] = x[i]
    traj[i,2] = y[i]



print (traj)





