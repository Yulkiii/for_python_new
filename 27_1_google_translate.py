import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time
import ipGenerate
import http.cookiejar as cookielib
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
def convert_to_float(charNum='1/4'):
    x=charNum.split('/')
    return float(int(x[0])/int(x[1]))

def get_info():
    firstUrl="http://jwcas.cczu.edu.cn/login"
    strhtml=requests.get(firstUrl,headers=headers,timeout=5)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    datas=soup.select("#fm1 > div.submit > input[type=hidden]:nth-child(1)")
    it=""
    execu=""
    for data in datas:
        it=str(data.get("value"))
    datas=soup.select("#fm1 > div.submit > input[type=hidden]:nth-child(2)")
    for data in datas:
        execu=str(data.get("value"))
    return it,execu
def log_in():
    session=requests.session()
    it,execu=get_info()
    after="http://jwcas.cczu.edu.cn/login"
    before="http://jwcas.cczu.edu.cn/login"
    postData = {
        'username': '18402218',
        'password': '07491X',
        'lt': it,
        'execution': execu,
        '_eventId': 'submit',
        'submit': 'LOGIN'
    }
    #f=open("my.html","w")
    login=session.post(before,data = postData, headers = headers)
    #response=session.get(after,cookies = login.cookies, headers = headers)
    #f.write(response.text)
    #f.close()
    print(login.content)

def main():
    log_in()
    exit(0)
if __name__=="__main__":
    main()
'''
https://translate.google.cn/translate_a/single?client=webapp&s/
l=auto&tl=en&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&d/
t=ss&dt=t&dt=gt&otf=1&ssel=0&tsel=0&kc=2&tk=788513.703746&q=%E6%89%8B%E6%9C%BA
'''
