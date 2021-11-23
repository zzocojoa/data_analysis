from os import makedirs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from PIL import Image
import matplotlib.font_manager as fm

# wordcloud
mysong = open('./sparta_data/week03/data/mysong.txt', 'r', encoding='utf-8-sig')
result = mysong.read().replace('\n', ' ')

for number in range(1, 11):
    result = result + result

for f in fm.fontManager.ttflist:
    if "Gothic" in f.name:
        print(f.fname)

font_path = 'C:\WINDOWS\Fonts\malgun.ttf'

mask = np.array(Image.open('./sparta_data/week03/data/cartoon-rock-musician.jpg'))
wc = WordCloud(font_path=font_path, background_color='white', mask=mask)
wc.generate(result)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(50,50))
plt.axis('off')
plt.imshow(wc)
plt.show()


# 월요일과 화요일의 수강완료 시간 비교
sparta_data = pd.read_csv('./sparta_data/week03/data/enrolleds_detail.csv')

format = '%Y-%m-%dT%H:%M:%S.%f'
sparta_data['done_date_time'] = pd.to_datetime(sparta_data['done_date'], format=format)
sparta_data['done_date_time_hour'] = sparta_data['done_date_time'].dt.hour
sparta_data['done_date_time_weekday'] = sparta_data['done_date_time'].dt.day_name()

sparta_data_monday = sparta_data[sparta_data['done_date_time_weekday'] == 'Monday']
sparta_data_tuesday = sparta_data[sparta_data['done_date_time_weekday'] == 'Tuesday']

sparta_data_mondaye = sparta_data_monday.groupby('done_date_time_hour')['user_id'].count()
sparta_data_tuesday = sparta_data_tuesday.groupby('done_date_time_hour')['user_id'].count()

weeks = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(10,10))
plt.plot(sparta_data_mondaye.index, sparta_data_mondaye)
plt.plot(sparta_data_tuesday.index, sparta_data_tuesday)
plt.xticks(np.arange(24))
plt.show()
