from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from skill_extractor import extract_skills, get_experience_years, get_education_level

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_semantic_score(job_description, resume_text):
    embeddings = model.encode([job_description, resume_text])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return float(score)

def get_skill_match(job_description, resume_text):
    job_skills = set(extract_skills(job_description))
    resume_skills = set(extract_skills(resume_text))
    
    if not job_skills:
        return 0, [], []
    
    matched = job_skills.intersection(resume_skills)
    missing = job_skills.difference(resume_skills)
    
    score = len(matched) / len(job_skills)
    return score, list(matched), list(missing)

def get_full_score(job_description, resume_text):
    # Semantic similarity (50% weight)
    semantic = get_semantic_score(job_description, resume_text)
    
    # Skill match (35% weight)
    skill_score, matched_skills, missing_skills = get_skill_match(job_description, resume_text)
    
    # Education score (15% weight)
    edu_score = min(get_education_level(resume_text) / 4, 1.0)
    
    # Final weighted score
    final_score = (semantic * 0.50) + (skill_score * 0.35) + (edu_score * 0.15)
    
    return {
        "final_score": round(final_score * 100, 2),
        "semantic_score": round(semantic * 100, 2),
        "skill_score": round(skill_score * 100, 2),
        "education_score": round(edu_score * 100, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }

def rank_resumes_full(job_description, resume_texts):
    results = []
    for idx, text in enumerate(resume_texts):
        scores = get_full_score(job_description, text)
        scores["idx"] = idx
        results.append(scores)
    
    ranked = sorted(results, key=lambda x: x["final_score"], reverse=True)
    return ranked