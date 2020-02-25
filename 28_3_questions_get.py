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
    #f=open("my.html","w")
    login=session.post(before,data = postData, headers = headers)
    #response=session.get(after,cookies = login.cookies, headers = headers)
    #f.write(response.text)
    #f.close()
    print(login.content)

def main():
    headUrl="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?"
    firstUrl1="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BF%C6%C6%D5%CC%E2&tmlb=%B7%C0%BB%F0%B0%B2%C8%AB%D3%EB%B1%A3%C3%DC"
    firstUrl2="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BF%C6%C6%D5%CC%E2&tmlb=%CA%B5%D1%E9%CA%D2%B0%B2%C8%AB%B9%DC%C0%ED"
    firstUrl3="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BF%C6%C6%D5%CC%E2&tmlb=%D2%C7%C6%F7%C9%E8%B1%B8%A3%A8%CC%D8%D6%D6%C9%E8%B1%B8%A3%A9%CA%B9%D3%C3%B0%B2%C8%AB"
    firstUrl4="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BF%C6%C6%D5%CC%E2&tmlb=%D3%C3%B5%E7%B0%B2%C8%AB"
    firstUrl5="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BF%C6%C6%D5%CC%E2&tmlb=%BB%FA%D0%B5%B9%A4%B3%CC"
    firstUrl6="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BF%C6%C6%D5%CC%E2&tmlb=%BB%AF%D1%A7%CE%A3%CF%D5%C6%B7%CA%B9%D3%C3%B0%B2%C8%AB"
    firstUrl7="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BB%F9%B4%A1%CC%E2&tmlb=%CA%B5%D1%E9%CA%D2%B0%B2%C8%AB%B9%DC%C0%ED"
    firstUrl8="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BB%F9%B4%A1%CC%E2&tmlb=%D2%C7%C6%F7%C9%E8%B1%B8%A3%A8%CC%D8%D6%D6%C9%E8%B1%B8%A3%A9%CA%B9%D3%C3%B0%B2%C8%AB"
    firstUrl9="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BB%F9%B4%A1%CC%E2&tmlb=%D3%C3%B5%E7%B0%B2%C8%AB"
    firstUrl10="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BB%F9%B4%A1%CC%E2&tmlb=%C9%FA%CE%EF%D2%BD%D2%A9"
    firstUrl11="http://sysaq.cczu.edu.cn/xs/aqzsxx.asp?zycc=%B1%BE%BF%C6%C9%FA&zymc=%B8%DF%B7%D6%D7%D3%B2%C4%C1%CF%D3%EB%B9%A4%B3%CC&zyfl=%C7%E1%BB%AF%C0%E0&tmlx=%BB%F9%B4%A1%CC%E2&tmlb=%BB%AF%D1%A7%CE%A3%CF%D5%C6%B7%CA%B9%D3%C3%B0%B2%C8%AB"
    firstUrl="http://sysaq.cczu.edu.cn/xs/aqzsks.asp"
    lastUrl="view-source:http://sysaq.cczu.edu.cn/xs/aqzsks.asp"
    cookies={"cookie":"ASPSESSIONIDASCADBAR=GLJENJGCEPDBNOHELNCDFEGH"}
    strhtml=requests.get(lastUrl,headers=headers,timeout=5,cookies=cookies)
    strhtml.encoding = 'GBK'
    soup=BeautifulSoup(strhtml.text,'lxml')
    all=""
    for i in range(100):
        selectOne="#tr_S-JCT-HXWXPSYAQ-"+str(i)
        datas=soup.select(selectOne)
        for data in datas:
            data=str(data)
            qus=data.split("</font>\r\n")
            qus2=qus[1].split("\r\n")
            qusReal=qus2[0].replace(" ","")
            answ=data.split("答案:")
            answ2=answ[1].split("<")
            answReal=answ2[0]
            all+=qusReal+"\n"+answReal+"\n"
            print(i)
    for i in range(100):
        selectOne="#tr_L-JCT-HXWXPSYAQ-"+str(i)
        datas=soup.select(selectOne)
        for data in datas:
            data=str(data)
            qus=data.split("</font>\r\n")
            qus2=qus[1].split("\r\n")
            qusReal=qus2[0].replace(" ","")
            answ=data.split("答案:")
            answ2=answ[1].split("<")
            answReal=answ2[0]
            all+=qusReal+"\n"+answReal+"\n"
            print(i)
    f=open("data11.txt","w")
    f.write(all)
    f.close()



if __name__=="__main__":
    main()



