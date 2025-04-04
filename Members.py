import streamlit as st
import pandas as pd
from utils import load_data, save_data

def main():
    st.title("📋 Members")
    members = load_data("members.csv")

    # Form to add a new member
    with st.form("add_member"):
        name = st.text_input("Full Name")
        phone = st.text_input("Phone")
        group = st.selectbox("Ministry Group", ["Youth", "Worship", "Ushering", "None"])
        submitted = st.form_submit_button("Add Member")
        if submitted and name:
            # Add the new member to the members list
            new_member = pd.DataFrame([[name, phone, group]], columns=["Name", "Phone", "Group"])
            members = pd.concat([members, new_member], ignore_index=True)
            save_data(members, "members.csv")
            st.success("✅ Member added!")

    # Display the members list
    st.subheader("👥 Members List")
    st.dataframe(members)

# Ensure the app runs when this module is executed directly
if __name__ == "__main__":
    main()
