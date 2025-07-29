import requests
# url = 'http://www.httpbin.org/post'
# headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'} 

# res = requests.post(url,headers=headers)
# print(res.json())
# get 请求
url = 'http://www.httpbin.org/get'
headers = {'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
res = requests.get(url,headers=headers) 
print(res.json())