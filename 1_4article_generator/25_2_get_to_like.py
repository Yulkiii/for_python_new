import threading
import time
import queue
import requests
from bs4 import BeautifulSoup
count=0
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        global count
        count+=1
        url="https://lv.dingtalk.com/interaction/createLike?uuid=e6e41cd9-9009-456d-8d5e-a133c4898749&count=17"
        while count<100000:
            requests.get(url)
            if(count%1000==0):
                print(count)
            count+=1
        self.live=0
def main():
    time1=time.time()
    global count
    for _ in range (40):
        thread=myThread(count)
        thread.start()

    print(time.time()-time1)

if __name__ == "__main__":
    main()
