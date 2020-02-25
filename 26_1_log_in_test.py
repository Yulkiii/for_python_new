import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time
import ipGenerate
import http.cookiejar as cookielib
header={''
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSESSIONID=4100A9005B7BF814CD400E5611D83530',
    'Host': 'jwcas.cczu.edu.cn',
    'Origin': 'http://jwcas.cczu.edu.cn',
    'Referer': 'http://jwcas.cczu.edu.cn/login',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
def convert_to_float(charNum='1/4'):
    x=charNum.split('/')
    return float(int(x[0])/int(x[1]))

def get_info():
    firstUrl="http://jwcas.cczu.edu.cn/login"
    strhtml=requests.get(firstUrl,headers=header,timeout=5)
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
    login=session.post(before,data = postData, headers = header)
    #response=session.get(after,cookies = login.cookies, headers = headers)
    #f.write(response.text)
    #f.close()
    print(login.content)



    
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
