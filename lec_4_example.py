import numpy as np
def grav_accel(phi=0,h=0):

  """ускорение свободного падения 
  phi - широта места наблюдения 
  h - высота над поверхностью Земли 
  """

  g=9.780318*(1+0.005302*np.sin(phi)**2-0.000006*(np.sin(2*phi)**2))-0.000003086*h

  return g 
 
def losing_weight_function(mass=50,phi_0=54,phi_end=0,h_end=3000):
    """Функция определяющая вес 
  """

  P_0=grav_accel(phi_0,h_end)*mass
  P_end=grav_accel(phi_end,h_end)*mass
  if delta_P>0:
    print('Вы похудете на:',delta_P,'r')
  elif delta_P <0:
    print('Вы поправитесь на:',delta_P*(-1),'r')
  else:
    print('ты-жиробас сиди дома:')

losting_weight_function(2)