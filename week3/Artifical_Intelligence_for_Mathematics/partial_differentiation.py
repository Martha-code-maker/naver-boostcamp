import sympy as sym
from sympy.abc import x,y

print(sym.diff(sym.poly(x**2 + 2*x*y + 3) + sym.cos(x + 2*y), x))