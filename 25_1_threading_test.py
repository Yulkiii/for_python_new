import threading
import time
import queue
import requests
from bs4 import BeautifulSoup
count=0
threads=[]
next_site=queue.Queue()
def convert_to_float(charNum='1/4'):
    x=charNum.split('/')
    return float(int(x[0])/int(x[1]))
def get_first_one(charNum='1/4'):
    x=charNum.split('/')
    return int(x[0])
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, site, live):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.site =site
        self.live=live
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        if self.live:
            global count
            global next_site
            strhtml=requests.get(self.site)
            strhtml.encoding = 'utf-8'
            soup=BeautifulSoup(strhtml.text,'lxml')
            datas=soup.select("div.pages > ul > li:nth-child(1) > a")
            for data in datas:
                page=str(data.get_text())
                pageNum=convert_to_float(page)
                first=get_first_one(page)
            if first==1: 
                datas=soup.select("p:nth-child(3)")
                for data in datas:
                    nextPage='https://m.umei.cc'
                    dataStr=str(data)
                    datalib=dataStr.split('"')
                    nextPage+=datalib[1]
                    next_site.put(nextPage)
            if pageNum!=1:
                datas=soup.select("div.pages > ul > li:nth-child(3) > a")
                for data in datas:
                    nextPic='https://m.umei.Fcc/meinvtupian/meinvxiezhen/'+data.get('href')
                    next_site.put(nextPic)
            datas=soup.select("#ArticleBox > p > a > img")
            for data in datas:
                picNet=data.get('src')
                time1=str(time.time())
                f=open('pic/'+time1+'.png','wb')
                pic=requests.get(picNet)
                f.write(pic.content)
                f.close()
            print(count)
            count+=1
        self.live=0
def main():
    time1=time.time()
    global threads
    global next_site
    url='https://m.umei.cc/meinvtupian/meinvxiezhen/204337.htm'
    threads.append(myThread(0, url,1))
    for thread in threads:
        thread.start()
    while count<200:
        time.sleep(0.1)
        while not next_site.empty():
            thread=myThread(count,next_site.get(),1)
            thread.start()
    print(time.time()-time1)

if __name__ == "__main__":
    main()







