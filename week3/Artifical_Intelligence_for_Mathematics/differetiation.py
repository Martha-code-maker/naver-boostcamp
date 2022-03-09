import sympy as sym
from sympy.abc import x

print(sym.diff(sym.poly(x**2 + 2*x + 3), x))
