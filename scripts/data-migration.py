from supabase import create_client
from dotenv import load_dotenv
load_dotenv()

import pandas as pd
import os

# directory containing csv files
data_dir = "../data/processed"

# supabase credentials
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# initialising client object
supabase = create_client(url, key)

# function to read data types of columns:
def get_sql_column_type(df):
    columns = df.columns
    types = df.dtypes
    # sql_types = []

    # for dtype in types:
    #     if pd.api.types.is_object_dtype(dtype):  # For text columns
    #         sql_types.append("text")
    #     elif pd.api.types.is_integer_dtype(dtype):  # For integer columns
    #         sql_types.append("integer")
    #     elif pd.api.types.is_float_dtype(dtype):  # For float columns
    #         sql_types.append("float")
    #     elif pd.api.types.is_bool_dtype(dtype):  # For boolean columns
    #         sql_types.append("boolean")
    #     elif pd.api.types.is_datetime64_any_dtype(dtype):  # For datetime columns
    #         sql_types.append("timestamp")
    #     else:
    #         sql_types.append("text")  # Default to text for any unknown type

    return dict(zip(columns, types))
# # function to upload csv files to supabase
# def upload_csv_to_supabase(file_path, table_name):
#     df = pd.read_csv(file_path)
#     create_table_query = {
#         "name": table_name,
#         "columns": [
#             {"name": col, "type": "text"} for col in df.columns  # Adjust type as needed
#         ] # json object
#     }

#     # using supabase's REST API to create the table

#     response = supabase.table(table_name).create(create_table_query).execute

# reading csv files
csv_files = os.listdir(data_dir)

for file in csv_files:
    if file.endswith(".csv"):
        print(file)
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        print(get_sql_column_type(df))
        # upload_csv_to_supabase(file_path, file)
