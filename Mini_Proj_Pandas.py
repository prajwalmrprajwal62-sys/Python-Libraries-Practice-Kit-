import pandas as pd

df=pd.read_csv("student_data.csv")

print(df.shape)
print(df.columns)
print(df.describe())
print(len(df))
print(df.groupby('mood').mean())

print("\nFocused students : \n",df[df['marks']>65].reset_index(drop=True))
print("\nTired students : \n",df[df['marks']<65].reset_index(drop=True))