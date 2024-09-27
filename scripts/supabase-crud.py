from supabase import create_client
from dotenv import load_dotenv
load_dotenv() 

from datetime import datetime, timedelta
import pandas as pd
import os


url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# print(url)

# Read Write operations -->

# READ
response = supabase.table("test_table").select("*").execute()

# response = supabase.table("test_table").select("*").eq("name", "Anshuman Pandey").execute()

# WRITE 
# data = supabase.table("test_table").insert({"name": "Siddhant Jha"}).execute()

# created_at = datetime.utcnow() - timedelta(hours=2)
# data = supabase.table("test_table").insert({"name": "Arnab Sharma", "created_at" : str(created_at)}).execute()

# UPDATE
# response = (
#     supabase.table("test_table")
#     .update({"name": "Tanishq Sharma"})
#     .eq("id", 7)
#     .execute()
# )

response = supabase.table("test_table").select("*").execute()
print(response)