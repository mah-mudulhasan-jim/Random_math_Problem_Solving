import math
import sympy as sp
# problem-03
x = sp.symbols("x")
f = sp.exp(x) + sp.exp(-x)
df = sp.diff(f, x)
y2 = df.subs(x, 1)
print(y2)