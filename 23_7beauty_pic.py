import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time

def convert_to_float(charNum='1/4'):
    x=charNum.split('/')
    return float(int(x[0])/int(x[1]))
def main():
    time1=time.time()
    count=0
    url='https://m.umei.cc/meinvtupian/meinvxiezhen/204337.htm'
    strhtml=requests.get(url)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    while count<40:
        datas=soup.select("#ArticleBox > p > a > img")
        for data in datas:
            picNet=data.get('src')
            f=open('pic/'+str(count)+'.png','wb')
            pic=requests.get(picNet)
            f.write(pic.content)
            f.close()
            count+=1
            print(count)
        datas=soup.select("div.pages > ul > li:nth-child(1) > a")
        for data in datas:
            page=str(data.get_text())
            pageNum=convert_to_float(page)
            print(pageNum)
        if pageNum==1:
            datas=soup.select("p:nth-child(3)")
            for data in datas:
                nextPage='https://m.umei.cc'
                dataStr=str(data)
                datalib=dataStr.split('"')
                nextPage+=datalib[1]
                strhtml=requests.get(nextPage)
                strhtml.encoding = 'utf-8'
                soup=BeautifulSoup(strhtml.text,'lxml')
        else:
            datas=soup.select("div.pages > ul > li:nth-child(3) > a")
            for data in datas:
                nextPic='https://m.umei.cc/meinvtupian/meinvxiezhen/'+data.get('href')
                strhtml=requests.get(nextPic)
                strhtml.encoding = 'utf-8'
                soup=BeautifulSoup(strhtml.text,'lxml')
    print(time.time()-time1)
    

    

if __name__=="__main__":
    main()
