import requests
import json
URL='http://127.0.0.1:8000/aicreate/'

data={
     "teachers_name" : "Shagor",
    "course_name" : "cst",
    "course_duration" : 44,
    "sit" : 6817,
}

json_data = json.dumps(data)
r= requests.post(url=URL, data=json_data)
data = r.json()
print(data)