import pygal

data = [0.16881, 0.14966, 0.07471, 0.06992, 0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
labels = ['Java', 'C', 'C++', 'Python', 'Visual Basic .NET', 'C#', 'PHP', 'JavaScript', 'SQL', 'Assembly language',
          '其他']

pie = pygal.Pie()

for i, per in enumerate(data):
    pie.add(labels[i], per)

pie.title = '2018年8月的编程语言指数排行榜'
pie.legend_at_bottom = True

pie.inner_radius = 0.4
pie.half_pie = True

pie.render_to_file('fk_books7.svg')
