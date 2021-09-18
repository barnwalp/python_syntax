import numpy as np
import pandas as pd
import re


df = pd.DataFrame([[2, 3, 4], [None, "", " "], [" ", " ", None]], columns=[
                  'a', 'b', 'c'], index=['x', 'y', 'z'])
print(df)

# Finding the location of null values
print(np.where(pd.isnull(df)))
print(f'values at location (1,0) and (2,2) is {df.iloc[1,0]}, {df.iloc[2,2]}')

# Replacing null values
print(df.replace(np.nan, "test"))

# Finding the location of empty string
print(df[df["b"] == ""])

# Replacing empty string
print(df.replace("", "empty"))
print(df.replace(" ", "space"))
print("------------------------------")
# print(df.replace(r'(\s+)', "check"))
# print(df[df["b"] == ''])

# + means 1 or more and * means 0 or more
print(df["b"].str.findall(r'\s+'))
print(df["b"].str.replace(r'\s*', "replaced"))
