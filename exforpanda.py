import pandas as pd

df = pd.read_csv("trio.sample.vcf",delimiter ="")
print(df.head())
s_1=df.iloc(:,[0,4])
s_1.columns = ['chromosomes','refbase','altbase']
print(s_1.head())
print(s_1.groupby(by=['chromosome', 'refbase']).count())

#aggregator is necessary, we need to identify the single chromosomes(each of them)
