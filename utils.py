"""utils.py

Helper functions across modules.
"""
import pandas as pd
import os

def save_df_to_csv(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path)

def load_csv_if_exists(path):
    if os.path.exists(path):
        return pd.read_csv(path, parse_dates=['date']).set_index('date')
    return None