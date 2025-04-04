import pandas as pd
import os

def load_data(filename):
    filepath = os.path.join("data", filename)
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        return pd.DataFrame()

def save_data(df, filename):
    filepath = os.path.join("data", filename)
    df.to_csv(filepath, index=False)
