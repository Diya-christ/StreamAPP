import streamlit as st
import pandas as pd

st.title("Employee Feedback System")

# Employee details
emp_id = st.text_input("Enter Employee ID")

name = st.text_input("Enter Employee Name")

department = st.selectbox(
    "Select Department",
    ["HR", "IT", "Finance", "Marketing", "Sales"]
)

rating = st.slider("Workplace Satisfaction", 1, 10)

facilities = st.multiselect(
    "Facilities Used",
    ["Cafeteria", "Transport", "Wi-Fi", "Gym", "Parking"]
)

improvement = st.text_area("Recommend Improvements")

document = st.file_uploader(
    "Upload Supporting Document (Optional)"
)

# Submit button
if st.button("Submit Feedback"):

    st.info("Feedback Submitted Successfully!")

    # Satisfaction Rating
    st.metric("Satisfaction Rating", rating)

    # Create table
    feedback = {
        "Employee ID": [emp_id],
        "Employee Name": [name],
        "Department": [department],
        "Facilities Used": [", ".join(facilities)],
        "Suggestions": [improvement],
        "Document": [document.name if document else "No Document"]
    }

    df = pd.DataFrame(feedback)

    st.write("### Feedback Details")
    st.table(df)