import pandas as pd 

df = pd.read_csv("student_data.csv")
#print(df.shape)
#print(df.head(5))
#print(df.info())
print(len(df))
print(type(df))
print(df.columns)
print(df.dtypes)
print(df.describe())
