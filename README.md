# 🎯 Resume Screening Tool

An AI-powered resume screening tool that automatically ranks candidates based on a job description using semantic matching and NLP.

## Features
- Upload multiple PDF/DOCX resumes
- Semantic similarity matching using Sentence Transformers
- Skill extraction using spaCy NLP
- Score breakdown — Skills, Semantic, Education
- Shows matched and missing skills for each candidate
- Clean web UI built with Streamlit

##  Tech Stack
- Python
- Streamlit
- Sentence Transformers (all-MiniLM-L6-v2)
- spaCy
- scikit-learn
- pdfplumber
- python-docx

##  How to Run

### 1. Clone the repository
git clone https://github.com/yourusername/resume-screening-tool.git
cd resume-screening-tool

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

### 4. Run the app
streamlit run app.py

##  How it Works
1. Paste a job description
2. Upload candidate resumes (PDF or DOCX)
3. Click Screen Resumes
4. Get ranked candidates with detailed score breakdown

##  Project Structure
resume-screening-tool/
├── app.py                 # Main Streamlit app
├── resume_parser.py       # PDF/DOCX text extraction
├── semantic_scorer.py     # AI scoring and ranking
├── skill_extractor.py     # Skill extraction using spaCy
├── requirements.txt       # Dependencies
└── sample_resumes/        # Sample resumes for testing