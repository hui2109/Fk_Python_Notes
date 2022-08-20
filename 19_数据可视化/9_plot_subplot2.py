import matplotlib.pyplot as plt
import numpy as np

plt.figure()
x_data = np.linspace(-np.pi * 2, np.pi * 2, 128, endpoint=True)

plt.subplot(2, 1, 1)
plt.plot(x_data, np.sin(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, ], ['-2派', '-派', '0', '派', '2派'])
plt.yticks([0, 0.5, 1])
plt.title('正弦曲线')

plt.subplot(223)
plt.plot(x_data, np.cos(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, ], ['-2派', '-派', '0', '派', '2派'])
plt.yticks([0, 0.5, 1])
plt.title('余弦曲线')

plt.subplot(224)
plt.plot(x_data, np.tan(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, ], ['-2派', '-派', '0', '派', '2派'])
plt.yticks([0, 0.5, 50])
plt.title('正切曲线')

plt.show()
