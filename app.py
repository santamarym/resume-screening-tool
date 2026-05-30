import streamlit as st
import os
import tempfile
from resume_parser import extract_text
from semantic_scorer import rank_resumes_full

st.set_page_config(page_title="Resume Screening Tool", layout="wide")

st.title("🎯 Resume Screening Tool")
st.markdown("AI-powered resume screening with semantic matching and skill extraction.")

# Job Description Input
st.header("Step 1: Enter Job Description")
job_description = st.text_area("Paste the job description here", height=200)

# Resume Upload
st.header("Step 2: Upload Resumes")
uploaded_files = st.file_uploader(
    "Upload PDF or DOCX resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

# Run Screening
if st.button("🔍 Screen Resumes"):
    if not job_description:
        st.error("Please enter a job description!")
    elif not uploaded_files:
        st.error("Please upload at least one resume!")
    else:
        resume_texts = []
        resume_names = []

        with st.spinner("Reading resumes..."):
            for file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp:
                    tmp.write(file.read())
                    tmp_path = tmp.name
                text = extract_text(tmp_path)
                resume_texts.append(text)
                resume_names.append(file.name)
                os.unlink(tmp_path)

        with st.spinner("Analyzing resumes with AI... this may take a moment..."):
            ranked = rank_resumes_full(job_description, resume_texts)

        st.success(f"✅ Screened {len(uploaded_files)} resumes!")
        st.header("🏆 Candidate Rankings")

        for rank, result in enumerate(ranked, start=1):
            idx = result["idx"]
            name = resume_names[idx]
            
            with st.expander(f"#{rank} — {name} — Overall Match: {result['final_score']}%"):
                
                # Score breakdown
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("🧠 Semantic Match", f"{result['semantic_score']}%")
                with col2:
                    st.metric("🛠 Skills Match", f"{result['skill_score']}%")
                with col3:
                    st.metric("🎓 Education", f"{result['education_score']}%")

                st.progress(result["final_score"] / 100)

                # Matched skills
                if result["matched_skills"]:
                    st.success("✅ Matched Skills: " + ", ".join(result["matched_skills"]))
                
                # Missing skills
                if result["missing_skills"]:
                    st.warning("❌ Missing Skills: " + ", ".join(result["missing_skills"]))

                # Resume preview
                st.write("**Resume Preview:**")
                st.write(resume_texts[idx][:500] + "...")