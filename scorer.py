from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resume_texts):
    documents = [job_description] + resume_texts
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    job_vector = tfidf_matrix[0]
    resume_vectors = tfidf_matrix[1:]
    
    scores = cosine_similarity(job_vector, resume_vectors)[0]
    
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return ranked