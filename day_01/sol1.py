# problem-01
import sympy as sp
import math
x = sp.symbols("x")
f = x**3 - 3*x**2 -45*x + 13
df3 = sp.diff(f, x, 3)
print(df3)