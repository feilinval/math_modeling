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

def ilips_plotter(r=1,a=1.9,b=1,):
   x= np.arange(-2.0,2.0,0.1)
   y= np.arange(-2.0,2.0,0.1)
   x,y=np.meshgrid(x,y)
   fxy=x**2/a**2+y**2/b**2
   plt.contour(x,y,fxy,levels=[1])
   plt.axis("equal") 
   plt.show()
   
ilips_plotter()

