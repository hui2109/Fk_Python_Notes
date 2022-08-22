import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data1 = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]

horizontal_line = pygal.HorizontalLine()

horizontal_line.add('疯狂Java讲义', y_data1)
horizontal_line.add('疯狂Android讲义', y_data2)

horizontal_line.x_labels = x_data
horizontal_line.y_labels = (20000, 40000, 60000, 80000, 100000)
horizontal_line.x_title = '销量'
horizontal_line.y_title = '年份'

horizontal_line.title = '疯狂图书的历年销量'

horizontal_line.render_to_file('fk_books4.svg')
