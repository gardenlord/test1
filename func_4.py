from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

# 绘图时确定线型的生成器
def linestyle_generator():
    linestyle = ['-', '--', '-.', ':']
    lineID = 0
    while True:
        yield linestyle[lineID]
        lineID = (lineID + 1) % len(linestyle)

# 完善绘图的函数
def plot_set(fig_ax, *args):
    fig_ax.set_xlabel(args[0])
    fig_ax.set_ylabel(args[1])
    # fig_ax.grid()
    fig_ax.grid(ls=':') # ls: linestyle or ls {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
    if len(args)==3:
        fig_ax.legend(loc=args[2])

# 完善伯德图的函数
def bodeplot_set(fig_ax, *args):
    fig_ax[0].grid(which="both", ls=':')
    fig_ax[0].set_ylabel('Gain [dB]')

    fig_ax[1].grid(which="both", ls=':')
    fig_ax[1].set_xlabel('$\omega$ [rad/s]')
    fig_ax[1].set_ylabel('Phase [deg]')
    
    if len(args) > 0:
        fig_ax[1].legend(loc=args[0])
    if len(args) > 1:
        fig_ax[0].legend(loc=args[1])

