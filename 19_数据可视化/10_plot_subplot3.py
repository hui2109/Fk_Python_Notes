import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x_data = np.linspace(-np.pi * 2, np.pi * 2, 128, endpoint=True)

gs = plt.GridSpec(2, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0])
ax3 = plt.subplot(gs[1, 1:3])

ax1.plot(x_data, np.sin(x_data))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.set_title('正弦曲线')

ax2.plot(x_data, np.cos(x_data))
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
ax2.set_title('余弦曲线')

ax3.plot(x_data, np.tan(x_data))
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
ax3.set_title('正切曲线')

plt.show()
