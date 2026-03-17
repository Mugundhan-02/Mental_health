import streamlit as st

st.set_page_config(page_title="Happy Mind - Prediction", page_icon="🧠", layout="wide")

if "logged_in" not in st.session_state:
    st.switch_page("app.py")

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#020617,#0f172a,#1e293b);
}
.card{
background:#1e293b;
padding:25px;
border-radius:15px;
box-shadow:0px 8px 25px rgba(0,0,0,0.4);
margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Mental Health Prediction")

st.write("Answer the questions below to analyze possible mental health risks.")

# ---------- INPUTS ----------
col1, col2 = st.columns(2)

with col1:
    sleep_hours = st.slider("Sleep Hours per Day", 0, 12)
    sleep_quality = st.selectbox(
        "Sleep Quality",
        ["Very Poor","Poor","Average","Good","Excellent"]
    )
    study_hours = st.slider("Study / Work Hours per Day", 0, 12)
    exercise_days = st.slider("Exercise Days per Week", 0, 7)
    focus = st.slider("Difficulty Concentrating", 0, 10)

with col2:
    screen_time = st.slider("Screen Time per Day", 0, 12)
    social = st.slider("Social Interaction Level", 0, 10)
    pressure = st.slider("Academic / Work Pressure", 0, 10)
    motivation = st.slider("Motivation Level", 0, 10)
    time_manage = st.slider("Time Management Ability", 0, 10)

support = st.selectbox(
    "Do you feel you have emotional support?",
    ["Yes","Sometimes","No"]
)

# ---------- PREDICTION ----------
if st.button("🔍 Analyze Mental Health"):

    # scoring logic
    stress_score = pressure*5 + screen_time*3 - sleep_hours*2
    anxiety_score = pressure*4 + screen_time*2 + focus*2
    depression_score = (10-social)*4 + (10-motivation)*3
    burnout_score = study_hours*4 + pressure*3 - exercise_days*2

    # sleep quality adjustment
    if sleep_quality in ["Very Poor","Poor"]:
        stress_score += 10
        anxiety_score += 10

    # emotional support adjustment
    if support == "No":
        depression_score += 10

    def get_level(score):
        if score < 30:
            return "Low", 30
        elif score < 60:
            return "Moderate", 60
        else:
            return "High", 90

    stress_level, stress_percent = get_level(stress_score)
    anxiety_level, anxiety_percent = get_level(anxiety_score)
    depression_level, depression_percent = get_level(depression_score)
    burnout_level, burnout_percent = get_level(burnout_score)

    st.subheader("🧠 Mental Health Report")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### Stress")
        st.progress(stress_percent/100)
        st.write("Level:", stress_level)
        st.write("Risk:", stress_percent,"%")
        st.write("Recommendation:")
        st.write("- Improve sleep routine")
        st.write("- Reduce screen time")
        st.write("- Practice relaxation techniques")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### Depression")
        st.progress(depression_percent/100)
        st.write("Level:", depression_level)
        st.write("Risk:", depression_percent,"%")
        st.write("Recommendation:")
        st.write("- Increase social interaction")
        st.write("- Engage in physical activities")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### Anxiety")
        st.progress(anxiety_percent/100)
        st.write("Level:", anxiety_level)
        st.write("Risk:", anxiety_percent,"%")
        st.write("Recommendation:")
        st.write("- Practice breathing exercises")
        st.write("- Take regular breaks")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("### Burnout")
        st.progress(burnout_percent/100)
        st.write("Level:", burnout_level)
        st.write("Risk:", burnout_percent,"%")
        st.write("Recommendation:")
        st.write("- Maintain work-life balance")
        st.write("- Schedule rest and recovery")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.write("Logged in as:")
st.sidebar.success(st.session_state["user_email"])

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")