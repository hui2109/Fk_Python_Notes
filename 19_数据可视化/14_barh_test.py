import matplotlib.pyplot as plt
import numpy as np

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data1 = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
bar_width = 0.3

plt.barh(y=range(len(x_data)),
         width=y_data1,
         label='疯狂Java讲义',
         color='steelblue',
         alpha=0.8,
         height=bar_width)
plt.barh(y=np.arange(len(x_data)) + bar_width + 0.05,
         width=y_data2,
         label='疯狂Android讲义',
         color='indianred',
         alpha=0.8,
         height=bar_width)

for y, x in enumerate(y_data1):
    plt.text(x + 5000, y - bar_width / 2, '%s' % x, ha='center', va='bottom')
for y, x in enumerate(y_data2):
    plt.text(x + 5000, y + bar_width / 2, '%s' % x, ha='center', va='bottom')
plt.title('Java和Android销量对比')
plt.xlabel('年份')
plt.ylabel('销量')
plt.legend()
plt.yticks(np.arange(len(x_data)) + bar_width / 2, x_data)
plt.show()
