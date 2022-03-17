import pandas as pd

df = pd.read_csv("c:\\python_temp\\workspace\\code\\week1\\week4\\lambda_map_apply\\wages.csv")
print(df.sex.unique())
df["sex_code"] = df.sex.map({"male": 0 , "female" : 1})
print(df.head(5))

#Replace 함수
df.sex.replace({'male': 0, 'female': 1}).head()
df.sex.replace(['male','female'], [0,1],inplace=True)
print(df.head(5))

#APPLY for datafrae
df_info = df[["earn", 'height', 'age']]
f = lambda x: x.max()-x.min()
print(df_info.apply(f))

#내장 연산 함수 사용시 똑같은 효과
print(df_info.sum())
print(df_info.apply(sum))

#scalar값 이외에 series값의 반환 가능
def f(x):
    return pd.Series([x.min(), x.max()], index= ["min","max"])
df_info.apply(f)

#applymap for dataframe
#series단위가 아닌 element단위로 ㅎ마수 적용
#series단위에 apply적용시킬 때와 같은 효과

f = lambda x: -x
print(df_info.applymap(f).head(5))
print(df_info["earn"].apply(f).head(5))
