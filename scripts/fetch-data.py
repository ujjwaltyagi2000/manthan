from supabase import create_client
import pandas as pd
import os
# Load environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Initialize Supabase client
supabase = create_client(url, key)

# Fetch data from a Supabase table
def fetch_data(table_name):
    response = supabase.table(table_name).select("*").execute()
    # Check if the response contains an error
    if response.data is not None:
        return pd.DataFrame(response.data)
    else:
        raise Exception(f"Error fetching data: {response.error}")

# Example: Fetch data from 'winning_turnout' table
try:
    df = fetch_data('winning_turnout')

    # Display the first few rows of the dataframe
    print(df.head())

    # EDA Example 1: Summary Statistics
    print(df.describe())

except Exception as e:
    print(f"An error occurred: {e}")
