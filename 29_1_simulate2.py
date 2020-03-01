import threading
import linecache
import numpy as np
import os
import matplotlib.pylab as plt
import time
import random
import math
import json

def main():
    data=[]
    with open("myData.json",'r') as load_f:
        load_dict = json.load(load_f)
    for i in load_dict:
        data.append(load_dict[i])
    '''
    plt.plot(data,'-',label='data')
    plt.xlabel("TIME/seconds")
    plt.ylabel("ANGLE/degrees")
    plt.show()
'''
    dataOriginal=[]
    dataProcessed=[]
    U1=1
    P1=1
    Preal1=0
    uncertain1=1
    uncertain1h=1
    U2=1
    uncertain2=2
    uncertain2h=10
    for i in load_dict:
        dataOriginal.append(load_dict[i])
        i=int(i)
        Preal1=math.sqrt(uncertain1*uncertain1+P1*P1)
        Kg=Preal1*Preal1/(Preal1*Preal1+uncertain2*uncertain2)
        U1=U1+Kg*(dataOriginal[i]-U1)
        dataProcessed.append(U1)
        P1=math.sqrt((1-Kg)*Preal1*Preal1)
        uncertain2h+=(dataOriginal[i]-U1)*(dataOriginal[i]-U1)
        if i>=1:
            uncertain1h+=(dataProcessed[i]-dataProcessed[i-1])*(dataProcessed[i]-dataProcessed[i-1])
    plt.xlabel("TIME/seconds")
    plt.ylabel("ANGLE/degrees")
    plt.plot(dataProcessed,'-',label='data2')
    plt.show()

if __name__=="__main__":
    main()