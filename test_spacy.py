import spacy

# Try loading the model
try:
    nlp = spacy.load("en_core_web_sm")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error: {e}")