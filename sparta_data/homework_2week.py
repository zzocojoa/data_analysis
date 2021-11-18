import pandas as pd
import matplotlib.pyplot as plt
population04 = pd.read_csv('./sparta_data/week02/data/population04.csv')

city04 =  population04.groupby('군구').sum()['유동인구수'].sort_values(ascending = True)


plt.rcParams['font.family'] = "AppleGothic"

plt.figure(figsize=(20,5))
plt.bar(city04.index, city04)
plt.title('4월의 구별 유동인구수')

population04_gangnam = population04[population04['군구']=='강남구']
population04_gangnam_data = population04_gangnam.groupby('일자').sum()['유동인구수']

plt.figure(figsize=(20,5))

date_list = []
for date in population04_gangnam_data.index:
    date_list.append(str(date))

plt.plot(date_list, population04_gangnam_data)
plt.xticks(rotation= 90)
plt.title('4월 일자별 강남구 유동인구수')

population07 = pd.read_csv('./sparta_data/week02/data/population07.csv')
population07 = population07[population07['군구']=='강남구']
population07 = population07.groupby('일자').sum()['유동인구수']

plt.figure(figsize=(20,5))
date_list = [str(date) for date in population04_gangnam_data.index]
date_list2 = [str(date) for date in population07.index]
plt.plot(date_list, population04_gangnam_data)
plt.plot(date_list2, population07)
plt.xticks(rotation= 90)
plt.title('4월과 7월 일자별 강남구 유동인구수')
plt.show()