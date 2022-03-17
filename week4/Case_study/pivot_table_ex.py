import dateutil
import pandas as pd

df_phone = pd.read_csv("c:\\python_temp\\workspace\\code\\week1\\week4\\Case_study\\phone_data.csv")
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)

print(df_phone.pivot_table(["duration"], index=[df_phone.month, df_phone.item],
                     columns=df_phone.network, aggfunc="sum", fill_value=0))