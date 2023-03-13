# 一阶滞后系统的阶跃响应(改变T值)

from func_4 import *
fig, ax = plt.subplots(figsize=(3, 2.3))
LS = linestyle_generator()

K = 1
T = (1, 0.5, 0.1)
for i in range(len(T)):
    y, t = step(tf([0, K], [T[i], 1]), np.arange(0, 5, 0.01))
    ax.plot(t, y, ls = next(LS), label='T='+str(T[i]))


ax.set_xticks(np.linspace(0, 5, 6))
ax.set_yticks(np.linspace(0, 1, 6))
plot_set(ax, 't', 'y', 'best')

plt.show()