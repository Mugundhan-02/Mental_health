import streamlit as st

st.title("Mental Health Prediction")

sleep = st.slider("Sleep Hours per Day", 0, 12)
study = st.slider("Study Hours per Day", 0, 12)
exercise = st.slider("Exercise Days per Week", 0, 7)
screen = st.slider("Screen Time per Day", 0, 12)
social = st.slider("Social Interaction Level", 0, 10)
pressure = st.slider("Academic Pressure", 0, 10)
time_manage = st.slider("Time Management", 0, 10)

if st.button("Predict Mental Health"):

    # Example logic
    stress_score = pressure*5 + screen*3 - sleep*2
    anxiety_score = pressure*4 + screen*2
    depression_score = (10-social)*5
    burnout_score = study*4 + pressure*3

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

    st.subheader("Mental Health Report")

    st.write("### Stress")
    st.progress(stress_percent/100)
    st.write("Level:", stress_level)
    st.write("Risk Percentage:", stress_percent,"%")

    st.write("Recommendation:")
    st.write("- Improve sleep schedule")
    st.write("- Reduce screen time")
    st.write("- Practice relaxation techniques")

    st.write("---")

    st.write("### Anxiety")
    st.progress(anxiety_percent/100)
    st.write("Level:", anxiety_level)
    st.write("Risk Percentage:", anxiety_percent,"%")

    st.write("Recommendation:")
    st.write("- Deep breathing exercises")
    st.write("- Take breaks during study/work")

    st.write("---")

    st.write("### Depression")
    st.progress(depression_percent/100)
    st.write("Level:", depression_level)
    st.write("Risk Percentage:", depression_percent,"%")

    st.write("Recommendation:")
    st.write("- Increase social interaction")
    st.write("- Engage in physical activities")

    st.write("---")

    st.write("### Burnout")
    st.progress(burnout_percent/100)
    st.write("Level:", burnout_level)
    st.write("Risk Percentage:", burnout_percent,"%")

    st.write("Recommendation:")
    st.write("- Maintain work-life balance")
    st.write("- Take regular breaks")