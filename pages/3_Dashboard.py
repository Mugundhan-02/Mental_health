import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Happy Mind - Dashboard", page_icon="🧠", layout="wide")

if "logged_in" not in st.session_state:
    st.switch_page("app.py")

user_email = st.session_state["user_email"]
file = "user_data.csv"

st.title("🧠 Happy Mind Dashboard")

# ---------- LOAD DATA ----------
if os.path.exists(file):
    df = pd.read_csv(file)
    user_data = df[df["Email"] == user_email]
else:
    user_data = pd.DataFrame()

# ---------- IF PROFILE NOT COMPLETED ----------
if user_data.empty:

    st.warning("Please complete your profile first")

    if st.button("Go to Profile"):
        st.switch_page("pages/2_Profile.py")

# ---------- DASHBOARD ----------
else:

    user = user_data.iloc[0]

    st.success(f"Welcome {user['Name']} 🌿")

    # ---------- METRICS ----------
    col1, col2, col3 = st.columns(3)

    col1.metric("😴 Sleep Hours", user["Sleep_Hours"])
    col2.metric("📱 Screen Time", user["Screen_Time"])
    col3.metric("📚 Work / Study Hours", user["Study_Hours"])

    st.divider()

    # ---------- BAR CHART ----------
    st.subheader("📊 Lifestyle Activity")

    lifestyle = pd.DataFrame({
        "Activity": ["Sleep","Screen Time","Study / Work"],
        "Hours": [
            user["Sleep_Hours"],
            user["Screen_Time"],
            user["Study_Hours"]
        ]
    })

    st.bar_chart(lifestyle.set_index("Activity"))

    # ---------- PIE CHART ----------
    st.subheader("🥧 Mental Wellness Indicators")

    labels = ["Exercise","Social Interaction","Stress"]

    values = [
        1 if user["Exercise"] != "None" else 0.5,
        {"Low":1,"Medium":2,"High":3}[user["Social_Interaction"]],
        {"Low":1,"Moderate":2,"High":3}[user["Stress_Level"]]
    ]

    fig, ax = plt.subplots(figsize=(4,4))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.0f%%"
    )

    ax.set_title("Lifestyle Balance")

    col1,col2,col3 = st.columns([1,2,1])

    with col2:
        st.pyplot(fig)

    # ---------- WELLNESS SCORE ----------
    st.subheader("🧠 Mental Wellness Score")

    score = 100

    if user["Sleep_Hours"] < 6:
        score -= 20

    if user["Screen_Time"] > 8:
        score -= 20

    if user["Stress_Level"] == "High":
        score -= 25

    if user["Exercise"] == "None":
        score -= 15

    st.progress(score/100)

    st.write(f"Your wellness score: **{score}/100**")

    if score >= 75:
        st.success("Your mental wellness looks healthy 👍")

    elif score >= 50:
        st.warning("Some lifestyle improvements may help")

    else:
        st.error("High stress risk detected")

# ---------- SIDEBAR ----------
st.sidebar.write("Logged in as:")
st.sidebar.success(user_email)

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")