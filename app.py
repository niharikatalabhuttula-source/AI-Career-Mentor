#creating homepage
import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 AI Career Mentor")
st.write("Welcome to your personal AI-powered career guidance platform!")
st.divider()
st.header("📄 Upload Your Resume")
uploaded_file = st.file_uploader(
    "Choose a PDF Resume",
    type=["pdf"]
)
st.sidebar.title("Navigation")
st.sidebar.write("🏠 Home")
st.sidebar.write("📄 Resume Analysis")
st.sidebar.write("📊 ATS Score")
st.sidebar.write("🎯 Skill Gap")
st.sidebar.write("📚 Learning Roadmap")   
if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
    st.write("File Name:", uploaded_file.name)
    extracted_text=extract_text_from_pdf(uploaded_file)
    skills =extract_skills(extracted_text)
    st.subheader("📄Extracted Resume Text") 
    st.text_area("Resume Content",extracted_text,height=400)
    st.subheader("✅ Skills Found")

    if skills:
        for skill in skills:
            st.write(f"• {skill}")
    else:
        st.warning("No skills detected.")
