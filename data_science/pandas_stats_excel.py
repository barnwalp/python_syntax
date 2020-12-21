import pandas as pd


df = pd.read_excel('modified.xlsx')

# Following line will group by the value of Type 1 and provide the mean value
# for its data; you may also sort the resulting table
# print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

# print(df.groupby(['Type 1']).count())
df['count'] = 1
print(df.columns.values)
print(df.groupby(['Type 1']).count()['count'])
print(df.groupby(['Type 1', 'Type 2']).count()['count'])

# Working with large amount of data
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results])

print(new_df)
