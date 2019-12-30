import pandas as pd 
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'], 'Max Speed': [380., 370., 24., 26.]}) 
print(df.groupby(['Animal']).count()) 
print(df.groupby(['cylinders']).count())