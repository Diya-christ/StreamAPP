import streamlit as st
import pandas as pd

st.title("Student Registration Portal")

# Student details
name = st.text_input("Enter Student Name")

age = st.number_input("Enter Age", 1, 100)

gender = st.radio("Select Gender", ["Male", "Female", "Other"])

department = st.selectbox("Select Department",
                          ["BCA", "BSc", "BCom", "BBA", "MCA"])

subjects = st.multiselect("Choose Subjects",
                          ["Python", "Java", "DBMS", "Web Development", "Data Science"])

date = st.date_input("Date of Admission")

photo = st.file_uploader("Upload Profile Photo", type=["jpg", "png", "jpeg"])

# Register button
if st.button("Register"):

    st.success("Student Registered Successfully!")

    if photo:
        st.image(photo, caption="Profile Photo", width=150)

    student = {
        "Name": [name],
        "Age": [age],
        "Gender": [gender],
        "Department": [department],
        "Subjects": [", ".join(subjects)],
        "Admission Date": [date]
    }

    df = pd.DataFrame(student)

    st.write("### Student Details")
    st.table(df)