import requests

url = "http://127.0.0.1:5000/predict"

test_samples = [
    {"code": "def add_numbers(a, b): return a + b"},
    {"code": "def sum_two_numbers(x, y): return x + y"},
    {"code": "def multiply_values(a, b): return a * b"},
    {"code": "def product_numbers(x, y): return x * y"},
    {"code": "def divide_numbers(a, b): return a / b"},
    {"code": "def division_values(x, y): return x / y"},
]

for sample in test_samples:
    response = requests.post(url, json={"code_snippets": [sample["code"]]})
    result = response.json()
    prediction = result["predictions"][0]

    print(f"Code: {sample['code']}")
    print(f"Predicted Plagiarism: {prediction}")
    print("-" * 40)
