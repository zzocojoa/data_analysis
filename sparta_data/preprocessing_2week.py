import pandas as pd
import matplotlib.pyplot as plt

commercial = pd.read_csv('./sparta_data/week02/data/commercial.csv', encoding='utf-8-sig')

column_name = list(commercial), len(list(commercial))

commercial.groupby('상가업소번호')['상권업종소분류명'].count().sort_values(ascending=False)

category_range = set(commercial['상권업종소분류명']), len(set(commercial['상권업종소분류명']))

commercial[['시', '구', '상세주소']] = commercial['도로명'].str.split(' ', n=2, expand=True)

seoul_data = commercial[commercial['시'] == '서울특별시']

seoul_chicken_data = seoul_data[seoul_data['상권업종소분류명'] == '후라이드/양념치킨']

sorted_chicken_count_gu = seoul_chicken_data.groupby('구')['상권업종소분류명'].count().sort_values(ascending=True)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(10,5))
plt.bar(sorted_chicken_count_gu.index, sorted_chicken_count_gu)
plt.xlabel('서울특별시')
plt.xticks(rotation=45)
plt.title('구에 따른 치킨집 분포도')
plt.show()

print(sorted_chicken_count_gu)