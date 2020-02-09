import requests
import json

url = 'http://httpbin.org/post'
s = json.dumps({'key1': 'value1', 'key2': 'value2'})
r = requests.post(url, data=s)
print (r.text)

url = 'http://jwcas.cczu.edu.cn/login?locale=en'
s = json.dumps({'username': '18402218', 'password': '07491X','warn':0,'rememberMe':0})
r = requests.post(url, data=s)
print (r.text)
