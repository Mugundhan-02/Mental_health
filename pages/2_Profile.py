import streamlit as st
import pandas as pd
import os

st.title("User Profile")

# Initialize session state
if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""

name = st.text_input("Enter Name", value=st.session_state.name)
age = st.number_input("Age", min_value=10, max_value=80)

gender = st.selectbox("Gender", ["Male","Female","Other"])

email = st.text_input("Email", value=st.session_state.email)

occupation = st.selectbox("Occupation", ["Student","Employee"])

college = st.text_input("College / Workplace")

sleep = st.slider("Sleep Hours", 0, 12)

screen_time = st.slider("Screen Time (hours)", 0, 15)

study_hours = st.slider("Study / Work Hours", 0, 15)

exercise = st.selectbox("Exercise Frequency",
["None","1-2 times/week","3-5 times/week","Daily"])

social = st.selectbox("Social Interaction", ["Low","Medium","High"])


if st.button("Save Profile"):

    if name == "" or email == "":
        st.warning("Please fill Name and Email")
    else:

        # store values
        st.session_state.name = name
        st.session_state.email = email

        data = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Email": email,
            "Occupation": occupation,
            "College": college,
            "Sleep_Hours": sleep,
            "Screen_Time": screen_time,
            "Study_Hours": study_hours,
            "Exercise": exercise,
            "Social_Interaction": social
        }

        df = pd.DataFrame([data])

        file = "user_data.csv"

        if os.path.exists(file):
            df.to_csv(file, mode="a", header=False, index=False)
        else:
            df.to_csv(file, index=False)

        st.success("Profile Saved Successfully")

        st.dataframe(df)