import sympy as sp
import math
r = sp.symbols("r")
h = sp.symbols("h")
eqn = 2*math.pi*r**2 + 2*math.pi*r*h - 384*math.pi
val_h = sp.solve(eqn, h)
# print(val_h)
v = math.pi*val_h[0]*r**2
# print('#', v)
dv = sp.diff(v, r)
# print(dv)
critical_point = sp.solve(dv, r)
# print(critical_point)
dv2 = sp.diff(v, r, 2)
# print(dv2)
for i in critical_point:
  if dv2.subs(r, i) < 0:
    max_r = i
# print(max_r)
max_v = v.subs(r,max_r)
print(f'Maximum Volume of the cylinder: {int(max_v)} unit^3.')