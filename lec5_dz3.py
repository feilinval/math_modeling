from sympy import symbols
from sympy import sin, cos, pi, exp  
from sympy import simplify,expand,factor,trigsimp
from sympy import linsolve,linsolve,solveset,solve

x,E=symbols('x E ')
expr=(x**2+x+(1/x)+(1/x**2))-4
solve_expr=solve(expr,x)
print(solve_expr)


M=9
e=0.8
expr=E-e*sin(E)-M
solveset_expr=solveset(expr,E)
print(solveset_expr)
