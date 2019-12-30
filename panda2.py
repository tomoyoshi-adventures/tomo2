import pandas as pd
import numpy as np 
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD')) #dataframe.transpose() then you will reverse the matrix so you can get correlation by rows

print(df.shape)
print(df.head(df.shape[0]))
print("Number of rows:" + str(df.shape[0]))
print("Number of columns:" + str(df.shape[1]))

df_mean = df.mean() # Mean(average) column per column
print("-------")
print(df_mean)
print(type(df_mean))
print("-------")

df_max = df.max() # Max value in each column
print("Max value: " + str(df_max))
print("-------")

df_min = df.min() # Min value in each column
print("Min value: " + str(df_min))
print("-------")

df_sum = df.sum()
df_sum_columns = df.sum(axis=0) # Sum of the values in each columns 
print("Sum of column values: " + str(df_sum_columns))
df_sum_rows = df.sum(axis=1) # Sum of the values in each rows 
print("Sum of row values: " + str(df_sum_rows))
print("-------")

df_count = df.count() # Count non-NA cells for each column or row.
df_count_columns = df.count(axis=0) # Count non-NA cells for each column.
print("Count of columns:" + str(df_count_columns))
df_count_rows = df.count(axis=1) # Count non-NA cells for each row.
print("Count of rows:" + str(df_count_rows))
print("-------")

df_diff = df.diff() # First discrete difference of element
df_diff_columns = df.diff(axis=0)
print("Diff columns:" +str(df_diff_columns))
df_diff_rows = df.diff(axis=1)
print("Diff rows:" +str(df_diff_rows))


# standard correlation coefficient.  

# Other possible methods are: â€šÀÃ²kendallâ€šÀÙ and â€šÀÃ²spearmanâ€šÀÙ
df_corr_pears= df.corr(method='pearson')
print("Pearson correlation:" +str(df_corr_pears))
df_corr_spearman= df.corr(method='spearman')
print("Pearson correlation(spear):" +str(df_corr_spearman))
df_corr_kendall= df.corr(method='kendall')
print("Pearson correlation(kendall):" +str(df_corr_kendall))
print("-------transpose:")
#print(df)
#print(df.transpose())
df_transpose_pear=df.transpose().corr(method='pearson')
print("Pearson correlation:" +str(df_transpose_pear))
df_transpose_spearman=df.transpose().corr(method='spearman')
print("Pearson correlation(spear):" +str(df_transpose_spearman))
df_transpose_kendall=df.transpose().corr(method='kendall')
print("Pearson correlation(kendall):" +str(df_transpose_kendall))
