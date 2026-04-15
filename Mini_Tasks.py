import pandas as pd

df=pd.read_csv("students.csv")

print(df.shape)
print(df.columns)
print(df.describe())
print("Passed students:\n",df[df['passed'] == 'Yes'])
print("attendance of students:\n",df['attendance']>80)
print(df.groupby('gender').mean())
print(df.add(["math_score,english_score,science_score"]))