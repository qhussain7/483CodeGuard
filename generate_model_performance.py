import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load extracted features dataset
feature_df = pd.read_csv("code_features.csv")

# Simulate labels (0 = Not Similar, 1 = Similar)
np.random.seed(42)
feature_df["label"] = np.random.choice([0, 1], size=len(feature_df))

# Split dataset into train and test sets
X = feature_df.drop(columns=["id", "label"])
y = feature_df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Support Vector Machine": SVC(kernel="linear", random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=500, random_state=42)
}

# Evaluate models
model_results = []
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    model_results.append({
        "Model": model_name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, zero_division=1),
        "Recall": recall_score(y_test, y_pred, zero_division=1),
        "F1-Score": f1_score(y_test, y_pred, zero_division=1)
    })

# Save results to CSV
results_df = pd.DataFrame(model_results)
results_df.to_csv("model_performance.csv", index=False)

print("File saved: model_performance.csv")

import pickle

# Assuming best model is Random Forest (update this if needed)
best_model = RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5, random_state=42)
best_model.fit(X_train, y_train)  # Ensure model is trained

# Save the trained model
with open("model.pkl", "wb") as model_file:
    pickle.dump(best_model, model_file)

print("✅ Model saved successfully as model.pkl")
