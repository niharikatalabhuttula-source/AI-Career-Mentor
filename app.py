#creating homepage
import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.education_extractor import extract_education
from utils.project_extractor import extract_projects
from utils.certification_extractor import extract_certifications
from utils.ats_score import calculate_ats_score
from utils.suggestion_generator import generate_suggestions
from utils.role_predictor import predict_roles
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
    education=extract_education(extracted_text)
    projects=extract_projects(extracted_text)
    certifications=extract_certifications(extracted_text)
    ats_score=calculate_ats_score(skills,education,projects,certifications)
    suggestions=generate_suggestions(skills,education,projects,certifications)
    recommended_roles=predict_roles(skills)
    st.subheader("📄Extracted Resume Text") 
    st.text_area("Resume Content",extracted_text,height=400)
    st.subheader("✅ Skills Found")

    if skills:
        for skill in skills:
            st.write(f"• {skill}")
    else:
        st.warning("No skills detected.")
    
    st.divider()

    st.subheader("🎓 Education")

    if education:
        for edu in education:
            st.write(f"• {edu}")
    else:
        st.warning("No education details found.")
    st.divider()

    st.subheader("💻 Projects")

    if projects:
        for project in projects:
            st.write(f"• {project}")
    else:
        st.warning("No project details found.")

    st.divider()

    st.subheader("🏆 Certifications")

    if certifications:
        for certification in certifications:
            st.write(f"• {certification}")
    else:
        st.warning("No certification details found.")
    
    st.divider()
    st.subheader("📊 ATS Score")
    st.write(f"**Score: {ats_score}/100**")

    if ats_score >= 90:
        st.success("🟢 Excellent Resume!")

    elif ats_score >= 70:
        st.info("🟡 Good Resume. A few improvements can make it stronger.")

    elif ats_score >= 50:
        st.warning("🟠 Resume needs improvement.")

    else:
        st.error("🔴 Poor Resume. Add more details and improve your resume.")

    st.divider()


    st.subheader("💡 Resume Improvement Suggestions")

    for suggestion in suggestions:
        st.write(f"• {suggestion}")

    st.divider()

    st.subheader("🎯 Recommended Career Roles")

    if recommended_roles:
        for role in recommended_roles:
            st.write(f"• {role}")
    else:
        st.warning("No suitable career roles found.")
    
