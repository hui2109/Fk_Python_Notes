import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (-Y - 1) ** 2)
Z = (Z1 - Z2) * 2
plt.contourf(x, y, Z, 16, alpha=0.75, cmap='rainbow')
c = plt.contour(x, y, Z, 16, colors='black', linewidth=0.5)
plt.clabel(c, inline=True, fontsize=10)
plt.xticks()
plt.yticks()
plt.title('等高线图')
plt.xlabel('维度')
plt.ylabel('经度')
plt.show()
