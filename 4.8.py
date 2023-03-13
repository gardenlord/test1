# 二阶系统的阶跃响应
from func_4 import *

fig, ax = plt.subplots(figsize=(3, 2.3))

LS = linestyle_generator()

zeta = [1, 0.7, 0.4]
omega_n = 5
for i in range(len(zeta)):
    P = tf([0, omega_n**2], [1, 2*zeta[i]*omega_n, omega_n**2])
    y, t = step(P, np.arange(0, 5, 0.01))
    
    pltargs = {'ls': next(LS), 'label': '$\zeta$='+str(zeta[i]) }
    ax.plot(t, y, **pltargs)

ax.set_xticks(np.arange(0, 5.2, step=1.0))
ax.set_yticks(np.arange(0, 1.3, step=0.25))
plot_set(ax, 't', 'y', 'best')    

#############################
fig, ax = plt.subplots(figsize=(3, 2.3))

LS = linestyle_generator()

zeta = [0.1, 0, -0.05]
omega_n = 5
for i in range(len(zeta)):
    P = tf([0, omega_n**2], [1, 2*zeta[i]*omega_n, omega_n**2])
    y, t = step(P, np.arange(0, 5, 0.01))
    
    pltargs = {'ls': next(LS), 'label': '$\zeta$='+str(zeta[i])}
    ax.plot(t, y, **pltargs)
 
ax.set_xticks(np.arange(0, 5.2, step=1.0))
ax.set_yticks(np.arange(-4, 5, step=2))

plot_set(ax, 't', 'y', 'lower left')
plt.show()
    
# fig.savefig("2nd_step1.pdf", transparent=True, bbox_inches="tight", pad_inches=0.0)