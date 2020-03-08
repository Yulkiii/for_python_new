import threading
import linecache
import numpy as np
import os
import matplotlib.pylab as plt
import time
import random
import math
import json
#25 Hz
#4 ms 
def main():
    data=[]
    dic_new={}
    time=0
    count=0
    with open("myData.json",'r') as load_f:
        load_dict = json.load(load_f)
        #round funtion :keep x.00 ,two bites of float
        #json visit https://zhuanlan.zhihu.com/p/27917664
    for i in load_dict:
        time+=40
        data.append(round(load_dict[i],4))
        time1=round(random.random()/2-0.25+time,2)
        data.append(time1)
        dic_new[count]=data
        count+=1
        data=[]
    with open("myData2.json","w") as f:
        json.dump(dic_new,f)
        print("success")


if __name__=="__main__":
    main()