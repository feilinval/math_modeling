from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin,cos,trigsimp

N=CoordSys3D("N")
a,b,c =symbols("a b c")
v=N.i-2*N.j
print(v/3)

v1=2*N.i+3*N.j-N.k
v2=N.j-4*N.j+N.k

sol=v1.dot(v2)
print(sol)

v=(a*b+a*c+b**2+b*c)*N.i+N.i
sol=v.factor
print(sol)