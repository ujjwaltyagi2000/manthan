import pandas as pd
import numpy as np
import os

# some columns have incorrect data types
# they must be corrected manually

# --> the values below will be changed until all datasets have corrected data types
# paths
file_name = "winning_turnout.csv"
directory = "../data/processed"
file_path = os.path.join(directory, file_name)

# files -->
'''
['candidate_background.csv', 'candidate_list_turnout.csv', 'census_data.csv', 'combined_economic_indicators.csv', 'literacy_data.csv', 'religion_data.csv', 'sc_st_data.csv', 
'slums_data.csv', 'winning_background.csv', 'winning_turnout.csv']
'''

df = pd.read_csv(file_path)
# df.info()

# column name
# column = 'votes'

# df[column] = df[column].astype("Int64")

# # for converting float columns to ints-->
# int_columns = ["age", "criminal_cases", "total_assets", "liabilities", "year"]
# df[int_columns] = df[int_columns].astype("Int64")

# null_nan_count = df[column].isnull().sum()
# # Check for empty strings (if the column is object dtype)
# empty_count = (df[column].astype(str).str.strip() == '').sum()

# print(f"null_nan_count: {null_nan_count}, empty_count: {empty_count}") 

# df[column] = pd.to_numeric(df[column], errors='coerce').astype('Int64')

# df.to_csv(file_path, index=False)
df.info()
