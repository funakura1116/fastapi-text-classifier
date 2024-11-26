import requests

url = "http://127.0.0.1:8000/predict"
data = {"text": "何度もアプリがクラッシュするので早急に対応してほしい"}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")