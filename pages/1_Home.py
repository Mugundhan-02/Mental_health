import streamlit as st

st.set_page_config(page_title="AI Mental Health System", page_icon="🧠")

st.title("🧠 AI Mental Health Prediction System")

st.write("""
Welcome to the **AI Mental Health Prediction System**.

Mental health plays an important role in maintaining a person's
overall well-being, productivity, and quality of life. Many
students and working professionals experience mental health
challenges due to academic pressure, long working hours,
excessive screen usage, and lack of proper rest.

This application uses **Artificial Intelligence and Machine Learning**
to analyze lifestyle patterns and provide insights about possible
mental health conditions.
""")

st.subheader("📊 What This System Analyzes")

st.write("""
The system evaluates several lifestyle factors that can influence
mental health. These include:

• Sleep hours per day  
• Screen time usage  
• Study or work hours  
• Physical exercise habits  
• Social interaction levels  
• Academic or work pressure  
• Time management ability  

These factors are commonly associated with mental health
conditions and can help identify early warning signs.
""")

st.subheader("🧠 Mental Health Conditions Predicted")

st.write("""
Based on the information provided by the user, the system
predicts the possible level of the following mental health conditions:

• **Stress** – Mental pressure caused by workload or responsibilities  

• **Anxiety** – Excessive worry or nervousness about future situations  

• **Depression** – Persistent sadness and loss of interest in activities  

• **Burnout** – Emotional and physical exhaustion caused by long-term stress  
""")

st.subheader("⚙️ How the System Works")

st.write("""
The application uses a machine learning model trained on
mental health datasets to analyze user lifestyle patterns.

The process works in four simple steps:

1️⃣ Go to the **Profile Page** and enter your basic information  

2️⃣ Navigate to the **Prediction Page** and enter lifestyle details  

3️⃣ Click **Analyze Mental Health** to run the AI prediction  

4️⃣ The system will generate a **Mental Health Report**
showing possible risk levels and recommendations.
""")

st.subheader("💡 Why This System Is Useful")

st.write("""
This application helps individuals become more aware of
their mental health condition. Early awareness can help
people take preventive actions before mental health issues
become severe.

The system also provides helpful recommendations and
educational information so users can learn how to maintain
better mental well-being.
""")

st.success("✅ Use the sidebar to navigate through the different sections of the application.")