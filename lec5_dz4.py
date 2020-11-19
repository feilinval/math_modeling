from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Abs


x=symbols("x")

gol=reduce_abs_inequality((Abs((x**2)+2*x-3))+(3*(x+1)),"<",x)
print(gol)
sol=reduce_rational_inequalities((((x-1)*(x+2))/((x-3)*(x+4))),"<=",x)
print(sol)



