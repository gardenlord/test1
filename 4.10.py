import sympy as sp
from func_4 import *

sp.init_printing()
s = sp.Symbol('s')
T = sp.Symbol('T', real=True)
P = 1 / ((1 + T * s) * s)
str = sp.apart(P, s)
print(str)
t = sp.Symbol('t', positive=True)
str = sp.inverse_laplace_transform(1/s-1/(s+1/T), s, t)
print(str)

# w = sp.Symbol('w', real=True)
# P = w**2/(s*(s+w)**2)
# str = sp.apart(P, s)
# print(str)

# P = sp.apart(w**2/s/(s+w)**2, s)
# Pt = sp.inverse_laplace_transform(P, s, t)
# str = sp.expand(Pt)
# print(str)

# p1= sp.Symbol('p1', real=True)
# p2= sp.Symbol('p2', real=True)
# P = w**2/(s*(s-p1)*(s-p2))
# str = sp.apart(P, s)
# print(str)

# str = sp.inverse_laplace_transform(P, s, t)
# print(str)

# P1 = tf([1, 3], [1, 3, 2])
# print(P1)
# fig, ax = plt.subplots(figsize=(3, 2.3))
# y, t = step(P1, np.arange(0, 10, 0.01))
    
# ax.plot(t, y)
# plot_set(ax, 't', 'y')
# plt.show()


P2 = tf([0, 1], [1, 2, 2, 1])
print(P2)
fig, ax = plt.subplots(figsize=(3, 2.3))
y, t = step(P2, np.arange(0, 15, 0.01))
ax.plot(t, y)
plot_set(ax, 't', 'y')
plt.show()
'''
fyi:
https://docs.sympy.org/latest/modules/polys/reference.html?highlight=apart#sympy.polys.partfrac.apart

'''