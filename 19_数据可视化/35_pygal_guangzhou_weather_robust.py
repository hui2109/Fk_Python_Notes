import csv
import pygal
from datetime import datetime
from datetime import timedelta

filename = 'guangzhou-2017.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    shades, sunnys, cloudys, rainys = 0, 0, 0, 0
    prev_day = datetime(2016, 12, 31)
    for row in reader:
        try:
            cur_day = datetime.strptime(row[0], '%Y-%m-%d')
            description = row[3]
        except ValueError:
            print(cur_day, '数据出现错误')
        else:
            diff = cur_day - prev_day
            if diff != timedelta(days=1):
                print(diff)
                print(diff.days)
                print('%s之前少了%d天的数据' % (cur_day, diff.days - 1))
            prev_day = cur_day
            if '阴' in description:
                shades += 1
            elif '晴' in description:
                sunnys += 1
            elif '云' in description:
                cloudys += 1
            elif '雨' in description:
                rainys += 1
            else:
                print(description)

pie = pygal.Pie()
pie.add('阴', shades)
pie.add('晴', sunnys)
pie.add('多云', cloudys)
pie.add('雨', rainys)

pie.title = '2017年广州天气汇总'
pie.legend_at_bottom = True

pie.render_to_file('guangzhou-weather-robust.svg')
