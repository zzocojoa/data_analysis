import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

enroll = pd.read_csv('./sparta_data/week03/data/enrolleds_detail.csv')
lectures = pd.read_csv('./sparta_data/week03/data/lectures.csv')

# lecture_id에 따른 user_id 수
enroll_detail = enroll.groupby('lecture_id')['user_id'].count()

plt.figure(figsize=(22,5))
plt.bar(enroll_detail.index, enroll_detail)
plt.title('강의에 따른 수강완료 수의 합계')
plt.xlabel('강의_id')
plt.ylabel('user_id')
plt.xticks(rotation=90)

# enroll_detail를 DataFrame으로 만든다.(합치기 위한 작업)
lecture_count = pd.DataFrame(enroll_detail)

# reset_index를 통해 새로운 Exel / colums을 부여
lecture_count = lecture_count.reset_index()

# 다른 이용자가 헷갈리지 않게 user_id를 count로 변환
lecture_count = lecture_count.rename(columns={'user_id':'count'})

# lecture_id로 합쳐주기 위해 set_index를 lecture_id로 변경
lectures = lectures.set_index('lecture_id')

# lectures의 matrix에 lecture_count를 join해준다.
full_lecture = lecture_count.join(lectures, on='lecture_id')
plt.figure(figsize=(22,5))
plt.bar(full_lecture['title'], full_lecture['count'])
plt.title('강의에 따른 수강완료 수의 합계')
plt.xlabel('강의명')

plt.xticks(rotation=90)
plt.show()