import streamlit as st
import random

# Test list of names
staff_names = ["Nisha", "Mahidhar", "Purshotham"]

# State to store assignments
if "assignments" not in st.session_state:
    st.session_state.assignments = {}

# Title
st.title("Secret Gift Exchange Test")

# Input for participant's name
participant_name = st.text_input("Enter your name (Nisha, Mahidhar, Purshotham):", "")

# Button to get the assigned name
if st.button("Get Your Assignment"):
    if participant_name not in staff_names:
        st.error("Your name is not on the list. Please contact the organizer.")
    elif participant_name in st.session_state.assignments:
        st.info(f"You have already been assigned: {st.session_state.assignments[participant_name]}")
    else:
        # Create a pool of names excluding the participant's name and already assigned names
        available_names = [
            name for name in staff_names
            if name != participant_name and name not in st.session_state.assignments.values()
        ]
        if not available_names:
            st.error("All names have been assigned. Please contact the organizer.")
        else:
            assigned_name = random.choice(available_names)
            st.session_state.assignments[participant_name] = assigned_name
            st.success(f"You have been assigned: {assigned_name}")

# Show all assignments (only for the organizer; comment this out if not needed)
if st.checkbox("Show all assignments (Organizer Only)"):
    st.write(st.session_state.assignments)
