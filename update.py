import requests 
import json

URL='http://127.0.0.1:8000/aicreate/'

data={
    'id' : 9,
    'teachers_name' : 'Arafat',
    'course_name' : 'Hossain', 
    'course_duration' : 3333, 
    'sit' : 4444, 
}

json_data = json.dumps(data)
r= requests.put(url=URL, data=json_data)
data = r.json()
print(data)