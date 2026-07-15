import streamlit as st

st.set_page_config(page_title="Student Registration", page_icon=":guardsman:", layout="centered")
st.title("Student Registration Form")

name = st.text_input("Student Name:")
father = st.text_input("Father's Name:")
email = st.text_input("Email:")
mobile = st.text_input("Mobile Number:")
gender = st.radio("Gender:", ["Male", "Female", "Other"])
age = st.number_input("Age:", min_value=18, max_value=50, step=1)
course = st.selectbox("Course:", ["B.Tech", "M.Tech", "PhD","BCA", "MCA", "BBA", "MBA"])
branch = st.selectbox("Branch:", ["CSE", "IT", "ECE", "ME", "CE"])
semester = st.selectbox("Semester:", ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"])
address = st.text_area("Address:")
agree = st.checkbox("I agree to the terms and conditions.")

if st.button("Register"):
    if name == "" or email == "" or mobile == "" or address == "":
        st.error("Please fill in all the required fields.")
    elif not agree:
        st.warning("Please agree to the terms and conditions.")
    else:
        st.success("Student Registration successful!")

        st.header("Student Details:")
        st.write(f"**Name:** {name}")
        st.write(f"**Father's Name:** {father}")
        st.write(f"**Email:** {email}")
        st.write(f"**Mobile Number:** {mobile}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Age:** {age}")
        st.write(f"**Course:** {course}")
        st.write(f"**Branch:** {branch}")
        st.write(f"**Semester:** {semester}")
        st.write(f"**Address:** {address}")
        st.balloons()