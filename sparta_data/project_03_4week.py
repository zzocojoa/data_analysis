from datetime import date, datetime
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns

code = pd.read_csv('./sparta_data/week04/data/corpgeneral.csv')

code = code[['회사명', '종목코드']]

code_result = code.rename(columns={'회사명':'corp', '종목코드':'code'})


# # 종목 코드번호 추출
    # corp_name = '카카오'
    # condition = f"corp=='{corp_name}'" 


    # kakao = code_result.query(condition) # 조건 부합 데이터 추출 query
    # kakao = kakao['code']
    # kakao_string = kakao.to_string(index=False) # index=False로 인덱스 값 제거
    # kakao_string = kakao_string.strip() # strip 공백 제거
    # kakao_code = kakao_string.rjust(6, '0') # 6 자릿수 만들어주기

    # kakao_stock_df = web.DataReader(kakao_code, 'naver')

# 종목 코드번호 추출
def get_code(code_result, corp_name):
    condition = f"corp=='{corp_name}'"
    code = code_result.query(condition)['code'].to_string(index=False).strip().rjust(6, '0')
    
    return code

samsung_code = get_code(code_result, '삼성전자')

companies = ['삼성전자', 'LG전자', '카카오', 'NAVER', 'CJ', '한화', '현대자동차', '기아자동차']

samsung_stock_df = web.DataReader(samsung_code, 'naver')
samsung_stock_df['Close'] = samsung_stock_df['Close'].astype(int)

start = datetime(2020, 1, 1)
end = datetime(2020, 12, 31)

stock_of_companies = pd.DataFrame({'Date':pd.date_range(start=start, end=end)})

for company in companies:
    company_code = get_code(code_result, company)
    stock_df = web.DataReader(company_code, 'naver', start, end)
    stock_of_companies = stock_of_companies.join(pd.DataFrame(stock_df['Close'].astype(int)).rename(columns={'Close':company}), on='Date')

corr_data = stock_of_companies.corr()

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(15,10))
sns.heatmap(data=corr_data, annot=False, fmt='.2f', linewidths=.5, cmap='Blues') # fmt='.2f' / 소수점 2자리, linewidths=.5 / 칸간 간격, cmap='Blues' / 색상
plt.show()

print(corr_data)