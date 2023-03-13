from func_4 import *
fig, ax = plt.subplots(figsize=(3, 2.3))

LS = linestyle_generator()

T = 0.5
K = [1, 2, 3]
for i in range(len(K)):
    y, t = step(tf([0, K[i]], [T, 1]), np.arange(0, 5, 0.01))
    ax.plot(t,y,ls=next(LS), label='K='+str(K[i]))

ax.set_xticks(np.arange(0, 5.2, step=1.0))
ax.set_yticks(np.arange(0, 3.2, step=1))
plot_set(ax, 't', 'y', 'upper left')

# plt.show()
# fig.savefig("1st_step2.pdf", transparent=True, bbox_inches="tight", pad_inches=0.0)

##################
import sympy as sp
sp.init_printing() # Initializes pretty-printer depending on the environment.
s = sp.Symbol('s')
T = sp.Symbol('T', real=True) # real: object can have only values from the set of real numbers.
P = 1/((1+T*s)*s)
print(sp.apart(P, s)) # Compute partial fraction decomposition of a rational function.

t = sp.Symbol('t', positive=True) # positive: object can have only positive (nonpositive) values.
str_2 = sp.inverse_laplace_transform(1/s - 1/(s + 1/T), s, t)
print(str_2)
print('end')

'''
fyi:
https://docs.sympy.org/latest/modules/core.html?highlight=symbol#module-sympy.core.symbol
https://docs.sympy.org/latest/modules/polys/reference.html?highlight=apart#sympy.polys.partfrac.apart

'''
