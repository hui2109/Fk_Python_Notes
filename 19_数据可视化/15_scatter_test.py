import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)
plt.scatter(x_data,
            np.sin(x_data),
            c='purple',
            s=50,
            alpha=0.5,
            marker='p',
            linewidths=1,
            edgecolors=['green', 'yellow'])
plt.scatter(x_data[0],
            np.sin(x_data)[0],
            c='red',
            s=150,
            alpha=1)
plt.scatter(x_data[-1],
            np.sin(x_data)[-1],
            c='black',
            s=150,
            alpha=1)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线的散点图')
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.show()
