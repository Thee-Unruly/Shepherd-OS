import streamlit as st
import pandas as pd
from utils import load_data, save_data

def main():
    st.title("📋 Onboarding - Complete Your Profile")

    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.error("You must be logged in to complete onboarding.")
        return

    members = load_data("members.csv")
    
    # Ensure that the logged-in user has not completed onboarding yet
    if "onboarding" in st.session_state and st.session_state.onboarding:
        st.write("Please fill out your personal details.")
        name = st.text_input("Full Name")
        phone = st.text_input("Phone")
        group = st.selectbox("Ministry Group", ["Youth", "Worship", "Ushering", "None"])

        if st.button("Save Profile"):
            new_member = pd.DataFrame([[name, phone, group]], columns=["Name", "Phone", "Group"])
            members = pd.concat([members, new_member], ignore_index=True)
            save_data(members, "members.csv")
            st.session_state.onboarding = False  # Mark onboarding as complete
            st.success("🎉 Onboarding complete! Redirecting to main application.")
            st.rerun()  # Redirect to the main application
    else:
        st.write("You have already completed onboarding!")

if __name__ == "__main__":
    main()
