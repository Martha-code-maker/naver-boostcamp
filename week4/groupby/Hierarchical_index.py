import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}

df = pd.DataFrame(ipl_data)
h_index = df.groupby(["Team","Year"])["Points"].sum()

#index
print(h_index.index)
print(h_index["Devils":"Kings"])  

#unstack
print(h_index.unstack()) #groupby로 묶인 data를 matrix 형태로 전환

#sawplevel
print(h_index.swaplevel())#"Team"과 "Year"의 순서를 바꿔서 출력

#operation
print(h_index.sum(level=0)) #index level=0: "team" 끼리 더하기
print(h_index.sum(level=1)) #index level=1 : "year"끼리 더하기

