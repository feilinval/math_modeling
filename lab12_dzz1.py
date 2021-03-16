import numpy as np
	
from scipy.integrate import odeint
	
import matplotlib.pyplot as plt
	
from matplotlib.animation import FuncAnimation
	
 
	
# Определяем переменную величину
	
frames = 365
	
seconds_in_year = 365 * 24 * 60 * 60
	
years = 1
	
t = np.linspace(0, years*seconds_in_year, frames)

# Определяем функцию для системы диф. уравнений

def move_func(s, t):
    (x, v_x, y, v_y,
      xm, vm_x, ym, vm_y) = s
    
    dxdt = v_x
    dv_xdt = - G * m * x / (x**2 + y**2)**1.5
    dydt = v_y
    dv_ydt = - G * m * y / (x**2 + y**2)**1.5
    
    dxmdt = vm_x
    dvm_xdt = - G * m * xm / (xm**2 + ym**2)**1.5
    dymdt = vm_y
    dvm_ydt = - G * m * ym / (xm**2 + ym**2)**1.5
    return (dxdt, dv_xdt, dydt, dv_ydt,
            dxmdt, dvm_xdt, dymdt, dvm_ydt)
# Определяем начальные значения и параметры
G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

xm0 = 228 * 10**9
vm_x0 = 0
ym0 = 0
vm_y0 = 24000



x0 = 149 * 10**9
v_x0 = 0
y0 = 0
v_y0 = 30000

s0 = (xm0, vm_x0, ym0, vm_y0,x0,v_x0,y0,v_y0)



# Строим решение в виде графика и анимируем
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
        xm = sol[i,4]
        ym = sol[i,6]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
        xm =sol[:i, 4]
        ym = sol[:i, 6]
    return ((x, y), (xm, ym))
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')

ballm, = plt.plot([], [], 'o', color='b')
ball_linem, = plt.plot([], [], '-', color='b')

plt.plot([0], [0], 'o', color='y', ms=20)

def animate(i):
    ball.set_data(solve_func(i, 'point')[0])
    ball_line.set_data(solve_func(i, 'line')[0])

    ballm.set_data(solve_func(i, 'point')[1])
    ball_linem.set_data(solve_func(i, 'line')[1])
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)  

plt.axis('equal')
edge = 4*x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()