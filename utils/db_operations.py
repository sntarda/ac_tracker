import pandas as pd

# Function to load units from a CSV file
def load_units(file_path):
    return pd.read_csv(file_path)

# Function to save units to a CSV file
def save_units(file_path, units_df):
    units_df.to_csv(file_path, index=False)

