import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy.core.fromnumeric import size
from wordcloud import WordCloud

plt.rcParams['font.family'] = 'Malgun Gothic'

text = open('./sparta_data/week03/data/Sequence_01.txt', encoding='utf-8')
text = text.read()
text = text.replace('\n', ' ')

result = ""
for number in range(1, 15):
    index = '{:02}'.format(number)
    filename = 'Sequence_' + index + '.txt'
    text = open('./sparta_data/week03/data/' + filename, 'r', encoding='utf-8-sig')
    result += text.read().replace('\n', ' ')

import re # 특수문자 제거

pattern = '[^\w\s]'
text = re.sub(pattern=pattern, repl='', string=result)



import matplotlib.font_manager as fm

for f in fm.fontManager.ttflist:
    if "Gothic" in f.name:
        print(f.fname)

font_path = 'C:\WINDOWS\Fonts\malgun.ttf'

wc = WordCloud(font_path=font_path, background_color='white')
wc.generate(text)

plt.figure(figsize=(30,30))
plt.axis("off")
plt.imshow(wc)

# 행 열을 만들어 마스킹을 한다.(numpy.array)
mask = np.array(Image.open('./sparta_data/week03/data/sparta.png'))
wc = WordCloud(font_path=font_path, background_color='white', mask=mask)
wc = wc.generate(text)

# subplot 으로 2개의 이미지 표현
f = plt.figure(figsize=(30,30))
f.add_subplot(1, 2, 1) # subplot 1번째
plt.imshow(mask, cmap=plt.cm.gray) # cmap=plt.cm.gray : plt.cm에 있는 칼라맵 넘겨줌
plt.title('Original Stencil', size=40)
plt.axis('off')
f.add_subplot(1, 2, 2) # subplot 2번째
plt.imshow(wc, interpolation='nearest') # https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html
plt.title('Sparta Cloud', size=40)
plt.axis('off')

# 저장하기
f = plt.figure(figsize=(30,30))
plt.imshow(wc, interpolation='nearest')
plt.title('나만의 워드 클라우드', size=40)
plt.axis('off')
plt.show()
f.savefig('./sparta_data/week03/data/myWordCloud.png')
