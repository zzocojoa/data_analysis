import pandas as pd
import matplotlib.pyplot as plt
import folium
import json
import webbrowser

plt.rcParams['font.family'] = 'Malgun Gothic'

population = pd.read_csv('./sparta_data/week02/data/population07.csv')
population_tail = population.tail(5)
population_list = list(population), len(list(population))
population_age = set(population['연령대(10세단위)']), len(set(population['연령대(10세단위)']))
population_si = set(population['시']), len(set(population['시']))
population_gun = set(population['군구']), len(set(population['군구']))
sorted_sum_of_population_by_gu = population.groupby('군구')['유동인구수'].sum().sort_values(ascending=True)

# plt.figure(figsize=(10,5))
# plt.bar(sorted_sum_of_population_by_gu.index, sorted_sum_of_population_by_gu)
# plt.title('2020년 7월 서울 군구별 유동인구 수')
# plt.xlabel('군구')
# plt.ylabel('유동인구수')
# plt.xticks(rotation=-45)
# plt.show()

population_gangnam = population[population['군구'] == '강남구']
population_gangnam_daily = population_gangnam.groupby('일자')['유동인구수'].sum()

plt.figure(figsize=(10,5))

date = []
for day in population_gangnam_daily.index:
    # print(day)
    date.append(str(day))

plt.plot(date, population_gangnam_daily)
plt.title('2020년 7월 서울 강남구 날짜별 유동인구 수')
plt.xlabel('날짜')
plt.ylabel('유동인구수')
plt.xticks(rotation=90)
# plt.show()

output_file = 'index.html'
m = folium.Map(location=[37.5502, 126.982], zoom_start=11, tiles='stamentoner')

seoul_stage_geo = './sparta_data/week02/data/seoul_geo.json'
geo_data = json.load(open(seoul_stage_geo, encoding='utf-8'))
folium.Choropleth(geo_data=geo_data,
                  data=sorted_sum_of_population_by_gu,
                  columns=[sorted_sum_of_population_by_gu.index, sorted_sum_of_population_by_gu],
                  fill_color='PuRd',
                  key_on='properties.name'
                  ).add_to(m)

m.save(output_file)
webbrowser.open(output_file)

