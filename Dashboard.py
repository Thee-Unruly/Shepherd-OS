import streamlit as st
from utils import load_data

def main():
    st.title("📊 Church Dashboard")

    members = load_data("members.csv")
    attendance = load_data("attendance.csv")
    giving = load_data("giving.csv")

    st.metric("👥 Total Members", len(members))
    st.metric("🕊️ Total Attendance", len(attendance))
    st.metric("💸 Total Giving", f"KES {giving['Amount'].sum():,.2f}")

# Ensure the app runs when this module is executed directly
if __name__ == "__main__":
    main()
