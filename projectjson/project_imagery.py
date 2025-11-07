import json, numpy
with open('imaginary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f"Total entry : {len(data)}")