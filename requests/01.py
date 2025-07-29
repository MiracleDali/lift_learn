import requests
#1.发送get请求
res= requests.get('https://www.httpbin.org/get')

#2.拆分服务器地址和接口路径
from urllib.parse import urljoin
server = 'https://www.httpbin.org'
api_url = '/get'

url = urljoin(serverapi_url)
res = requests.get(url)
print(res.text)

