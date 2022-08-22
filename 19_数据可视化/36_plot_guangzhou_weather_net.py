import re
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from urllib.request import *
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def get_html(city, year, month):
    url = 'https://lishi.tianqi.com/' + city + '/' + str(year) + str(month) + '.html'
    request = Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64)' +
                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    response = urlopen(request)
    return response.read().decode('utf-8')


dates, highs, lows = [], [], []
city = 'chengdu'
year = '2021'
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
pre_day = datetime(2020, 12, 31)
for month in months:
    html = get_html(city, year, month)
    text = ''.join(html.split())
    pattern = re.compile(r'<divclass="tian_three">(.*?)</div><script>')
    table = re.findall(pattern, text)
    pattern1 = re.compile('(?:<li>|<liclass="hide">)(.*?)</li>')

    uls = re.findall(pattern1, table[0])

    for ul in uls:
        pattern2 = re.compile(r'>(.*?)</div>')
        lis = re.findall(pattern2, ul)
        d_str = re.findall(r'(.*?)星', lis[0])[0]
        try:
            cur_day = datetime.strptime(d_str, '%Y-%m-%d')
            high = int(lis[1][:-1])
            low = int(lis[2][:-1])
        except ValueError:
            print(cur_day, '数据出现错误')
        else:
            diff = cur_day - pre_day
            if diff != timedelta(days=1):
                print('%s之前少了%d天的数据' % (cur_day, diff.days - 1))
            dates.append(cur_day)
            highs.append(high)
            lows.append(low)
            pre_day = cur_day

fig = plt.figure(dpi=128, figsize=(12, 9))
plt.plot(dates, highs, c='red', alpha=0.5, label='最高气温', linewidth=2.0)
plt.plot(dates, lows, c='blue', alpha=0.5, label='最低气温', linewidth=2.0)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.xlabel('日期')
plt.ylabel('气温（℃）')
fig.autofmt_xdate()

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.title('%s年成都最高气温和最低气温' % year)
plt.legend()

plt.show()
