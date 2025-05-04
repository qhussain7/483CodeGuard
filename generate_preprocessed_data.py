import pandas as pd
import re
import ast

# Function to clean source code (removes comments and whitespace)
def clean_code(code):
    code = re.sub(r'#.*', '', code)  # Remove single-line comments
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)  # Remove multi-line comments
    code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)
    return '\n'.join([line.strip() for line in code.splitlines() if line.strip()])

# Function to tokenize source code
def tokenize_code(code):
    return re.findall(r'\b\w+\b|[^\s\w]', code)

# Function to generate AST representation
def generate_ast(code):
    try:
        tree = ast.parse(code)
        return ast.dump(tree, annotate_fields=False)
    except Exception:
        return None

# Sample dataset (replace with real dataset)
sample_data = [
    {"id": 1, "code": "def add(a, b):\n    return a + b\n\n# This function adds two numbers"},
    {"id": 2, "code": "def multiply(a, b):\n    return a * b\n\n# Multiplication function"},
    {"id": 3, "code": "def add(a, b):\n    sum = a + b\n    return sum  # Returns sum"},
]

# Process dataset
processed_data = []
for entry in sample_data:
    cleaned_code = clean_code(entry["code"])
    tokenized_code = tokenize_code(cleaned_code)
    ast_representation = generate_ast(cleaned_code)
    
    processed_data.append({
        "id": entry["id"],
        "cleaned_code": cleaned_code,
        "tokens": tokenized_code,
        "ast": ast_representation
    })

# Convert to DataFrame and save
df = pd.DataFrame(processed_data)
df.to_csv("preprocessed_code_data.csv", index=False)

print("File saved: preprocessed_code_data.csv")
