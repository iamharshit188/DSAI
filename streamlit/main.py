import streamlit as st

def main():
    st.title("Login Form")
    
    with st.form("login_form"):
        username = st.text_input("Username:", key="username_input")
        password = st.text_input("Password:", type="password", key="password_input")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            if username and password:
                st.success(f"Welcome, {username}!")
            else:
                st.error("Please enter both username and password.")

if __name__ == "__main__":
    main()
    