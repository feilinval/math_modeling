import math
print(math.sqrt(3))

import sympy
print(sympy.sqrt(3))

print(2*sympy.sqrt(3))

from sympy import symbols
x, y = symbols("x y")
expr = x+2*y
print (expr)

print (expr + 1)

print (x*expr)

from sympy import sin, cos, pi, exp
print(sin(x**2)-exp(-2*x)+cos(pi/x))
