
import requests
url = 'http://www.httpbin.org/post'
d = {
    "file" : open('./file.txt', 'rb')

}
res = requests.post(url,files=d)
print(res.json())