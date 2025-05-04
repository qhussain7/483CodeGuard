# CodeGuard: Code Plagiarism Detection System

## Overview
CodeGuard is a machine learning-based system that detects plagiarism in source code. It uses TF-IDF vectorization and supervised learning models (Random Forest, SVM, and Logistic Regression) to identify code similarities. A Flask-based API is provided for testing and deployment.

## Features
- **Preprocessing**: Cleans source code by removing comments and formatting inconsistencies.
- **Feature Extraction**: Uses TF-IDF to convert source code into numerical representations.
- **Machine Learning Models**: Trains multiple classifiers to detect code similarity.
- **Web API**: A Flask-based API to test plagiarism detection.

## Installation
### **1. Clone the Repository**
```bash
cd ~/Desktop  # Navigate to your desired directory
git clone https://github.com/your-repo/codeguard.git
cd codeguard
```
### **2. Install Dependencies**
```bash
pip install flask scikit-learn pandas numpy pickle5
```
### **3. Run Preprocessing & Feature Extraction**
```bash
python3 generate_preprocessed_data.py
python3 generate_code_features.py
```
### **4. Train Models & Evaluate Performance**
```bash
python3 generate_model_performance.py
```
### **5. Start the Flask API**
```bash
python3 flask_app.py
```

## Usage
### **Sending a Request to the API**
Once the Flask app is running, send a request using `curl`:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"code_snippets": ["def add(a, b): return a + b"]}'
```
### **Expected Response:**
```json
{
    "predictions": [0]
}
```
A prediction of `0` means **not similar**, while `1` means **potential plagiarism detected**.

## File Structure
```
📂 483CodeGuard
 ├── flask_app.py              # Flask API for plagiarism detection
 ├── generate_preprocessed_data.py  # Cleans and tokenizes source code
 ├── generate_code_features.py # Extracts TF-IDF features
 ├── generate_model_performance.py  # Trains & evaluates models
 ├── model.pkl                 # Trained Random Forest model
 ├── tfidf_vectorizer.pkl       # TF-IDF vectorizer
 ├── preprocessed_code_data.csv # Cleaned and tokenized data
 ├── code_features.csv          # Extracted TF-IDF features
 ├── model_performance.csv      # Model evaluation results
```

## Authors
- **Qasim Hussain**

## Future Improvements
- Implement deep learning-based similarity detection.
- Add support for additional programming languages.
- Deploy as a web-based plagiarism checker.

## License
MIT License. Feel free to use and modify!

# 483CodeGuard
