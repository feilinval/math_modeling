from sympy import symbols
from sympy import sin, cos, pi, exp
import sympy

o,a,p=symbols("o a p")






ch=exp(a)-exp(-a)/2
sh=exp(a)-exp(-a)/2

x=a*sh.subs(a,p)/ch.subs(a,p)-cos(o)
y=a*sin(p)/ch.subs(a,p)-cos(o)

p1=int(input("введите число p"))
o1=int(input("введите число o"))
a1=int(input("введите число a"))
x=x.subs(p,p1)
x=x.subs(o,o1)
x=x.subs(a,a1)
print(x.evalf())
 




