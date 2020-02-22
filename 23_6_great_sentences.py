import requests
from bs4 import BeautifulSoup
import re


def main():
    count=0
    count2=0
    txtAll=''
    url='https://www.mingyantong.com/writer/taylor-swift'
    while count<100:
        strhtml=requests.get(url)
        soup=BeautifulSoup(strhtml.text,'lxml')
        datas=soup.select("div.views-field-phpcode-1 > a")
        count2+=1
        for data in datas:
            txtAll+='"泰勒斯威夫特a,'+str(data.get_text())+'b",\n'
            count+=1
            print(count)
        url="https://www.mingyantong.com/writer/taylor-swift?page="+str(count2)
    f=open("txt_file/txt2.txt","w")
    f.write(txtAll)
    f.close()

        

if __name__=="__main__":
    main()
