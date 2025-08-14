import requests


# 密码加密逻辑：md5(md5(password) + rand)
# 1.md5方法：拿到网页的 md5.js文件  
# 2.password值： quickon4You --> 密码明文
# 3.rand值： https://software.demo.qucheng.cc/index.php?m=user&f=refreshRandom 

# 拿到cookie
cookie_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
}
cookie_url = 'https://software.demo.qucheng.cc/index.php?m=user&f=login'
res_cookie = requests.get(url=cookie_url, headers=cookie_header)
cookie_d = requests.utils.dict_from_cookiejar(res_cookie.cookies)
print(cookie_d)


# 密码的加密
# 1. rand的获取
rand_url = "https://software.demo.qucheng.cc/index.php?m=user&f=refreshRandom"
header_rand = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://software.demo.qucheng.cc/index.php?m=user&f=login&referer=L2luZGV4LnBocD9tPW15JmY9aW5kZXg='
}
res_rand = requests.get(url=rand_url, headers=header_rand, cookies=cookie_d)
print(res_rand.text)





# 2.使用python 调用js文件中的方法，也就是这里的md5文件
# pip install PyExecJS  安装需要的库
# 下面这段代码最好单独放在一个文件中使用时调用
import execjs
import os

rootpath = os.path.dirname(__file__)
jspath = os.path.join(rootpath, "md5.js")

class ExecJs():
    
    _instance = False

    def _get_js(self, name):
        js_str = ""
        with open (name, "r", encoding="utf-8") as f:
            line = f.readline()
            while line:
                js_str = js_str + line
                line = f.readline()
        return js_str
    
    def get_encrypt_pwd(self, function, *args):
        ctx = execjs.compile(self._get_js(jspath))
        return ctx.call(function, *args)

e = ExecJs()
# 进行MD5加密密码明文
step1 = e.get_encrypt_pwd('md5', 'quickon4You')
step2 = e.get_encrypt_pwd('md5', step1 + res_rand.text)
print(step2)




url = "https://software.demo.qucheng.cc/index.php?m=user&f=login"
data = {
    'account': 'demo',
    'password': step2,
    'passwordStrength': '1',
    'referer': '/index.php?m=my&f=index',
    'verifyRand': res_rand.text,
    'keepLogin': '0',
    'captcha': ''
}

header = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '788',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryrNOKvRRI3UxYlolI',
    'priority': 'u=1, i',
    'referer': 'https://software.demo.qucheng.cc/index.php?m=user&f=login&referer=L2luZGV4LnBocD9tPW15JmY9aW5kZXg=',
    # 'sec-ch-ua': "Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138",
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'x-requested-with': 'XMLHttpRequest'
}


res = requests.post(url=url, data=data, headers=header, cookies=cookie_d)
print(res.text)




