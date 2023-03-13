# 伝達関数モデルのステップ応答
# 1次遅れ系
from func_4 import *
def cross_lines(x, y, **kwargs):
    ax = plt.gca() # Get the current Axes.
    ax.axhline(y, **kwargs) # Add a horizontal line across the Axes.
    ax.axvline(x, **kwargs) # Add a vertical line across the Axes.
    ax.scatter(T, 0.632, **kwargs) # A scatter plot of y vs. x with varying marker size and/or color.

fig, ax = plt.subplots(figsize=(3, 2.3))

(T, K) = (0.5, 1) 
P = tf([0, K], [T, 1]) # 一阶滞后系统
y, t = step(P, np.arange(0, 5, 0.01)) # 阶跃响应
ax.plot(t,y, color='k')

cross_lines(T, 0.632, color='k',lw=0.5) # linewidth or lw
ax.annotate('$(0.5, 0.632)$', xy=(0.7, 0.5)) # Annotate the point xy with text text.

ax.set_xticks(np.linspace(0, 5, 6))
plot_set(ax, 't', 'y')
plt.show()