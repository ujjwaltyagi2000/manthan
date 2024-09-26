import os
import pandas as pd

# Directory containing CSV files
data_folder = '../data/processed'

# function to rename columns  
def rename_columns(df):
    new_columns = [col.lower().replace(' ', '_').replace('(%)', 'pct') for col in df.columns] # list comprehension
    df.columns = new_columns
    return df

for file in os.listdir(data_folder):
    if file.endswith('.csv'):
        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path)
        df = rename_columns(df)
        df.to_csv(file_path, index=False)

