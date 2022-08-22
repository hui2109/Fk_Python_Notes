import pygal

data = [0.16881, 0.14966, 0.07471, 0.06992, 0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
labels = ['Java', 'C', 'C++', 'Python', 'Visual Basic .NET', 'C#', 'PHP', 'JavaScript', 'SQL', 'Assembly language',
          '其他']

gauge = pygal.Gauge()
gauge.range = [0, 1]

for i, per in enumerate(data):
    gauge.add(labels[i], per)
gauge.title = '2018年8月的编程语言指数排行榜'
gauge.legend_at_bottom = True

gauge.render_to_file('fk_books9.svg')
