import pandas as pd

df1 = pd.DataFrame({'Name' : ['cherry', 'mango','potato','onion'], 'Type': ['Fruit','Fruit','Vegetable','Vegetable'],'Price': [100,110,60,80]}
                    , columns = ["Name","Type","Price"])

df2 = pd.DataFrame({'Name' : ['pepper', 'carrot','banana','kiwi'], 'Type': ['Vegetable','Vegetable','Fruit','Fruit'],'Price': [50,70,90,120]}
                    , columns = ["Name","Type","Price"])

df3 = pd.concat([df1,df2],axis=0)

df_fruit = df3[df3['Type'] == 'Fruit'].sort_values(["Price"], ascending=False)
df_Veg = df3[df3['Type'] == 'Vegetable'].sort_values(["Price"], ascending=False)

print("Sum of Top 2 Fruit Price: ", df_fruit['Price'].nlargest(2).sum())
print("Sum of Top 2 Vegetable Price: ", df_Veg['Price'].nlargest(2).sum())