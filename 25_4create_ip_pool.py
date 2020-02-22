import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import time
import ipGenerate

def convert_to_float(charNum='1/4'):
    x=charNum.split('/')
    return float(int(x[0])/int(x[1]))
def main():
    time1=time.time()
    ip_list = ipGenerate.get_ip_list()
    proxies = ipGenerate.get_random_ip(ip_list)
    url='https://blog.csdn.net/P_e_n_g___/article/details/104201201'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        'Accept':'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding':'gzip',
        'Connection':'close',
        'Referer':None
        }
    print(proxies)
    strhtml=requests.get(url,headers=headers,proxies=proxies,timeout=5)
    strhtml.encoding = 'utf-8'
    soup=BeautifulSoup(strhtml.text,'lxml')
    print(soup.contents)
    print(time.time()-time1)
    

    

if __name__=="__main__":
    main()
