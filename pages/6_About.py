import streamlit as st

st.set_page_config(
    page_title="AI Mental Health System",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Mental Health Prediction System")

st.write("""
Welcome to the AI Mental Health Prediction System.

This application predicts possible mental health conditions
based on lifestyle factors.
""")

st.subheader("How the System Works")

st.write("""
The system analyzes:

• Sleep hours  
• Screen time  
• Study hours  
• Exercise  
• Social interaction  

Then predicts:

• Stress  
• Anxiety  
• Depression  
• Burnout  
""")

st.info("Use the sidebar to navigate to Dashboard, Prediction, Education, Solutions, and Profile pages.")