import streamlit as st
from utils.parser import parse_resume
from utils.llm import analyse_resume

st.set_page_config(
    page_title="AI Resume Analyzer", 
    layout="centered",
    page_icon="📄"
)

st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        padding: 20px 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        height: 50px;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload your resume", 
    type=["pdf", "docx"],
    help="Supported formats: PDF, DOCX"
)

job_role = st.text_area(
    "Enter Job Role",
    placeholder="e.g., 'Senior Software Engineer'",
)

if uploaded_file:
    st.success(f"File uploaded: {uploaded_file.name}")

if uploaded_file and job_role:
    if st.button("Analyze Resume", type="primary"):
        with st.spinner("AI is analyzing your resume..."):
            resume_text = parse_resume(uploaded_file)
            
            if not resume_text or "Error" in resume_text:
                st.error(f"{resume_text}")
            else:
                analysis_result = analyse_resume(resume_text, job_role)
                
                st.markdown("---")
                st.subheader("Analysis Results")
                
                st.markdown(analysis_result)
                
                st.success("Analysis complete!")
