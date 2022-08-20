import matplotlib.pyplot as plt

data = [0.16881, 0.14966, 0.07471, 0.06992, 0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
labels = ['Java', 'C', 'C++', 'Python', 'Visual Basic .NET', 'C#', 'PHP', 'JavaScript', 'SQL', 'Assembly language',
          '其他']
explode = [0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0]
colors = ['red', 'pink', 'magenta', 'purple', 'orange']
plt.axes(aspect='equal')
plt.xlim(0, 8)
plt.ylim(0, 8)

plt.pie(x=data,
        labels=labels,
        explode=explode,
        colors=colors,
        autopct='%.3f%%',
        pctdistance=0.8,
        labeldistance=1.15,
        startangle=180,
        radius=3.8,
        center=(4, 4),
        counterclock=False,
        wedgeprops={'linewidth': 1, 'edgecolor': 'green'},
        textprops={'fontsize': 12, 'color': 'black'},
        frame=1)
plt.xticks()
plt.yticks()
plt.title('2018年8月的编程语言指数排行榜')
plt.show()
