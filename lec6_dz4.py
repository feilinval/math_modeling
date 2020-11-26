import matplotlib.pyplot as plt
import numpy as np

def stupenki_plotter(N=100,title="stupenki plotter"): 
    x=np.arange(1,N,0.01)
    y=[]
    for i in range(len(x)):
        y.append(x[i]//1)
    plt.plot(x,y)
    plt.show()
stupenki_plotter()