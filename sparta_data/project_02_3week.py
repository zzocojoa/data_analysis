import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.formats.format import format_array

plt.rcParams['font.family'] = 'Malgun Gothic'

sparta_data = pd.read_csv('./sparta_data/week03/data/enrolleds_detail.csv')

format = '%Y-%m-%dT%H:%M:%S.%f' 
sparta_data['done_data_time'] = pd.to_datetime(sparta_data['done_date'], format=format)

# 요일 부여(.dt.day_name())
sparta_data['done_date_time_weekday'] = sparta_data['done_data_time'].dt.day_name()

weekdata = sparta_data.groupby('done_date_time_weekday')['user_id'].count()

weeks = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

weekdata = weekdata.agg(weeks) # aggregation

# 요일별 수강완료 수강생 수 (bar)
plt.figure(figsize=(8,5))
plt.bar(weekdata.index, weekdata)
plt.title('요일별 수강완료 수강생 수')
plt.xlabel('요일')
plt.ylabel('수강생(명)')
plt.xticks(rotation=90)

# 시간 부여(.dt.hour)
sparta_data['done_date_hour']= sparta_data['done_data_time'].dt.hour

hour_data = sparta_data.groupby('done_date_hour')['user_id'].count().sort_index()

# 시간별 수강완료 수(plot)
plt.figure(figsize=(10,5))
plt.plot(hour_data.index, hour_data)
plt.title('시간별 수강완료 수')
plt.xlabel('시간')
plt.ylabel('사용자(명)')
plt.xticks(np.arange(24))

# pivot_table
# pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, margins_name='All')
# data: 분석할 데이터
# values: 분석할 수
# index: 행 인덱스
# columns: 열 인덱스
# aggfunc: 분석 방법(aggregation function)
sparta_data_pivot_table = pd.pivot_table(sparta_data, values='user_id', aggfunc='count',
                                        index=['done_date_time_weekday'],
                                        columns=['done_date_hour']
                                        ).agg(weeks)

# 요일별 종료 시간 히트맵(pivot_table)
plt.figure(figsize=(14,5))
plt.pcolor(sparta_data_pivot_table)
plt.xticks(np.arange(0.5, len(sparta_data_pivot_table.columns), 1), sparta_data_pivot_table.columns) # 위치 지정만 해준다
plt.yticks(np.arange(0.5, len(sparta_data_pivot_table.index), 1), sparta_data_pivot_table.index)
plt.title('요일별 종료 시간 히트맵')
plt.xlabel('시간')
plt.ylabel('요일')
plt.colorbar()
plt.show()


print(sparta_data_pivot_table)