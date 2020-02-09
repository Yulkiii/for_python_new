import requests
from bs4 import BeautifulSoup
import re


def main():
    url='http://www.cntour.cn/'
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    #data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
    datas = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
    for item in datas:
        result={
            'title':item.get('title'),
            'link':item.get('href'),
            'ID':re.findall('\d+',item.get('href'))
        }
        print(result)

    print(datas)

    pass

if __name__=="__main__":
    main()


