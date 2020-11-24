from sympy import sqrt
from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs
from sympy.vector import CoordSys3D


N = CoordSys3D("N")
E1, E2, x, y, z, i, j, k =symbols("E1 E2 x y z i j k")


q1 = 1
q2 = - 0.5

E1 = (((q1*x)/((sqrt((x**2) + (y**2) + (z**2))**3)))*N.i + ((q1*y)/(sqrt((x**2) + (y**2) + (z**2))**3))*N.j + ((q1*z)/(sqrt((x**2) + (y**2) + (z**2))**3))*N.k)

E2 = (((q2*(x - 1))/(sqrt(((x-1)**2) + ((y - 1)**2) + ((z - 1)**2)))**2)**3)*N.i + (((q2*(y - 1))/(sqrt(((x-1)**2) + ((y - 1)**2) + ((z - 1)**2)))**2)**3)*N.j + (((q2*(z - 1))/(sqrt(((x-1)**2) + ((y - 1)**2) + ((z - 1)**2)))**2)**3)*N.i

E = E1 + E2
E_new = E.subs([(x, 3), (y, 4), (z, 5)])

print(E_new.evalf())

print(sqrt(E_new.dot(E_new)).evalf())