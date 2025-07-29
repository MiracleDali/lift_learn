import requests
import json
url = 'http://www.httpbin.org/post'
d = {
    "key1": "value1",   
    "key2": "value2"

}
data_json = json.dumps(d)
res = requests.post(url, data=data_json)  
print(res.json())  