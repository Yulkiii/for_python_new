import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time
import ipGenerate
import http.cookiejar as cookielib
import json
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
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
    login=session.post(before,data = postData, headers = headers)
    print(login.content)
def download_json(site=""):
    strhtml=requests.get(site,verify=False)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    datas=soup.select("data")
    f=open("my.json","wb")
    f.write(strhtml.content)
    f.close()
def analist_json():
    data = json.load(open("my.json",encoding="utf-8"))
    print(data["famous"][0])



def main():
    #download_json("https://raw.githubusercontent.com/bizhili/acm/master/myweb.json")
    analist_json()
    exit(0)

if __name__=="__main__":
    main()
