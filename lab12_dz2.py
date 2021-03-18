import numpy as np
	
from scipy.integrate import odeint
	
import matplotlib.pyplot as plt
	
from matplotlib.animation import FuncAnimation
	
 
frames = 365
	
seconds_in_year = 365 * 24 * 60 * 60
	
years = 1


t = np.linspace(0, years*seconds_in_year, frames)


def move_func(s, t):
    (x, vx, y, vy,
      xm, vmx, ym, vmy) = s
    
    dxdt = vx
    dv_xdt  =(k*q1*q)/(m*(x**2+y**2)**1.5)
    dydt = vy
    dv_ydt  =(k*q1*q)/(m*(x**2+y**2)**1.5)
    
    dxmdt = vmx
    dvm_xdt = (k*q2*q)/(m*(x**2+y**2)**1.5)
    dymdt = vmy
    dvm_ydt = (k*q2*q)/(m*(x**2+y**2)**1.5)
    
    dxodt = vox
    dvo_xdt = (k*q3*q)/(m*(x**2+y**2)**1.5)
    dyodt = voy
    dvo_ydt = (k*q3*q)/(m*(x**2+y**2)**1.5)
    
    dxjdt = vjx
    dvj_xdt = (k*q4*q)/(m*(x**2+y**2)**1.5)
    dyjdt = vjy
    dvj_ydt = (k*q4*q)/(m*(x**2+y**2)**1.5)
    
    dxpdt = vpx
    dvp_xdt = (k*q5*q)/(m*(x**2+y**2)**1.5)
    dypdt = vpy
    dvp_ydt = (k*q5*q)/(m*(x**2+y**2)**1.5)
    

    return (dxdt, dv_xdt, dydt, dv_ydt,
            dxmdt, dvm_xdt, dymdt, dvm_ydt,
            dxodt,dvo_xdt,dyodt,dvo_ydt,
            dxjdt,dvj_xdt,dyjdt,dvj_ydt,
            dxpdt,dvp_xdt,dypdt,dvp_ydt)
            



q1=1
q2=1
q3=1
q4=1
q5=1
q=100
k=9*10**9

x0=-40
vx0=1
y0=20
vy0=0

xm0=-40
vmx0=1
ym0=-20
vmy0=0

xo0=-40
vxo0=1
yo0=40
vyo0=0

xj0=-40
vxj0=1
yj0=-40
vyj0=0

xp0=-40
vxp0=1
yp0=-50
vyp0=0



m=10**5
    
    
s0=(x0,vx0,y0,vy0,
    xm0,vmx0,ym0,vmy0,
    xo0,vxo0,vmo0,vmyo0,
    xj0,vxj0,vmj0,vmyj0,
    xp0,vxp0,yp0,vyp0)

def solve_func(i, key):
        sol = odeint(move_func, s0, t)
        if key == 'point':
            x = sol[i, 0]
            y = sol[i, 2]
            xm = sol[i,4]
            ym = sol[i,6]
            xo
            yo
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
    
    ballm.set_data(solve_func(i, 'point')[2])
    ball_linem.set_data(solve_func(i, 'line')[2])
    
    ballm.set_data(solve_func(i, 'point')[3])
    ball_linem.set_data(solve_func(i, 'line')[3])
    
    ballm.set_data(solve_func(i, 'point')[4])
    ball_linem.set_data(solve_func(i, 'line')[4])
    
    
ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)  

plt.axis('equal')
edge = 4*x0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()


