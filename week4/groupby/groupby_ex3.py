import pandas as pd
import numpy as np
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)
grouped = df.groupby("Team")

#1. aggregation
#:요약된 통계정보를 추출
print(grouped.agg(sum))
print(grouped.agg(np.mean))
print(grouped.agg([np.sum, np.mean,np.std]))

#2.transformation
# 개별 데이터 변환을 지원
score = lambda x: (x-x.mean())/x.std()
print(grouped.transform(score))

#3.filter
#:특정 조건으로 데이터를 검색할 때 사용
print(grouped.filter(lambda x:len(x) >= 3)) #len(x): grouped된 dataframe의 개수
