from func_4 import *

fig, ax = plt.subplots(figsize=(3, 2.3))

LS = linestyle_generator()

zeta = 0.7
omega_n = [1, 5, 10]
for i in range(len(omega_n)):
    P = tf([0, omega_n[i]**2], [1, 2*zeta*omega_n[i], omega_n[i]**2])
    y, t = step(P, np.arange(0, 5, 0.01))
    
    pltargs = {'ls': next(LS)}
    pltargs['label'] = '$\omega_n$='+str(omega_n[i])
    ax.plot(t, y, **pltargs)

ax.set_xticks(np.arange(0, 5.2, step=1.0))
plot_set(ax, 't', 'y', 'best')

plt.show()
# fig.savefig("2nd_step3.pdf", transparent=True, bbox_inches="tight", pad_inches=0.0)