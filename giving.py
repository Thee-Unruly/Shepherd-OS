import streamlit as st
from datetime import datetime
import pandas as pd
from utils import load_data, save_data

def main():
    st.title("💰 Giving Tracker")

    members = load_data("members.csv")
    giving = load_data("giving.csv")

    # Form for recording a giving entry
    with st.form("giving_form"):
        giver = st.selectbox("Select Member", members["Name"].tolist())
        amount = st.number_input("Amount Given", min_value=0.0, format="%.2f")
        date = st.date_input("Date", datetime.today())
        submitted = st.form_submit_button("Save")
        if submitted:
            # Append the new entry to the giving records
            giving = pd.concat([
                giving,
                pd.DataFrame([[giver, amount, date]], columns=["Name", "Amount", "Date"])
            ], ignore_index=True)
            save_data(giving, "giving.csv")
            st.success("💸 Giving recorded!")

    # Display the giving records
    st.subheader("🧾 Giving Records")
    st.dataframe(giving)

# Ensure the app runs when this module is executed directly
if __name__ == "__main__":
    main()
