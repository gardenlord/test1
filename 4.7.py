from func_4 import *

# 2次遅れ系
def cross_lines(x, y, **kwargs):
    plt.gca() # Get the current Axes.
    ax.axhline(y, **kwargs) # Add a horizontal line across the Axes.
    ax.axvline(x, **kwargs) # Add a vertical line across the Axes.
    ax.scatter(x, y, **kwargs) # A scatter plot of y vs. x with varying marker size and/or color.
    
(zeta, omega_n) = (0.4, 5) # 设置阻尼系数和无阻尼自然振荡频率

fig, ax = plt.subplots(figsize=(3, 2.3))

P = tf([0,omega_n**2], [1, 2*zeta*omega_n, omega_n**2]) # Create a transfer function system. Can create MIMO systems.
y, t = step(P, np.arange(0,5,0.01))
ax.plot(t,y, color='k')

ymax = 1 + 1 * np.exp(-(np.pi*zeta)/np.sqrt(1-zeta**2)) # 最大超调量+1
Tp = np.pi/omega_n/np.sqrt(1-zeta**2) # 峰值时间
cross_lines(Tp, ymax, color='k',lw=0.5)

ax.annotate('$(T_P, y_{max)}$', xy=(1.2, 1.1))

print('ymax=',ymax)
print('Tp=', Tp)

ax.set_xticks(np.arange(0, 5.2, step=1.0))
ax.set_yticks(np.arange(0, 1.3, step=0.25))
plot_set(ax, 't', 'y')

plt.show()

'''
fyi:
https://python-control.readthedocs.io/en/0.9.3.post2/generated/control.tf.html

'''