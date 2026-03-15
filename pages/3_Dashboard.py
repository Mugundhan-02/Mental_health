import streamlit as st
import pandas as pd
import os

st.title("My Mental Health Dashboard")

file = "user_data.csv"

email = st.text_input("Enter your Email to view dashboard")

if st.button("Show My Dashboard"):

    if os.path.exists(file):

        df = pd.read_csv(file)

        user = df[df["Email"] == email]

        if not user.empty:

            st.subheader("Your Profile")
            st.dataframe(user)

            sleep = user["Sleep_Hours"].values[0]
            screen = user["Screen_Time"].values[0]
            study = user["Study_Hours"].values[0]

            chart_data = pd.DataFrame({
                "Category":["Sleep","Screen Time","Study/Work"],
                "Hours":[sleep,screen,study]
            })

            st.subheader("Daily Activity Overview")
            st.bar_chart(chart_data.set_index("Category"))

            st.subheader("Exercise Level")
            st.write(user["Exercise"].values[0])

            st.subheader("Social Interaction")
            st.write(user["Social_Interaction"].values[0])

        else:
            st.error("User not found. Please check your email.")

    else:
        st.warning("No data available yet.")