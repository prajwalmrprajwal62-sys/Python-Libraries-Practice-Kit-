import pandas as pd

df=pd.read_csv("students.csv")

print(df.shape)
print(df.columns)
print(df.describe())
print("Average scores")
print(df[['math_score', 'english_score', 'science_score']].mean())
print("Passed students:\n",df[df['passed'] == 'Yes'])
print(df[df['attendance'] > 80])
print(df.groupby('gender')[['math_score', 'english_score', 'science_score']].mean())
df['total_score']=df['math_score']+df['english_score']+df['science_score']
print(df[['name', 'total_score']])