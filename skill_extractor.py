import spacy

nlp = spacy.load("en_core_web_sm")

# Common tech skills list
SKILLS_DB = [
    "python", "java", "javascript", "typescript", "c++", "c#", "ruby", "php",
    "swift", "kotlin", "r", "matlab", "scala", "go", "rust",
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "pytorch", "keras", "scikit-learn", "opencv",
    "pandas", "numpy", "matplotlib", "seaborn", "plotly",
    "sql", "mysql", "postgresql", "mongodb", "redis", "firebase",
    "django", "flask", "fastapi", "react", "nodejs", "html", "css",
    "docker", "kubernetes", "aws", "azure", "gcp", "git", "linux",
    "data science", "data analysis", "big data", "spark", "hadoop",
    "communication", "teamwork", "leadership", "problem solving"
]

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text_lower:
            found_skills.append(skill)
    return list(set(found_skills))

def get_experience_years(text):
    import re
    patterns = [
        r'(\d+)\+?\s*years?\s*of\s*experience',
        r'(\d+)\+?\s*years?\s*experience',
        r'experience\s*of\s*(\d+)\+?\s*years?',
    ]
    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return int(match.group(1))
    return 0

def get_education_level(text):
    text_lower = text.lower()
    if any(word in text_lower for word in ["phd", "doctorate", "ph.d"]):
        return 4
    elif any(word in text_lower for word in ["master", "mtech", "msc", "mba", "m.tech"]):
        return 3
    elif any(word in text_lower for word in ["bachelor", "btech", "bsc", "b.tech", "degree"]):
        return 2
    elif any(word in text_lower for word in ["diploma", "certificate"]):
        return 1
    return 0