import streamlit as st
import pickle
import bcrypt
import pandas as pd
from pathlib import Path

# Load passwords
def load_passwords():
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    if file_path.exists():
        with file_path.open("rb") as file:
            names, usernames, hashed_passwords = pickle.load(file)
    else:
        names, usernames, hashed_passwords = [], [], []
    return names, usernames, hashed_passwords

# Save passwords
def save_passwords(names, usernames, hashed_passwords):
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("wb") as file:
        pickle.dump((names, usernames, hashed_passwords), file)

# Save user data
def save_member_data(member_data):
    members = load_data("members.csv")
    members = pd.concat([members, member_data], ignore_index=True)
    save_data(members, "members.csv")

# Load data
def load_data(filepath):
    file_path = Path(filepath)
    if file_path.exists() and file_path.stat().st_size > 0:
        return pd.read_csv(filepath)
    else:
        columns = ["Name", "Phone", "Email", "Group", "Gender", "Date_of_Birth", "Address", "Username"]
        df = pd.DataFrame(columns=columns)
        df.to_csv(filepath, index=False)
        return df

# Save to CSV
def save_data(dataframe, filepath):
    dataframe.to_csv(filepath, index=False)

# -----------------------
# MAIN LOGIC
# -----------------------
def main():
    st.markdown("<h1 style='text-align: center;'>📖 SHEPHERD OS Login/Signup</h1>", unsafe_allow_html=True)

    # Initialize session
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "onboarding" not in st.session_state:
        st.session_state.onboarding = False

    # 1. If onboarding is active
    if st.session_state.onboarding:
        st.subheader("📝 Onboarding - Personal Information")
        with st.form("onboarding_form"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number")
            email = st.text_input("Email Address")
            group = st.selectbox("Ministry Group", ["Hospitality", "Worship", "Ushering", "Media", "Sound", "Creatives"])
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            dob = st.date_input("Date of Birth")
            address = st.text_area("Address")
            submit = st.form_submit_button("Complete Onboarding")

            if submit:
                new_member = pd.DataFrame([[name, phone, email, group, gender, dob, address, st.session_state.username]],
                                          columns=["Name", "Phone", "Email", "Group", "Gender", "Date_of_Birth", "Address", "Username"])
                save_member_data(new_member)
                st.success("✅ Onboarding Complete! Welcome to the platform.")
                st.session_state.logged_in = True
                st.session_state.onboarding = False
                st.rerun()
        return

    # 2. If user already logged in (reroute)
    if st.session_state.logged_in:
        st.experimental_rerun()

    # 3. Normal login/signup flow
    names, usernames, hashed_passwords = load_passwords()
    option = st.selectbox("Choose an option", ["Login", "Signup"])

    if option == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in usernames:
                idx = usernames.index(username)
                if bcrypt.checkpw(password.encode(), hashed_passwords[idx].encode()):
                    st.session_state.logged_in = True
                    st.experimental_rerun()
                else:
                    st.error("Incorrect password")
            else:
                st.error("Username not found")

    elif option == "Signup":
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Signup"):
            if new_username in usernames:
                st.error("Username already exists")
            else:
                hashed_pw = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
                names.append(new_username)
                usernames.append(new_username)
                hashed_passwords.append(hashed_pw.decode())
                save_passwords(names, usernames, hashed_passwords)

                st.success("Signup successful! Redirecting to onboarding...")

                # Set onboarding and username
                st.session_state.onboarding = True
                st.session_state.username = new_username
                st.rerun()

if __name__ == "__main__":
    main()
