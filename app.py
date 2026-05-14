import streamlit as st
from utils import recommend_colleges, recommend_scholarships

st.set_page_config(page_title="College Admission Assistant", layout="wide")

st.title("🎓 College Admission Assistant")
st.write("Find suitable colleges and scholarships based on your profile.")

name = st.text_input("Your Name")

marks = st.number_input(
    "Class 12 Percentage",
    min_value=0.0,
    max_value=100.0,
    step=0.1
)

course = st.selectbox(
    "Preferred Course",
    ["B.Tech", "BCA", "BBA", "BA", "BSc"]
)

city = st.text_input("Preferred City / State")

budget = st.number_input(
    "Maximum Annual Budget (INR)",
    min_value=0
)

college_type = st.selectbox(
    "College Preference",
    ["Any", "Government", "Private"]
)

if st.button("Find Colleges"):
    college_results = recommend_colleges(
        course,
        marks,
        city,
        budget,
        college_type
    )

    scholarship_results = recommend_scholarships(marks)

    st.subheader("🏫 Recommended Colleges")

    if college_results.empty:
        st.warning("No matching colleges found.")
    else:
        st.dataframe(college_results)

    st.subheader("💰 Scholarship Suggestions")

    if scholarship_results.empty:
        st.warning("No scholarships found.")
    else:
        st.dataframe(scholarship_results)