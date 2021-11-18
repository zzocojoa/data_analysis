import pandas as pd
import matplotlib.pyplot as plt

chicken07 = pd.read_csv('./sparta_data/week01/data/chicken_07.csv')
chicken08 = pd.read_csv('./sparta_data/week01/data/chicken_08.csv')
chicken09 = pd.read_csv('./sparta_data/week01/data/chicken_09.csv')

chicken_data = pd.concat([chicken07, chicken08, chicken09])


chicken_data = chicken_data.reset_index(drop=True)

weeks = ['월', '화', '수', '목', '금', '토', '일']

sum_of_call_by_chicken = chicken_data.groupby('요일')['통화건수'].sum().reindex(weeks)
# sum_of_call_by_chicken = chicken_data.groupby('요일')['통화건수'].sum().sort_values(ascending=True)

plt.rcParams['font.family'] = 'Malgun Gothic' # window
# plt.rcParams['font.family'] = 'AppleGothic' # mac

plt.figure(figsize=(8,5))
plt.bar(sum_of_call_by_chicken.index, sum_of_call_by_chicken)
plt.xlabel('요일')
plt.xticks(rotation=45)
plt.title('요일별 치킨 전체 주문량')
plt.show()

print(sum_of_call_by_chicken)