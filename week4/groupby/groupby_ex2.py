import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)
#1. grouped
grouped = df.groupby("Team")
#group에 의해 split된 상태 추출 가능
for name,group in grouped:
    print(name)
    print(group)
#2. get_group
#: 특정 key 값을 가진 그룹의 정보만 추출 가능
print(grouped.get_group("Devils"))

