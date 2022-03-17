import pandas as pd

raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_score': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'test_score'])

raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])

#left join
print(pd.merge(df_a,df_b, on = 'subject_id', how= 'left'))

#right join
print(pd.merge(df_a,df_b,on='subject_id', how='right'))

#full(outer) join
print(pd.merge(df_a,df_b, on='subject_id', how = 'outer'))

#inner join
print(pd.merge(df_a,df_b,on ='subject_id', how='inner'))

#index based join
print(pd.merge(df_a,df_b, right_index=True, left_index= True))
