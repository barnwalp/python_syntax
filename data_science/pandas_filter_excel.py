import pandas as pd
import re       # import regex

df = pd.read_excel('modified.xlsx')

# filterting the column by "contains string"
# print(df.loc[df['Name'].str.contains('Mega')])

# Reverse (not contain) can be done by
# print(df.loc[~df['Name'].str.contains('Mega')])

# filter the column 'Type 1'
# or, | may also be used instead of &
new_df = df.loc[
    (df['Type 1'] == 'Grass') &
    (df['Type 2'] == 'Poison') &
    (df['HP'] > 70)
]

# Filtering using regex expression; flag=re.I will ignore cases in fire|grass
# print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])

print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

# conditional changes
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

# another column can also be changed
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

# Multiple columns can also be modified
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['t1', 't2']
print(df.loc[df['Type 1'].str.contains('Flamer')])
print(df.loc[df['Total'] > 500])

# drop will delete old index and inplace=True will change the new_df wihout
# assignment
new_df.reset_index(drop=True, inplace=True)
new_df.to_csv('modified1.csv')
