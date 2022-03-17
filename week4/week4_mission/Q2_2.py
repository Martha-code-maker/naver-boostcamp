import pandas as pd

df1 = pd.DataFrame({'Name' : ['cherry', 'mango','potato','onion'], 'Type': ['Fruit','Fruit','Vegetable','Vegetable'],'Price': [100,110,60,80]}
                    , columns = ["Name","Type","Price"])

df2 = pd.DataFrame({'Name' : ['pepper', 'carrot','banana','kiwi'], 'Type': ['Vegetable','Vegetable','Fruit','Fruit'],'Price': [50,70,90,120]}
                    , columns = ["Name","Type","Price"])

df3 = pd.concat([df1,df2],axis=0)

df_fruit = df3.loc[df3['Type'] == "Fruit"]
df_fruit = df_fruit.sort_values(by="Price",ascending=False)

df_veg = df3.loc[df3['Type'] == 'Vegetable']
df_veg = df_veg.sort_values(by="Price", ascending=False)

print("Sum of Top 2 Fruit Price: ", sum(df_fruit[:2]["Price"]))
print("Sum of Top 2 Vegetable Price: ",sum(df_veg[:2]['Price']))