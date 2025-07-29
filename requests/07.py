import requests
url = 'http://www.httpbin.org/cookies'
query_data = {'name': 'xiaoming',
    'age': 18}
header_data = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
cookies_data = {"sessinID":"123456" }
res=requests.get(url,params=query_data,headers=header_data,cookies=cookies_data)  
print(res.json)
