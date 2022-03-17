import dateutil
import pandas as pd

df_phone = pd.read_csv("c:\\python_temp\\workspace\\code\\week1\\week4\\Case_study\\phone_data.csv")
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)

print(df_phone.groupby('month')['duration'].sum())
print(df_phone[df_phone['item'] == 'call'].groupby('network')['duration'].sum())
print(df_phone.groupby(['month','item'])['date'].count())
print(df_phone.groupby(['month','item'])['date'].count().unstack())
print(df_phone.groupby(['month','item']).agg({'duration':sum,    #sum of the durations for each group
                                             'network_type': "count",   #find the number of network type entires    
                                             'date': 'first'})) #get first date per group