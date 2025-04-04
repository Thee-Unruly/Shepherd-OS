import pandas as pd
from pathlib import Path

# Utility function to load data from a CSV file
def load_data(filepath):
    file_path = Path(filepath)
    if file_path.exists() and file_path.stat().st_size > 0:  # Check if the file exists and is not empty
        return pd.read_csv(filepath)
    else:
        # Create an empty DataFrame with the correct columns if the file is empty or doesn't exist
        if filepath == "members.csv":
            columns = ["Name", "Phone", "Email", "Group", "Gender", "Date_of_Birth", "Address", "Username"]
        elif filepath == "attendance.csv":
            columns = ["Name", "Date"]
        else:
            columns = []  # Empty columns if not a recognized file

        # Save an empty DataFrame with columns to the file
        df = pd.DataFrame(columns=columns)
        df.to_csv(filepath, index=False)  # Save the empty DataFrame with columns
        return df

# Utility function to save data to a CSV file
def save_data(dataframe, filepath):
    dataframe.to_csv(filepath, index=False)
