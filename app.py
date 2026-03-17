import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Mental Health App", layout="wide")

st.title("🔐 Happy Mind Login")

file = "users.csv"

# create users.csv if not exists
if not os.path.exists(file):
    df = pd.DataFrame(columns=["email","password"])
    df.to_csv(file,index=False)

tab1, tab2 = st.tabs(["Login","Sign Up"])

# LOGIN
with tab1:

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        df = pd.read_csv(file)

        user = df[(df["email"] == email) & (df["password"] == password)]

        if not user.empty:

            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email

            st.success("Login Successful")

            st.switch_page("pages/1_Home.py")

        else:
            st.error("Invalid email or password")


# SIGNUP
with tab2:

    new_email = st.text_input("Create Email")
    new_password = st.text_input("Create Password", type="password")

    if st.button("Create Account"):

        df = pd.read_csv(file)

        if new_email in df["email"].values:
            st.warning("Account already exists")

        else:

            new_user = pd.DataFrame({
                "email":[new_email],
                "password":[new_password]
            })

            df = pd.concat([df,new_user],ignore_index=True)
            df.to_csv(file,index=False)

            st.success("Account created successfully")