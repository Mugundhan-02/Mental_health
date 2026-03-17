import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Happy Mind - Profile", page_icon="🧠", layout="wide")

if "logged_in" not in st.session_state:
    st.switch_page("app.py")

user_email = st.session_state["user_email"]
file = "user_data.csv"

# ---------- MODERN STYLE ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#020617,#0f172a,#1e293b);
}

/* Title */
.title{
font-size:48px;
font-weight:700;
color:#e2e8f0;
margin-bottom:10px;
}

/* Profile header card */
.profile-header{
background:#1e293b;
padding:30px;
border-radius:20px;
box-shadow:0px 10px 30px rgba(0,0,0,0.5);
margin-bottom:25px;
}

/* Info cards */
.card{
background:#1e293b;
padding:25px;
border-radius:15px;
box-shadow:0px 8px 25px rgba(0,0,0,0.4);
margin-bottom:20px;
}

/* Section title */
.section-title{
font-size:22px;
font-weight:600;
color:#e5e7eb;
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌿 Happy Mind Profile</div>', unsafe_allow_html=True)

# ---------- LOAD USER DATA ----------
if os.path.exists(file):
    df = pd.read_csv(file)
    user_data = df[df["Email"] == user_email]
else:
    user_data = pd.DataFrame()

# ---------- PROFILE VIEW ----------
if not user_data.empty:

    user = user_data.iloc[0]

    st.markdown(f"""
    <div class="profile-header">
        <h2>👤 {user['Name']}</h2>
        <p>Age: {user['Age']} | {user['Gender']}</p>
        <p>{user['Occupation']} | {user['City']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Lifestyle Overview</div>', unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric("😴 Sleep Hours", user["Sleep_Hours"])

    with col2:
        st.metric("📱 Screen Time", user["Screen_Time"])

    with col3:
        st.metric("📚 Study/Work Hours", user["Study_Hours"])

    st.markdown('<div class="section-title">Wellness Factors</div>', unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="card">
        <b>🏃 Exercise</b><br>{user['Exercise']}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card">
        <b>😊 Mood</b><br>{user['Mood']}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
        <b>⚡ Stress Level</b><br>{user['Stress_Level']}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="card">
        <b>👥 Social Interaction</b><br>{user['Social_Interaction']}
        </div>
        """, unsafe_allow_html=True)

# ---------- FIRST TIME PROFILE ----------
else:

    st.info("Complete your profile to personalize your Happy Mind experience.")

    st.markdown("### Personal Information")

    col1,col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")
        age = st.number_input("Age",10,80)
        gender = st.selectbox("Gender",["Male","Female","Other"])
        city = st.text_input("City")

    with col2:
        occupation = st.selectbox("Occupation",["Student","Employee"])
        education = st.selectbox("Education",
        ["High School","Undergraduate","Postgraduate","Other"])
        relationship = st.selectbox("Relationship Status",
        ["Single","In a Relationship","Married","Prefer not to say"])

    st.markdown("### Lifestyle Habits")

    col1,col2,col3 = st.columns(3)

    with col1:
        sleep = st.slider("Sleep Hours",0,12)

    with col2:
        screen_time = st.slider("Screen Time",0,12)

    with col3:
        study_hours = st.slider("Study / Work Hours",0,12)

    exercise = st.selectbox("Exercise Frequency",
    ["None","1-2 times/week","3-5 times/week","Daily"])

    st.markdown("### Mental Well-Being")

    col1,col2,col3 = st.columns(3)

    with col1:
        mood = st.selectbox("Mood",["Happy","Neutral","Stressed","Sad"])

    with col2:
        stress = st.selectbox("Stress Level",["Low","Moderate","High"])

    with col3:
        social = st.selectbox("Social Interaction",["Low","Medium","High"])

    support = st.selectbox("Emotional Support",["Yes","Sometimes","No"])

    if st.button("💾 Save Profile"):

        data = {
            "Name":name,
            "Age":age,
            "Gender":gender,
            "Email":user_email,
            "Occupation":occupation,
            "Education":education,
            "City":city,
            "Relationship":relationship,
            "Sleep_Hours":sleep,
            "Screen_Time":screen_time,
            "Study_Hours":study_hours,
            "Exercise":exercise,
            "Mood":mood,
            "Stress_Level":stress,
            "Social_Interaction":social,
            "Support":support
        }

        new_df = pd.DataFrame([data])

        if os.path.exists(file):
            new_df.to_csv(file,mode="a",header=False,index=False)
        else:
            new_df.to_csv(file,index=False)

        st.success("Profile saved successfully")
        st.rerun()

# ---------- SIDEBAR ----------
st.sidebar.write("Logged in as:")
st.sidebar.success(user_email)

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")