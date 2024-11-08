from supabase import create_client
import pandas as pd
import os

# Load environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Initialize Supabase client
supabase = create_client(url, key)

def fetch_data(table_name):
# Fetch all rows from a Supabase table and return them as a DataFrame.
    all_data = []
    limit = 1000  # Supabase default limit
    offset = 0  # Start from the first row

    while True:
        # Fetch data using range for pagination
        response = supabase.table(table_name).select("*").range(offset, offset + limit - 1).execute()

        if response.data:
            all_data.extend(response.data)
            offset += limit
        else:
            # Stop if no more data is available
            break

    if all_data:
        return pd.DataFrame(all_data)
    else:
        raise Exception(f"Error fetching data: {response.error}")
