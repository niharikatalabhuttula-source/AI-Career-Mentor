import streamlit as st
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
if uploaded_file:
    st.success("Resume uploaded successfully!")
    st.write("File Name:", uploaded_file.name)
st.sidebar.title("Navigation")
st.sidebar.write("🏠 Home")
st.sidebar.write("📄 Resume Analysis")
st.sidebar.write("📊 ATS Score")
st.sidebar.write("🎯 Skill Gap")
st.sidebar.write("📚 Learning Roadmap")    
