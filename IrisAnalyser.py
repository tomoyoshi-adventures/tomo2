import pandas as pd
class IrisAnalyser:
	def __init__(self):
		self.__df =pd.read_csv(petaldata.csv)
	def get_df(self):
		return self.__df
    def n_rows(self):
        return self.__df.shape[0]
    def n_cols(self):
        return self.__df.shape[1]
    def avg_petal_length(self):
        pl_slice = self.__df.loc[:,'petal_length']
        print(type(pl_slice))
    def avgs_1(self):
        return self.__df.mean()
    def avgs_2(self):
        pl_slice = self.__df.loc1:,
        #you go to git hub
        /
        /
        /
        /
        /
iris_analyserser= IrisAnalyser()
df = iris_analyserser.get_df()

#print(df.head())
print("# of rows:" + str(iris_analyser.n_rows()))
print("# of cols:" + str(iris_analyser.n_cols()))

avg_pl = iris_analyser.avg_petal_length()
print("The AVG petal length is :" + str(avg_pl))
