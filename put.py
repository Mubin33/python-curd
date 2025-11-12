import requests
import json

URL = 'http://127.0.0.1:8000/aiquest/10/'

data = {
    'id': 10,
    'teachers_name': 'Arafat',
    'course_name': 'Hossain',
    'course_duration': 3333,
    'sit': 4444,
}

json_data = json.dumps(data)

# ✅ Add correct header
headers = {'Content-Type': 'application/json'}

r = requests.put(url=URL, data=json_data, headers=headers)

print("Status code:", r.status_code)
print("Response:", r.text)
