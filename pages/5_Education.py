import streamlit as st

st.title("🧠 Mental Health Education Center")

st.write("""
Mental health plays a very important role in a person's overall well-being.
Understanding mental health disorders helps individuals recognize early
symptoms and take preventive actions before the condition becomes severe.

Use the search bar below to learn about different mental health conditions.
""")

st.write("Available topics: Stress, Anxiety, Depression, Burnout")

search = st.text_input("🔎 Search Mental Health Disorder").lower()

st.divider()

# ---------------- STRESS ----------------

if search == "stress":

    st.header("😰 Stress")

    st.write("""
Stress is a natural psychological and physical response that occurs when
people face demanding or challenging situations. In small amounts,
stress can be beneficial because it motivates individuals to complete
tasks and respond effectively to challenges. However, when stress
continues for a long period of time without proper rest or recovery,
it can negatively affect a person's mental and physical health.

Many students and working professionals experience stress due to
academic pressure, deadlines, heavy workload, and expectations from
family or society. Chronic stress can reduce concentration,
affect sleep quality, and lower overall productivity.

Early identification of stress is important because unmanaged stress
can eventually lead to more serious mental health conditions such as
anxiety or depression.
""")

    st.subheader("Early Signs of Stress")

    st.write("""
People experiencing stress may start noticing several early warning
signs such as headaches, fatigue, irritability, and difficulty
concentrating on tasks. Some individuals may also experience sleep
disturbances, mood swings, and a feeling of being overwhelmed.
These symptoms indicate that the body and mind are struggling to
cope with pressure.
""")

    st.subheader("Ways to Manage Stress")

    st.write("""
Stress can be managed through healthy lifestyle habits and
relaxation techniques. Regular physical exercise helps release
endorphins that improve mood and reduce tension. Maintaining
a proper sleep schedule and limiting excessive screen time
also supports mental balance.

Practices such as meditation, deep breathing exercises,
and mindfulness are effective in calming the mind. In addition,
talking with friends, family members, or mentors can provide
emotional support and help individuals handle stressful
situations more effectively.
""")

# ---------------- ANXIETY ----------------

elif search == "anxiety":

    st.header("😟 Anxiety")

    st.write("""
Anxiety is a mental health condition characterized by excessive
worry, fear, or nervousness about future events or uncertain
situations. While occasional anxiety is a normal human response
to stressful situations, persistent and intense anxiety may
interfere with daily life and personal well-being.

People experiencing anxiety may constantly worry about
academic performance, social interactions, career choices,
or personal relationships. This constant worrying can
create mental fatigue and make it difficult for individuals
to relax or focus on important tasks.
""")

    st.subheader("Early Signs of Anxiety")

    st.write("""
Early signs of anxiety include restlessness, difficulty sleeping,
rapid heartbeat, excessive worrying, and difficulty concentrating.
Individuals may also feel constantly tense or nervous even when
there is no immediate danger or problem.

Over time, untreated anxiety can affect academic performance,
work productivity, and relationships with others.
""")

    st.subheader("Ways to Reduce Anxiety")

    st.write("""
Managing anxiety involves adopting calming and supportive
lifestyle practices. Regular physical activity, meditation,
and deep breathing techniques can help regulate emotions
and reduce nervousness.

Limiting caffeine intake, reducing excessive screen exposure,
and maintaining a structured daily routine can also improve
mental stability. In more severe cases, professional guidance
from psychologists or counselors can help individuals develop
coping strategies and manage anxiety effectively.
""")

# ---------------- DEPRESSION ----------------

elif search == "depression":

    st.header("😔 Depression")

    st.write("""
Depression is a serious mental health disorder that affects
how a person thinks, feels, and behaves. It is characterized
by persistent feelings of sadness, hopelessness, and loss of
interest in activities that were once enjoyable.

Unlike temporary sadness that everyone experiences from time
to time, depression can last for weeks or months and may
significantly impact daily life. Students and professionals
experiencing depression may struggle with concentration,
motivation, and maintaining relationships.
""")

    st.subheader("Early Signs of Depression")

    st.write("""
Common early symptoms of depression include prolonged sadness,
lack of motivation, fatigue, difficulty sleeping or oversleeping,
changes in appetite, and loss of interest in hobbies or social
activities. Individuals may also experience feelings of worthlessness
or low self-esteem.

Recognizing these early signs is important because early
intervention can prevent the condition from becoming more severe.
""")

    st.subheader("Ways to Cope with Depression")

    st.write("""
Coping with depression often requires a combination of healthy
lifestyle habits and emotional support. Engaging in regular
physical activity, maintaining a structured daily routine,
and staying socially connected can significantly improve mood.

Spending time with supportive friends or family members helps
reduce feelings of isolation. In more serious cases, seeking
professional mental health support from therapists or counselors
is strongly recommended.
""")

# ---------------- BURNOUT ----------------

elif search == "burnout":

    st.header("🔥 Burnout")

    st.write("""
Burnout is a state of emotional, mental, and physical exhaustion
caused by prolonged stress, especially related to work or academic
responsibilities. It often occurs when individuals feel overwhelmed
by continuous pressure and lack adequate rest or relaxation.

Students preparing for exams or professionals working long hours
may experience burnout when they push themselves beyond their
mental and physical limits for extended periods of time.
""")

    st.subheader("Early Signs of Burnout")

    st.write("""
Early symptoms of burnout include constant fatigue, reduced
motivation, decreased productivity, and feelings of frustration
or detachment from work or studies. Individuals may also feel
emotionally drained and unable to meet daily demands.
""")

    st.subheader("Ways to Recover from Burnout")

    st.write("""
Recovering from burnout requires restoring balance between
work and personal life. Taking regular breaks, practicing
time management, and setting realistic goals can reduce
excessive workload pressure.

Engaging in hobbies, spending time outdoors, and maintaining
a healthy sleep schedule can also help the mind recover
from prolonged stress and improve overall well-being.
""")

elif search != "":
    st.warning("Topic not found. Try: Stress, Anxiety, Depression, Burnout")