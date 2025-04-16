# this script generates SQL queries for table creation from CSV files

import pandas as pd
import os

# Directory containing CSV files
data_dir = "../data/processed"

# File to save the generated SQL queries
output_file = "create_table_queries.sql"

# returns the SQL type for a given pandas dtype
def get_sql_column_type(df):
    columns = df.columns
    sql_types = []
    
    for column, dtype in df.dtypes.items():
        if pd.api.types.is_object_dtype(dtype):
            sql_types.append("text")  # Maps to text in SQL
        elif pd.api.types.is_int64_dtype(dtype) or pd.api.types.is_integer_dtype(dtype):
            sql_types.append("int")   # Maps to integer in SQL
        elif pd.api.types.is_float_dtype(dtype):
            sql_types.append("float")  # Maps to float in SQL
        elif pd.api.types.is_bool_dtype(dtype):
            sql_types.append("boolean")  # Maps to boolean in SQL
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            sql_types.append("timestamp")  # Maps to timestamp in SQL
        else:
            sql_types.append("text")  # Fallback to text for unknown types
    
    return dict(zip(columns, sql_types))

'''
we could've written the conditionals as 
if dtype == "object":
    sql_types.append("text")
The issue with such conditionals is that they directly compare the dtype to a string (e.g., "object"), 
which works in some cases but may not handle all scenarios correctly, particularly for special or more nuanced 
Pandas data types like nullable integers (Int64) or datetime types.

'''

# Generate SQL queries for all CSV files
csv_files = os.listdir(data_dir)
queries = []

for file in csv_files:
    if file.endswith(".csv"):
        print(f"Processing file: {file}")
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)

        table_name = os.path.splitext(file)[0]  # Use filename (without extension) as table name
        column_types = get_sql_column_type(df)
        
        # Create SQL query for table creation with quoted column names
        columns_def = ", ".join([f'"{col}" {col_type}' if col.isnumeric() else f"{col} {col_type}" for col, col_type in column_types.items()])
        create_table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_def});'
        queries.append(create_table_query)

# Save the queries to a text file
with open(output_file, "w") as f:
    for query in queries:
        f.write(query + "\n")

print(f"SQL queries saved to {output_file}")
