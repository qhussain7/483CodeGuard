import requests

url = "http://127.0.0.1:5000/predict"

test_samples = [
    {"code": "def add(a, b): result = a; result += b; return result"},
    {"code": "def sum_values(x, y): temp = x + 0; temp += y; return temp"},
    {"code": "def multiply(x, y): total = 1; total = total * x; total = total * y; return total"},
    {"code": "def multiplication(a, b): product = a * b; return product"},
    {"code": "def divide_numbers(x, y): temp = x / y; temp *= 1; return temp"},
    {"code": "def division_result(a, b): return (a / b) * 1"},
]

for sample in test_samples:
    response = requests.post(url, json={"code_snippets": [sample["code"]]})
    result = response.json()
    prediction = result["predictions"][0]

    print(f"Code: {sample['code']}")
    print(f"Predicted Plagiarism: {prediction}")
    print("-" * 40)
