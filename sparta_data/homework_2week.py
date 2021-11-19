import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

population04 = pd.read_csv('./sparta_data/week02/data/population04.csv')
population07 = pd.read_csv('./sparta_data/week02/data/population07.csv')

# 4월의 유동인구가 가장 많은 구는 어디?
population04 = population04[population04['시'] == '서울']
sum_of_city04 =population04.groupby('군구')['유동인구수'].sum()

# plt.figure(figsize=(10,5))
# plt.bar(sum_of_city04.index, sum_of_city04)
# plt.title("4월의 유동인구가 가장 많은 구")
# plt.xlabel('군구')
# plt.ylabel('유동인구수')
# plt.xticks(rotation=-45)

# 4월 강남구의 일별 유동인구
gangnam_gu04 = population04[population04['군구'] == '강남구']
gangnam_gu_date04 = gangnam_gu04.groupby('일자')['유동인구수'].sum()

date04 = []

for day04 in gangnam_gu_date04.index:
    date04.append(str(day04))

# plt.figure(figsize=(20,5))
# plt.plot(date04, gangnam_gu_date04)
# plt.title('4월 강남구의 일별 유동인구 수')
# plt.xlabel('2020년 4월')
# plt.ylabel('유동인구수')
# plt.xticks(rotation=90)

# 4월과 7월 강남구의 일별 유동인구
gangnam_gu07 = population07[population07['군구'] == '강남구']
gangnam_gu_date07 = gangnam_gu07.groupby('일자')['유동인구수'].sum()

date07 = []

for day07 in gangnam_gu_date07.index:
    date07.append(str(day07))

plt.figure(figsize=(20,5))
# date_list = [str(date) for date in population04_gangnam_data.index] - for문의 짧은 문장
# date_list2 = [str(date) for date in population07.index] - for문의 짧은 문장
plt.plot(date04, gangnam_gu_date04)
plt.plot(date07, gangnam_gu_date07)
plt.xlabel('2020년 7월')
plt.ylabel('유동인구수')
plt.xticks(rotation=90)
plt.show()
