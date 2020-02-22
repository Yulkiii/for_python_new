import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time
import ipGenerate
import http.cookiejar as cookielib

def convert_to_float(charNum='1/4'):
    x=charNum.split('/')
    return float(int(x[0])/int(x[1]))
def main():
    time1=time.time()
    mafengwoSession = requests.session()
    # 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
    mafengwoSession.cookies = cookielib.LWPCookieJar(filename = "myCookies.txt")
    ip_list = ipGenerate.get_ip_list()
    proxies = ipGenerate.get_random_ip(ip_list)
    url="http://jwcas.cczu.edu.cn/login"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
        }
    postData = {
        'username': '18402218',
        'password': '07491X',
        'lt': 'LT-1824810-DWoUNvB73WNmIpfKGbBrZSrPKfCbZ4',
        'execution': 'e1s2',
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
