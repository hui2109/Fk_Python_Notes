import json

filename = 'gdp_json.json'
with open(filename) as f:
    gdp_list = json.load(f)
for gdp_dict in gdp_list:
    if gdp_dict['Year'] == 2016 and gdp_dict['Country Code'] == 'CHN':
        print(gdp_dict['Country Name'], gdp_dict['Value'])
