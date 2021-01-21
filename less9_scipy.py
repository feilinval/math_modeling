import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#пределы изменения переменной велечины
#В данной задаче переменной велечиной является время
t=np.arange(0,10**6,100)

#запись диф.уравнения в виду функции
def radio_function(m,t):
    dmdt =  -k*m
    return dmdt

# Определение начальных условий и параметров
m_0=10
k= 1.64*10**(-6) #постоянная распада для 

# Решение дифференциального уравнения функцией odeint
solve_Bi=odeint(radio_function, m_0,t)

# Построение решения в виду графика функции 
plt.plot(t,solve_Bi[:,0],label="распад Висмутас 210")
plt.xlabel("Период распада,секунды")
plt.ylabel("функция распада")
plt.title("Радиоктивный распад")
plt.legend()


plt.show()
