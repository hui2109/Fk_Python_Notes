import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'guangzhou-2017.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    start_date = datetime(2017, 6, 30)
    end_date = datetime(2017, 8, 1)
    dates, highs, lows = [], [], []
    for row in reader:
        d = datetime.strptime(row[0], '%Y-%m-%d')
        if start_date < d < end_date:
            dates.append(d)
            highs.append(int(row[1]))
            lows.append(int(row[2]))

# 配置图形
fig = plt.figure(dpi=128, figsize=(12, 9))
plt.plot(dates, highs, c='red', label='最高气温', alpha=0.5,
         linewidth=2.0, linestyle='-', marker='v')
plt.plot(dates, lows, c='blue', label='最低气温', alpha=0.5,
         linewidth=3.0, linestyle='-.', marker='o')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.xlabel('日期')
plt.ylabel('气温（℃）')
fig.autofmt_xdate()
plt.title('2017年7月广州最高气温和最低气温')

plt.legend()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
