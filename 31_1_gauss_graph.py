# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math
def gauss_dis(x, mu=0, sigma=1):
    left = 1 / (np.sqrt(2 * math.pi) * np.sqrt(sigma))
    right = np.exp(-(x - mu)**2 / (2 * sigma))
    return left*right

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(0.1, 10, 0.25)
X, Y = np.meshgrid(X, Y)
Z=gauss_dis(X, mu=Y/2, sigma=Y)
plt.xlabel("Position")
plt.ylabel("time")
ax.set_zlabel("probability")
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()