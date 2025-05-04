import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load preprocessed dataset
df = pd.read_csv("preprocessed_code_data.csv")

# Handle missing AST entries
df["ast"] = df["ast"].fillna("")

# Combine cleaned code and AST representations for feature extraction
df["combined_text"] = df["cleaned_code"] + " " + df["ast"]

# Train TF-IDF vectorizer on dataset
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
tfidf_features = tfidf_vectorizer.fit_transform(df["combined_text"]).toarray()

# Convert to DataFrame and save
feature_df = pd.DataFrame(tfidf_features, columns=[f"feature_{i}" for i in range(tfidf_features.shape[1])])
feature_df.insert(0, "id", df["id"])  # Retain original ID
feature_df.to_csv("code_features.csv", index=False)

# Save the trained TF-IDF vectorizer
with open("tfidf_vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(tfidf_vectorizer, vectorizer_file)

print("Files saved: code_features.csv & tfidf_vectorizer.pkl")
