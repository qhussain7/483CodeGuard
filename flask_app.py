from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load TF-IDF vectorizer
with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json.get("code_snippets", [])
    
    if not data:
        return jsonify({"error": "No code snippets provided"}), 400
    
    # Transform input code using TF-IDF vectorizer
    transformed_data = tfidf_vectorizer.transform(data)
    
    # Make predictions
    predictions = model.predict(transformed_data)
    
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
