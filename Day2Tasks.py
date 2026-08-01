import pandas as pd
df = pd.read_csv('students.csv')

print(df['passed'].value_counts())
print('Gender=',df['gender'].nunique())