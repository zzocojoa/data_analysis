import pandas as pd
import matplotlib.pyplot as plt
import folium
import json
import webbrowser

chicken07 = pd.read_csv('./sparta_data/week01/data/chicken_07.csv')
chicken08 = pd.read_csv('./sparta_data/week01/data/chicken_08.csv')
chicken09 = pd.read_csv('./sparta_data/week01/data/chicken_09.csv')

chicken_data = pd.concat([chicken07, chicken08, chicken09])
chicken_data = chicken_data.reset_index(drop=True)

# 구에 따른 치킨집 분포도
commercial = pd.read_csv('./sparta_data/week02/data/commercial.csv')
commercial_store_name = set(commercial['상권업종소분류명']) # 후라이드/양념치킨
commercial[['시', '구', '상세주소']] = commercial['도로명주소'].str.split(' ', n=2, expand=True)
commercial_list = list(commercial)

seoul_data = commercial[commercial['시'] == '서울특별시']
seoul_chicken_data = seoul_data[seoul_data['상권업종소분류명'] == '후라이드/양념치킨']
chicken_count_gu = seoul_chicken_data.groupby('구')['상권업종소분류명'].count().sort_index(ascending=True)

new_chicken_count_gu = pd.DataFrame(chicken_count_gu).reset_index()

# 서울 강남구 날짜별 유동인구 수
population = pd.read_csv('./sparta_data/week02/data/population07.csv')
sum_of_population_by_gu = population.groupby('군구')['유동인구수'].sum().sort_index(ascending=True)


# 상권과 유동인구 같이 분석
new_sum_of_population_by_gu = pd.DataFrame(sum_of_population_by_gu).reset_index()

gu_chicken = new_chicken_count_gu.join(new_sum_of_population_by_gu.set_index('군구'), on='구')

gu_chicken['유동인구수/치킨집수'] = gu_chicken['유동인구수'] / gu_chicken['상권업종소분류명']

gu_chicken = gu_chicken.sort_values(by='유동인구수/치킨집수')

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(10,5))
plt.bar(gu_chicken['구'], gu_chicken['유동인구수/치킨집수'])
plt.title('치킨집 당 유동인구 수')
plt.xlabel('구')
plt.ylabel('유동인구수/치킨집수')
plt.xticks(rotation=90)
plt.show()
# print(gu_chicken)