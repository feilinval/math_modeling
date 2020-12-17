import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from math import sqrt, cos, sin

fig,ax=plt.subplots()
ball,=plt.plot([],[],"o",color="r",label="ball")

t=np.linspace (-5,105)
x=sin(t)*(e**(np.cos(t))-2*cos*(4*t)+(sin**5)*(t/12))
