import streamlit as st
from auth import register_user, login_user

st.title("Login System")

menu = ["Register", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if choice == "Register":
    if st.button("Register"):
        result = register_user(username, password)
        st.success(result)

elif choice == "Login":
    if st.button("Login"):
        result = login_user(username, password)
        st.success(result)
