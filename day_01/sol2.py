import math
import sympy as sp
# problem-02
x = sp.symbols("x")
f = sp.atan(x)
df = sp.diff(f, x)
print(df)