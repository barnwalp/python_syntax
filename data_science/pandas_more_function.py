import pandas as pd


df = pd.read_csv('pokemon_data.csv')
# provide the stastics details of the table
# print(df.describe())

# Sorting the table in descending order
# print(df.sort_values('Name', ascending=False))

# Sorting the table with multiple column
# print(df.sort_values(['Type 1', 'HP'], ascending=True))

# Creating a column by adding several column value
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# Delete a column
df = df.drop(columns=['Total'])

# Faster way to add column by using iloc
# axis=1 implies that summation will be done horizontally, 0 for vertically
# [:, 4:10] means all rows from column 4 to 9
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df.head(5))

# Getting column as a list
cols = list(df.columns.values)

# rearranging the table columns
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# saving to the csv file, false index will ensure that no index is added
df.to_csv('modified.csv', index=False)

# saving the csv as excel file
df.to_excel('modified.xlsx', index=False)
