import matplotlib.pyplot as plt
import numpy as np
def circle_plotter(R=1,title="circle plotter"): 
   x= np.arange(-2.0,2.0,0.1)
   y= np.arange(-2.0,2.0,0.1)
   X,Y=np.meshgrid(x,y)
   fxy=X**2+Y**2
   plt.contour(X,Y,fxy,levels=[R])
   plt.axis("equal") 
   plt.show()
   
circle_plotter()

