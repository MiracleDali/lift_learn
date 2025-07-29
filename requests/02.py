# post简单模拟
import requests

d={'name':'germey'} 
res = requests.post('http://httpbin.org/post', data=d)
# print(res.text)
print(res.json(),type(res.json()))
#data的字符串格式
s = 'name=germey'
res = requests.post('http://httpbin.org/post', data=s) 
print(res.json(),type(res.json()))