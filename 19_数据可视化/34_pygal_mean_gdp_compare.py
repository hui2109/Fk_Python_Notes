import json
import pygal

filename = 'gdp_json.json'
with open(filename) as f:
    gdp_list = json.load(f)
pop_filename = 'population-figures-by-country.json'
with open(pop_filename) as f:
    pop_list = json.load(f)

country_mean_gdps = [{}, {}, {}, {}]
country_codes = ['USA', 'JPN', 'RUS', 'CAN']
for gdp_dict in gdp_list:
    for i, country_code in enumerate(country_codes):
        if gdp_dict['Country Code'] == country_code:
            year = gdp_dict['Year']
            if 2000 < year < 2017:
                for pop_dict in pop_list:
                    if pop_dict['Country_Code'] == country_code:
                        country_mean_gdps[i][year] = round(gdp_dict['Value'] / pop_dict['Population_in_%d' % year])

country_mean_gdp_list = [[], [], [], []]
x_data = range(2001, 2017)
for i in range(len(country_mean_gdp_list)):
    for year in x_data:
        country_mean_gdp_list[i].append(country_mean_gdps[i][year])
countries = ['美国', '日本', '俄罗斯', '加拿大']

bar = pygal.Bar()
for i in range(len(countries)):
    bar.add(countries[i], country_mean_gdp_list[i])

bar.width = 1100
bar.x_labels = x_data
bar.x_labels_rotation = 45

bar.x_title = '年份'
bar.y_title = '人均GDP（美元）'
bar.title = '从2001年到2016年各国人均GDP对比'
bar.legend_at_bottom = True

bar.render_to_file('mean_gdp_compare.svg')
