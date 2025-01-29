import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("data.csv")

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['resume_text'] + " " + data['job_description'])
y = [1] * len(data)  # Dummy labels for training

# Train a simple classifier
model = LogisticRegression()
model.fit(X, y)

# Save the model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model trained and saved!")