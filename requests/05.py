
import requests
url = 'http://www.httpbin.org/post？name=xiaoming&age=18 '
d = {
    'name': 'xiaoming',
    'age': 18,
  
}
d1 = {
    "say": "hello python!"
}
res = requests.post(url, params=d,data=d1)
print(res.json())