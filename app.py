from flask import Flask, request, jsonify
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract keywords
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    return keywords

# Function to calculate ATS score
def calculate_ats_score(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0] * 100

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    resume_file = request.files.get('resume')
    job_description = request.form.get('job_description')

    # Extract text from resume PDF
    resume_text = extract_text_from_pdf(resume_file)

    # Calculate ATS score
    ats_score = calculate_ats_score(resume_text, job_description)

    # Extract keywords
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)

    # Find missing keywords
    missing_keywords = set(job_keywords) - set(resume_keywords)

    return jsonify({
        "ats_score": round(ats_score, 2),
        "missing_keywords": list(missing_keywords),
        "suggestions": f"Add these keywords to your resume: {', '.join(missing_keywords)}"
    })

if __name__ == '__main__':
    app.run(debug=True)