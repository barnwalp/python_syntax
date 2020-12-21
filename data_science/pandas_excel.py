import pandas as pd
from openpyxl import load_workbook


# Get the data from the csv file
# for tab separated file, second argument to be passed as
# delimiter='\t'
df = pd.read_csv('pokemon_data.csv')
# Print the loaded data
# print(df)

# printing top 3 and bottom 3 rows of the loaded data
# print(df.head(3))
# print(df.tail(3))

wb = load_workbook('empty_book.xlsx')

# loading excel file
df_xlsx = pd.read_excel('empty_book.xlsx', sheet_name='Data')
# print(df_xlsx)

# Getting the table header
print(df.columns)

# Getting all the value of a column
print(df['Name'])

# Getting the first 5 value of the column
print(df['Name'][:5])

# Getting multiple columns of the table
print(df[['Name', 'Type 1', 'HP']])

# Getting first 4 rows
print(df.head(4))
print(df.iloc[1:4])

# Read a specific Location(R, C)
print(df.iloc[2, 1])

# iterating through all rows and value
for index, row in df.iterrows():
    # index is the row value and row is data of that index with the header
    print(index, row)

# Getting the specific rows which meet some criteria
print(df.loc[df['Type 1'] == "Fire"])
