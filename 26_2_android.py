import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time
import ipGenerate
import http.cookiejar as cookielib
header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
def convert_to_float(charNum='1/4'):
    x=charNum.split('/')
    return float(int(x[0])/int(x[1]))

def get_info():
    firstUrl="https://cczu.cpdaily.com/iap/login?service=https%3A%2F%2Fcczu.cpdaily.com%2Fportal%2Flogin"
    strhtml=requests.get(firstUrl,headers=headers,timeout=5)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    datas=soup.select("#lt")
    it=""
    for data in datas:
        it=str(data.get("value"))
    return it
def log_in():
    session=requests.session()
    it=get_info()
    after="https://cczu.cpdaily.com/wec-counselor-collector-apps/stu/mobile/index.html?collectorWid=377&timestamp=1582446275893#/notice"
    before="https://cczu.cpdaily.com/iap/doLogin"
    postData = {
        'username': '18402218',
        'password': 'LIXING12345',
        'lt': it,
        'captcha':"",
        'rememberMe': 'false'
    }
    f=open("my.txt","w")
    cookie={"cookie":"acw_tc=76b20ff815824479378691816e1d7601742fd841d7b987a6eadae038be152b; MOD_AUTH_CAS=ST-iap:1018565411790461:ST:8eaeee32-06e9-404c-9477-56630b20d74b:20200223165227"}
    login=session.post(before,data = postData, headers = header)
    response=session.get(after,cookies = cookie, headers = headers)
    f.write(str(login.cookies))
    f.close()
    print(response.text)

def main():
    log_in()
    exit(0)
    time1=time.time()
    mafengwoSession = requests.session()
    # 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    mafengwoSession.cookies = cookielib.LWPCookieJar(filename = "myCookies.txt")
    ip_list = ipGenerate.get_ip_list()
    proxies = ipGenerate.get_random_ip(ip_list)
    url="http://jwcas.cczu.edu.cn/login"

    postData = {
        'username': '18402218',
        'password': '07491X',
        'lt':" ",
        'execution': " ",
        '_eventId': 'submit',
        'submit': 'LOGIN',
    }
    responseRes = mafengwoSession.post(url, data = postData, headers = headers)
    print(f"statusCode = {responseRes.status_code}")
    mafengwoSession.cookies.save()
    exit (0)
    print(proxies)
    strhtml=requests.get(url,headers=headers,proxies=proxies,timeout=3)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    print(soup.contents)
    print(time.time()-time1)
    

    

if __name__=="__main__":
    main()
