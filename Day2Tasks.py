import pandas as pd

df2 = pd.read_csv('attendance.csv')
df1 = pd.read_csv('students.csv')

print(df1['passed'].value_counts())
print('Gender=',df1['gender'].nunique())

print(df1.merge(df2, on='name'))
print(df1.merge(df2, on='name', how='inner'))
print(df1.merge(df2, on='name', how='left'))
print(df1.merge(df2, on='name', how='right'))
