import json
from matplotlib import pyplot as plt
import numpy as np

filename = 'gdp_json.json'
with open(filename) as f:
    gdp_list = json.load(f)
country_gdps = [{}, {}, {}, {}, {}]
country_codes = ['CHN', 'USA', 'JPN', 'RUS', 'CAN']
for gdp_dict in gdp_list:
    for i, country_code in enumerate(country_codes):
        if gdp_dict['Country Code'] == country_code:
            year = gdp_dict['Year']
            if 2000 < year < 2017:
                country_gdps[i][year] = gdp_dict['Value']

country_gdp_list = [[], [], [], [], []]
x_data = range(2001, 2017)
for i in range(len(country_gdp_list)):
    for year in x_data:
        country_gdp_list[i].append(country_gdps[i][year] / 1e8)

bar_width = 0.15
fig = plt.figure(dpi=128, figsize=(15, 9))
colors = ['indianred', 'steelblue', 'gold', 'lightpink', 'seagreen']
countries = ['中国', '美国', '日本', '俄罗斯', '加拿大']

for i in range(len(colors)):
    plt.bar(x=np.arange(len(x_data)) + bar_width * i, height=country_gdp_list[i],
            label=countries[i], width=bar_width, color=colors[i], alpha=0.8)
    if i < 2:
        for x, y in enumerate(country_gdp_list[i]):
            plt.text(x, y + 100, '%.0f' % y, ha='center', va='bottom')

# 这行代码重新设置了x轴的标签
plt.xticks(np.arange(len(x_data)) + bar_width * 2, x_data)

plt.xlabel('年份')
plt.ylabel('GDP（亿美元）')
plt.legend()

plt.show()
