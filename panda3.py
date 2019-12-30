import pandas as pd 
df = pd.read_csv("Auto.csv", delimiter=",") 
print(df)
print(df.shape)
print(df.head(5))
print(df.describe())

s_l=df.loc[:,["mpg","cylinders","origin","name"]]#with labels
s_2=df.iloc[:,[0,1,4,8]]#slicing with indices
print(s_l)
print(s_2)
print(df.index)
print(df.columns)
#compute average weight
s_3 =df.mean().loc["weight"]
print(s_3)
df_w_sort=df.sort_values(by=['weight', 'cylinders'], ascending=False)
print(df_w_sort.loc[:,['weight','cylinders','name']])
print(df.loc[54,['weight','cylinders','name']])

df_i_sort=df.sort_index(axis=1,ascending=False)#for columns
print(df_i_sort)

print(df.groupby(['cylinders']).count())
print(df.groupby(['name']).count())