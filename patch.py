import requests
import json

URL = 'http://127.0.0.1:8000/aiquest/10/'

data = { 
    'sit': 555444,
}

json_data = json.dumps(data)

# ✅ Add correct header
headers = {'Content-Type': 'application/json'}

r = requests.patch(url=URL, data=json_data, headers=headers)

print("Status code:", r.status_code)
print("Response:", r.text)
