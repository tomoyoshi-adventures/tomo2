import pandas as pd 
df = pd.DataFrame(data = [   ['NJ', 'Towaco', 'Square'],    ['CA', 'San Francisco', 'Oval'],    ['TX', 'Austin', 'Triangle'],    ['MD', 'Baltimore', 'Square'],    ['OH', 'Columbus', 'Hexagon'],    ['IL', 'Chicago', 'Circle']  ],   columns = ['State', 'City', 'Shape']) 

s = pd.Series(data=['NJ', 'CA', 'TX', 'MD', 'OH', 'IL'])

print(df.head(2)) 
print(df.tail(3)) 
print(df.shape) 
print(df.to_numpy()) 
print(df.describe())

series = df['State'] # by label
sliced_df = df[1:4] # getting a slice
multiaxis_slice = df.loc[1:3, ['State', 'City']] #slice by label
multiaxis_slice_iloc = df.iloc[1:3, 0:2] # slice by position
