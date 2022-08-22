import pygal

data = [
    [5, 4.0, 5, 5, 5],
    [4.8, 2.8, 4.8, 4.8, 4.9],
    [4.5, 2.9, 4.6, 4.0, 4.9],
    [4.0, 4.8, 4.9, 4.0, 5],
    [3.0, 4.2, 2.3, 3.5, 2],
    [4.8, 4.3, 3.9, 3.0, 4.5]
]
labels = ['Java', 'C', 'C++', 'Python', 'C#', 'PHP']

radar = pygal.Radar()

for i, per in enumerate(data):
    radar.add(labels[i], per)

radar.x_labels = ['平台健壮性', '语法易用性', '社区活跃度', '市场份额', '未来趋势']
radar.title = '编程语言对比'
radar.dots_size = 6
radar.legend_at_bottom = True

radar.render_to_file('fk_books10.svg')
