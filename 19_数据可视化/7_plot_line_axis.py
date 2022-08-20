import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data1 = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

plt.plot(x_data, y_data1, color='red', linewidth=2.0, linestyle='--', label='疯狂Java讲义年销量')
plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.', label='疯狂Android讲义年销量')

plt.legend(loc='best')
plt.xlabel('年份')
plt.ylabel('图书销量（本）')
plt.title('疯狂图书的历年销量')
plt.yticks([50000, 70000, 100000], [r'挺好', r'优秀', r'火爆'])

ax = plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 70000))

plt.show()
