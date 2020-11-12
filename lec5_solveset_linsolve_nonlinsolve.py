from sympy import symbols
from sympy import sin, cos, pi, exp  
from sympy import simplify,expand,factor,trigsimp
from sympy import linsolve,linsolve,solveset,solve

x,y,z=symbols('x y z')
expr=x**2-2
solve_expr=solve(expr,x)
print(solve_expr)

expr=sin(x**2)-exp(-2*x)+cos(pi/x)
solve_expr=solve(expr,x)
print(solve_expr)

system=[x+y+z-1, x+y+2*z-3,x-2*y+z]
solve_system=linsolve(system,(x,y,z))
print(solve_system)

system=[x**2+x,x-y]
print(solve_system)
