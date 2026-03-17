import streamlit as st

st.set_page_config(page_title="Happy Mind - Education", page_icon="🧠", layout="wide")

if "logged_in" not in st.session_state:
    st.switch_page("app.py")

st.title("🧠 Mental Health Education Center")

st.write("""
The **Happy Mind Education Center** provides detailed information about
common mental health conditions and psychological well-being topics.
Understanding these topics can help individuals recognize early warning
signs and adopt healthier lifestyle habits.

Mental health awareness is an important step toward maintaining emotional
balance, improving productivity, and supporting overall well-being.
""")

st.divider()

topic = st.selectbox(
"📚 Select a Topic to Learn",
[
"Select Topic",
"Stress",
"Anxiety",
"Depression",
"Burnout",
"Sleep & Mental Health",
"Digital Well-Being",
"Emotional Resilience",
"Mindfulness & Relaxation"
]
)

st.divider()

# -------------------------------------------------
# STRESS
# -------------------------------------------------

if topic == "Stress":

    st.header("😰 Stress")

    st.subheader("Overview")

    st.write("""
Stress is the body’s natural response to pressure or challenging
situations. When individuals encounter demanding circumstances,
the brain activates the **fight-or-flight response**, releasing
hormones such as cortisol and adrenaline. These hormones prepare
the body to react quickly to potential threats.

In small amounts, stress can be helpful because it increases
alertness, motivation, and focus. However, when stress becomes
chronic or overwhelming, it can negatively affect both mental
and physical health.
""")

    st.subheader("Common Causes")

    st.write("""
Stress can arise from many aspects of life, including:

- Academic pressure and examinations
- Work deadlines and heavy workload
- Financial difficulties
- Relationship conflicts
- Major life changes
- Lack of sleep or poor lifestyle habits
""")

    st.subheader("Symptoms")

    st.write("""
Stress affects individuals in different ways. Common symptoms include:

- Headaches or muscle tension
- Difficulty concentrating
- Irritability or mood swings
- Sleep disturbances
- Feeling overwhelmed or anxious
""")

    st.subheader("Impact on Health")

    st.write("""
Chronic stress can weaken the immune system, increase the risk
of cardiovascular diseases, and contribute to anxiety disorders
and depression. Long-term stress may also lead to emotional
exhaustion and reduced productivity.
""")

    st.subheader("Management Strategies")

    st.write("""
Stress can be managed through healthy habits such as:

- Regular physical exercise
- Maintaining a consistent sleep schedule
- Practicing mindfulness or meditation
- Taking breaks during work or study
- Seeking emotional support from friends or family
""")

# -------------------------------------------------
# ANXIETY
# -------------------------------------------------

elif topic == "Anxiety":

    st.header("😟 Anxiety")

    st.subheader("Overview")

    st.write("""
Anxiety is characterized by persistent feelings of worry,
nervousness, or fear about future events or uncertain situations.
While occasional anxiety is a normal response to stress,
excessive or prolonged anxiety may interfere with daily life.
""")

    st.subheader("Types of Anxiety")

    st.write("""
Common anxiety disorders include:

- Generalized Anxiety Disorder (GAD)
- Social Anxiety Disorder
- Panic Disorder
- Specific Phobias
""")

    st.subheader("Symptoms")

    st.write("""
Symptoms may include:

- Restlessness
- Rapid heartbeat
- Difficulty sleeping
- Excessive worrying
- Difficulty concentrating
""")

    st.subheader("Causes")

    st.write("""
Anxiety can result from a combination of biological,
psychological, and environmental factors such as
genetics, traumatic experiences, or prolonged stress.
""")

    st.subheader("Management")

    st.write("""
Effective strategies include:

- Deep breathing exercises
- Regular physical activity
- Cognitive behavioral therapy (CBT)
- Limiting caffeine intake
- Developing structured routines
""")

# -------------------------------------------------
# DEPRESSION
# -------------------------------------------------

