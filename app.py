import streamlit as st
from utils.parser import parse_resume

st.set_page_config(page_title="AI Resume Analyzer")
st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])
job_role = st.text_input("Enter the job role :")

if uploaded_file and job_role:
    if st.button("Analyze"):
        st.info("Processing your resume...")

        resume_text = parse_resume(uploaded_file)
        st.write(resume_text)
        
