import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data1 = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

stack_bar = pygal.StackedBar()

stack_bar.add('疯狂Java讲义', y_data1)
stack_bar.add('疯狂Android讲义', y_data2)

stack_bar.x_labels = x_data
stack_bar.y_labels = (20000, 40000, 60000, 80000, 100000)
stack_bar.x_title = '销量'
stack_bar.y_title = '年份'
stack_bar.title = '疯狂图书的历年销量'

stack_bar.legend_at_bottom = True

stack_bar.render_to_file('fk_books5.svg')
