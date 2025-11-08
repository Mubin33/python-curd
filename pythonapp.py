import requests

# URL = 'http://127.0.0.1:8000/aiinfo/'
response = requests.get('http://127.0.0.1:8000/aiinfo/')
data = response.json()
print(data)