elif topic == "Depression":

    st.header("😔 Depression")

    st.subheader("Overview")

    st.write("""
Depression is a serious mental health disorder that affects
how a person thinks, feels, and behaves. It is characterized
by persistent sadness and loss of interest in activities.
""")

    st.subheader("Symptoms")

    st.write("""
Common symptoms include:

- Persistent sadness
- Loss of motivation
- Fatigue
- Sleep disturbances
- Feelings of worthlessness
""")

    st.subheader("Causes")

    st.write("""
Depression may be caused by genetic factors, chemical
imbalances in the brain, traumatic experiences, or
chronic stress.
""")

    st.subheader("Treatment")

    st.write("""
Treatment options include:

- Psychotherapy
- Medication prescribed by professionals
- Physical exercise
- Social support
""")

# -------------------------------------------------
# BURNOUT
# -------------------------------------------------

elif topic == "Burnout":

    st.header("🔥 Burnout")

    st.subheader("Overview")

    st.write("""
Burnout is a state of emotional, mental, and physical exhaustion
caused by prolonged stress, especially related to work or academic
responsibilities.
""")

    st.subheader("Symptoms")

    st.write("""
Common signs include:

- Chronic fatigue
- Lack of motivation
- Decreased productivity
- Emotional exhaustion
""")

    st.subheader("Recovery")

    st.write("""
Recovery strategies include:

- Taking regular breaks
- Setting realistic goals
- Maintaining work-life balance
- Engaging in hobbies
""")

# -------------------------------------------------
# SLEEP
# -------------------------------------------------

elif topic == "Sleep & Mental Health":

    st.header("😴 Sleep & Mental Health")

    st.write("""
Sleep is essential for emotional regulation, cognitive
function, and overall mental health.
""")

    st.subheader("Benefits of Quality Sleep")

    st.write("""
- Improves concentration
- Regulates emotions
- Reduces stress
- Supports memory and learning
""")

    st.subheader("Sleep Hygiene Tips")

    st.write("""
- Maintain consistent sleep schedules
- Avoid screens before bedtime
- Create a comfortable sleeping environment
- Limit caffeine intake at night
""")

# -------------------------------------------------
# DIGITAL WELLBEING
# -------------------------------------------------

elif topic == "Digital Well-Being":

    st.header("📱 Digital Well-Being")

    st.write("""
Digital well-being refers to maintaining a healthy relationship
with technology and managing screen time effectively.
""")

    st.subheader("Common Problems")

    st.write("""
- Social media comparison
- Screen addiction
- Sleep disruption
""")

    st.subheader("Healthy Habits")

    st.write("""
- Schedule screen-free time
- Reduce social media usage
- Take digital detox breaks
""")

# -------------------------------------------------
# RESILIENCE
# -------------------------------------------------

elif topic == "Emotional Resilience":

    st.header("🧠 Emotional Resilience")

    st.write("""
Emotional resilience is the ability to adapt to stressful
situations and recover from challenges.
""")

    st.subheader("Ways to Build Resilience")

    st.write("""
- Develop positive thinking habits
- Maintain supportive relationships
- Learn problem-solving skills
""")

# -------------------------------------------------
# MINDFULNESS
# -------------------------------------------------

elif topic == "Mindfulness & Relaxation":

    st.header("🧘 Mindfulness & Relaxation")

    st.write("""
Mindfulness is the practice of focusing attention on the
present moment without judgment.
""")

    st.subheader("Common Techniques")

    st.write("""
- Meditation
- Deep breathing
- Yoga
- Journaling thoughts
""")

st.divider()

st.subheader("💡 Daily Mental Wellness Habits")

col1,col2,col3 = st.columns(3)

col1.success("😴 Maintain healthy sleep")
col2.success("🏃 Exercise regularly")
col3.success("👥 Stay socially connected")

col1.success("🧘 Practice mindfulness")
col2.success("📵 Reduce excessive screen time")
col3.success("📅 Manage time effectively")

# ---------- SIDEBAR ----------

st.sidebar.write("Logged in as:")
st.sidebar.success(st.session_state["user_email"])

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")