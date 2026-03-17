import streamlit as st

st.set_page_config(page_title="Happy Mind", page_icon="🧠", layout="wide")

if "logged_in" not in st.session_state:
    st.switch_page("app.py")

# ---------- STYLE ----------
st.markdown("""
<style>

/* Animated Background */
.stApp{
background: linear-gradient(-45deg,#020617,#0f172a,#1e293b,#020617);
background-size:400% 400%;
animation:gradientBG 12s ease infinite;
}

@keyframes gradientBG{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Title Glow */
.title{
font-size:60px;
font-weight:700;
text-align:center;
color:#e2e8f0;
animation:glow 3s ease-in-out infinite alternate;
}

@keyframes glow{
from{text-shadow:0 0 10px #22c55e;}
to{text-shadow:0 0 30px #22c55e;}
}

/* Section Title */
.section{
font-size:30px;
font-weight:600;
margin-top:20px;
color:#e5e7eb;
}

/* Feature Cards */
.card{
background:#1e293b;
padding:25px;
border-radius:15px;
transition:0.3s;
box-shadow:0px 10px 30px rgba(0,0,0,0.4);
}

.card:hover{
transform:translateY(-8px);
box-shadow:0px 15px 40px rgba(34,197,94,0.4);
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">🌿 Happy Mind</div>', unsafe_allow_html=True)

st.markdown("""
### Your AI Companion for Mental Wellness

Welcome to **Happy Mind**, a digital platform designed to help individuals
understand and improve their emotional and psychological well-being.

Mental health is an essential part of a person's life. In today's fast-paced
environment, students and professionals often experience mental challenges
caused by academic pressure, demanding work schedules, long screen exposure,
and limited rest.

Happy Mind uses **Artificial Intelligence and Machine Learning** to analyze
daily lifestyle patterns and provide insights about possible mental health
risks such as **stress, anxiety, depression, and burnout**.
""")

st.caption("💙 Understand your mind • Improve your lifestyle • Build emotional balance")

st.divider()

# ---------- WHAT SYSTEM ANALYZES ----------
st.markdown('<div class="section">📊 What Happy Mind Analyzes</div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>😴 Sleep Patterns</h3>
    Healthy sleep is essential for emotional regulation,
    cognitive performance, and stress management.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>📱 Screen Time</h3>
    Long hours on digital devices can increase anxiety,
    reduce attention span, and cause mental fatigue.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🏃 Lifestyle Habits</h3>
    Physical activity, social interaction, and daily
    routines strongly influence mental well-being.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------- CONDITIONS ----------
st.markdown('<div class="section">🧠 Mental Health Conditions Evaluated</div>', unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    st.markdown("""
**Stress**

Stress occurs when a person experiences excessive pressure
from academic responsibilities, work demands, or personal
challenges.

**Anxiety**

Anxiety is characterized by persistent worry or nervousness
about future events and uncertainty.
""")

with col2:
    st.markdown("""
**Depression**

Depression involves persistent sadness, loss of motivation,
and decreased interest in daily activities.

**Burnout**

Burnout is a state of emotional and physical exhaustion
caused by prolonged stress.
""")

st.divider()

# ---------- HOW SYSTEM WORKS ----------
st.markdown('<div class="section">⚙️ How Happy Mind Works</div>', unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

col1.info("👤 Step 1\nCreate your personal profile")
col2.info("📊 Step 2\nEnter lifestyle information")
col3.info("🤖 Step 3\nAI analyzes patterns")
col4.info("📄 Step 4\nView mental health insights")

st.divider()

# ---------- WELLNESS TIPS ----------
st.markdown('<div class="section">🌿 Daily Mental Wellness Tips</div>', unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    st.success("✔ Maintain 7–8 hours of sleep")
    st.success("✔ Take regular breaks from screens")
    st.success("✔ Practice mindfulness or meditation")

with col2:
    st.success("✔ Exercise regularly")
    st.success("✔ Maintain social connections")
    st.success("✔ Balance productivity with rest")

st.divider()

st.caption("💡 Mental health awareness helps people identify early warning signs and build healthier lifestyles.")

# ---------- SIDEBAR ----------
st.sidebar.write("Logged in as:")
st.sidebar.success(st.session_state["user_email"])

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")