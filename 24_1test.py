import requests
from bs4 import BeautifulSoup
import re
#ArticleBox > p > a > img

def main():
    count=0
    url='https://m.umei.cc/meinvtupian/meinvxiezhen/204337.htm'
    strhtml=requests.get(url)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    datas=soup.select("#ArticleBox > p > a > img")
    for data in datas:
        
        print(data.get("src"))
        f=open('pic/'+str(count)+'.png','wb')
        pic=requests.get(data.get("src"))
        f.write(pic.content)
        f.close()



if __name__=="__main__":
    main()