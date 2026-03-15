import streamlit as st

st.set_page_config(
    page_title="AI Mental Health System",
    page_icon="🧠",
    layout="wide"
)

# Title Section
st.title("🧠 AI Mental Health Prediction System")
st.subheader("Understanding Mental Health in the Modern World")

st.divider()

# Introduction Section
st.header("Why Mental Health is Important")

st.write("""
Mental health is a fundamental part of overall well-being. It affects how individuals think,
feel, and behave in everyday life. A healthy mental state helps people manage stress,
maintain relationships, work productively, and make meaningful decisions.

In today's fast-paced digital world, people often focus more on physical health while
ignoring emotional and psychological well-being. However, mental health problems can
develop silently and may not always show clear physical symptoms.
""")

st.divider()

# Two column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Students and Mental Health")
    st.write("""
Students today experience significant academic pressure, competition,
and expectations from family and society. They must balance assignments,
examinations, social relationships, and career planning at the same time.

Excessive screen time, social media comparisons, and reduced physical
activity can increase stress levels. Over time this can lead to anxiety,
lack of motivation, and emotional exhaustion without the student even
realizing what is happening.
""")

with col2:
    st.subheader("Employees and Workplace Stress")
    st.write("""
Employees also face mental challenges due to workload, deadlines,
job insecurity, and the pressure to constantly perform well.

Long working hours and poor work-life balance can gradually affect
a person's emotional health. If stress continues for long periods,
it may result in burnout, reduced productivity, and decreased
job satisfaction.
""")

st.divider()

# Warning section
st.header("⚠️ When Mental Health is Ignored")

st.warning("""
Ignoring mental health problems can have serious consequences.
Continuous stress and emotional pressure may lead to sleep problems,
difficulty concentrating, mood changes, and reduced performance
in both academic and professional life.

In severe cases, untreated mental health conditions can develop
into anxiety disorders, depression, or long-term burnout.
Early awareness and support are extremely important.
""")

st.divider()

# Benefits Section
st.header("Benefits of Maintaining Good Mental Health")

col3, col4, col5 = st.columns(3)

with col3:
    st.success("✔ Better Focus and Productivity")

with col4:
    st.success("✔ Stronger Relationships")

with col5:
    st.success("✔ Improved Quality of Life")

st.write("""
People who take care of their mental health are generally more confident,
emotionally stable, and capable of handling challenges effectively.
Maintaining healthy habits such as proper sleep, physical activity,
and social interaction can significantly improve mental well-being.
""")

st.divider()

# AI system section
st.header("How This AI System Helps")

st.info("""
This AI Mental Health Prediction System analyzes lifestyle factors
such as sleep hours, screen time, study hours, exercise, and social
interaction. Using machine learning models, the system predicts
possible mental health risks and helps users become more aware
of their emotional well-being.

The goal of this system is to promote awareness and encourage
people to take proactive steps toward maintaining a healthier
and more balanced life.
""")

st.divider()

st.caption("Use the sidebar to navigate through Dashboard, Prediction, Education, and Profile sections.")