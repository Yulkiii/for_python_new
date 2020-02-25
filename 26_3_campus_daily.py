import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time
import ipGenerate
import http.cookiejar as cookielib
import json
cookie={"cookie":"acw_tc=76b20ffd15824710135263772e0f1a81f421aaf3dc9ba4279502867de7f5d4; userClientId=1582471048989e2n4gkkmr61rk4yglnl9; MOD_AUTH_CAS=ST-iap:1018565411790461:ST:9976c696-092f-40e1-9386-696ca7656745:20200224184721"}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }

def main():
    firstUrl="https://cczu.cpdaily.com/wec-counselor-collector-apps/stu/mobile/index.html?collectorWid=405#/notice"
    postData={"formWid":"261","collectWid":"405","schoolTaskWid":"","form":[{"wid":"6554","formWid":"261","fieldType":1,"title":"您的体温度数是：","description":"请同学们直接写数字。","minLength":1,"sort":"1","maxLength":300,"isRequired":1,"imageCount":"","hasOtherItems":0,"colName":"field001","value":"36.5","fieldItems":[]},{"wid":"6555","formWid":"261","fieldType":2,"title":"您是否有咳嗽现象？","description":"","minLength":0,"sort":"2","maxLength":"","isRequired":1,"imageCount":"","hasOtherItems":0,"colName":"field002","value":"否","fieldItems":[{"itemWid":"39873","content":"否","isOtherItems":0,"contendExtend":"","isSelected":""}]}]}
    postUrl="https://cczu.cpdaily.com/wec-counselor-collector-apps/stu/collector/submitForm"
    session=requests.session()
    login=session.post(postUrl,cookies=cookie,data=postData, headers = headers,timeout=5,verify=False)
    #strhtml=requests.get(firstUrl,cookies=cookie,headers=headers,timeout=5,verify=False)
    #strhtml.encoding="utf-8"
    #soup=BeautifulSoup(strhtml.text,'lxml')
    #datas=soup.select("body")
    print(login.text)

if __name__=="__main__":
    main()


'''
{"formWid":"261","collectWid":"395","schoolTaskWid":null,"form":[{"wid":"6554","formWid":"261","fieldType":1,"title":"您的体温度数是：","description":"请同学们直接写数字。","minLength":1,"sort":"1","maxLength":300,"isRequired":1,"imageCount":null,"hasOtherItems":0,"colName":"field001","value":"36.5","fieldItems":[]},{"wid":"6555","formWid":"261","fieldType":2,"title":"您是否有咳嗽现象？","description":"","minLength":0,"sort":"2","maxLength":null,"isRequired":1,"imageCount":null,"hasOtherItems":0,"colName":"field002","value":"否","fieldItems":[{"itemWid":"39873","content":"否","isOtherItems":0,"contendExtend":"","isSelected":null}]}]}
https://cczu.cpdaily.com/wec-counselor-collector-apps/stu/collector/submitForm
'''
