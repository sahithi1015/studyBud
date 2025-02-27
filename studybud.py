import streamlit as st

st.set_page_config(page_title="Study Bud", layout="wide")

# User login
if 'user' not in st.session_state:
    st.session_state['user'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'Dashboard'

st.title("Study Bud")

if st.session_state['user'] is None or st.session_state['user'] == "":
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if username and password:  # Simple check for non-empty credentials
            st.session_state['user'] = username
            st.success(f"Welcome, {username}!")
            st.experimental_rerun()
        else:
            st.error("Please enter both username and password")
else:
    st.sidebar.title("Navigation")
    st.session_state['page'] = st.sidebar.radio("Go to", ["Dashboard", "Subjects", "Timetable", "Tasks", "Progress", "Notes", "Premium", "Recommendations", "Gamification", "Chatbot"])

    if st.session_state['page'] == "Dashboard":
        st.header("Dashboard")
        st.write(f"Welcome to the STUDY BUD, {st.session_state['user']}!")

    elif st.session_state['page'] == "Subjects":
        st.header("Subjects")
        num_subjects = st.number_input("Enter the number of subjects:", min_value=1, step=1)
        time_limit = st.number_input("Enter the total time available (in hours):", min_value=1, step=1)

        if st.button("Provide Schedule"):
            if num_subjects > 0 and time_limit > 0:
                time_per_subject = time_limit / num_subjects
                st.session_state['schedule'] = [(f"Subject {i+1}", round(time_per_subject, 2)) for i in range(num_subjects)]
                st.session_state['page'] = 'Timetable'
                st.experimental_rerun()

    elif st.session_state['page'] == "Timetable":
        st.header("Timetable")
        if 'schedule' in st.session_state:
            st.write("Here is your study schedule:")
            for subject, time in st.session_state['schedule']:
                st.write(f"{subject}: {time} hours")
        else:
            st.write("No schedule available. Please generate one from the Subjects page.")

    elif st.session_state['page'] == "Tasks":
        st.header("Tasks")
        task = st.text_input("Add a new task:")
        if st.button("Add Task"):
            st.write(f"Task added: {task}")

    elif st.session_state['page'] == "Progress":
        st.header("Progress Tracking")
        progress = st.slider("Track your practice progress:", 0, 100, 0)
        st.write(f"Your current progress: {progress}%")

    elif st.session_state['page'] == "Notes":
        st.header("Notes")
        uploaded_file = st.file_uploader("Upload your notes:")
        if uploaded_file is not None:
            st.write(f"File uploaded: {uploaded_file.name}")

    elif st.session_state['page'] == "Premium":
        st.header("Premium Model")
        st.write("Upgrade to premium for personalized mentor assistance!")
        st.write("Cost: $9.99/month")

    elif st.session_state['page'] == "Recommendations":
        st.header("Recommendations")
        st.write("Recommended Books and Resources:")
        st.write("- 'Atomic Habits' by James Clear")
        st.write("- 'Deep Work' by Cal Newport")
        st.write("- Coursera: Learning How to Learn")

    elif st.session_state['page'] == "Gamification":
        st.header("Gamification")
        st.write("Take a quick quiz and earn badges!")
        question = st.radio("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"])
        if st.button("Submit Answer"):
            if question == "Paris":
                st.write("Correct! You've earned a badge!")
            else:
                st.write("Try again!")

    elif st.session_state['page'] == "Chatbot":
        st.header("Study Bud AI Chatbot")
        user_input = st.text_input("Chat with our AI mentor:")
        if user_input:
            st.write(f"AI Response: (Pretend AI response for now) {user_input}")

    if st.sidebar.button("Logout"):
        st.session_state['user'] = None
        st.session_state['page'] = 'Dashboard'
        st.experimental_rerun()
