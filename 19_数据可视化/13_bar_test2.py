import matplotlib.pyplot as plt
import numpy as np

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data1 = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
bar_width = 0.3

plt.bar(x=range(len(x_data)),
        height=y_data1,
        label='疯狂Java讲义',
        color='steelblue',
        alpha=0.8,
        width=bar_width)
plt.bar(x=np.arange(len(x_data)) + bar_width + 0.05,
        height=y_data2,
        label='疯狂Android讲义',
        color='indianred',
        alpha=0.8,
        width=bar_width)

for x, y in enumerate(y_data1):
    plt.text(x, y + 300, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
    plt.text(x + bar_width+0.1, y + 2500, '%s' % y, ha='center', va='center_baseline')
plt.title('Java和Android销量对比')
plt.xlabel('年份')
plt.ylabel('销量')
plt.legend()
plt.xticks(np.arange(len(x_data)) + bar_width / 2, x_data)
plt.show()
