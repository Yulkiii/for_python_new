import requests
from bs4 import BeautifulSoup
import re


def main():
    url='https://blog.csdn.net/weixin_43013761/article/details/102698446'
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    txtFind=''
    txtAll=''
    for i in range(5,36):
        flag=0
        txtFind='#content_views > h1:nth-child('+str(i)+')'
        datas=soup.select(txtFind)
        if datas:
            result={datas[0].get_text()}
            txtAll+=''.join(result)+'\n'
        else :
            txtFind='#content_views > p:nth-child('+str(i)+') >a'
            datas=soup.select(txtFind)
            if datas:
                result2=''
                for data in datas:
                    result2='Describe: '+str(data.get_text())+'\n'+'Link: '+str(data.get('href'))
                    txtAll+=result2+'\n'
    f= open("txt_file/txt1.txt", "w")
    f.write(txtAll)
    f.close()
    print(txtAll)
    

if __name__=="__main__":
    main()
