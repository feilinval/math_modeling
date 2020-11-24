from sympy import sqrt
from sympy import symbols
from sympy import sin, cos, pi, exp
from sympy import simplify, expand, factor, trigsimp
from sympy import solveset, linsolve, nonlinsolve, Eq, solve
from sympy import Abs

x, y, z =symbols("x y z")
simp_expr1 = simplify((x*y**2)-(2*x*y*z)+(x*z**2)+(y**2)-(2*y*z)+(z**2))/((x**2)-1)

print(simp_expr1)

a = symbols("a")

simp_expr2 = simplify(sqrt((1 + sin(a))/(1 - sin(a))) + (sqrt(1 - sin(a))/(1 + sin(a))))

print(simp_expr2)